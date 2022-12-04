import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("SELECT symbol, SUM(shares_number) FROM users_history WHERE user_id = ? GROUP BY symbol", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session ["user_id"])[0]["cash"]
    investment_total = 0

    for row in rows:
        if row["SUM(shares_number)"] == 0:
            rows.remove(row)
            continue

        stock_quote = lookup(row["symbol"])
        row["name"] = stock_quote["name"]
        row["price"] = stock_quote["price"]
        row["total"] = row["price"] * row["SUM(shares_number)"]
        investment_total += stock_quote["price"]

    grand_total = cash + investment_total
    cash = cash

    return render_template("index.html", grand_total=grand_total, rows=rows, cash=cash)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        get_quote = lookup(request.form.get("symbol"))
        shares_number = int(request.form.get("shares"))

        if not isinstance(shares_number, int):
            return apology("number of shares is not a positive integer", 400)
        shares_number = int(shares_number)

        if not request.form.get("symbol"):
            return apology("input symbol is blank", 400)
        elif shares_number <= 0:
            return apology("number of shares is not a positive integer", 400)
        elif not get_quote:
            return apology("symbol does not exist", 400)
        elif not shares_number:
            return apology("input number of shares", 400)

        name = get_quote["name"]
        price = get_quote["price"]
        symbol = get_quote["symbol"]
        price_total = price * shares_number

        user_current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        if user_current_cash[0]["cash"] < price_total:
            return apology("insufficient cash", 400)

        cash_left = user_current_cash[0]["cash"] - price_total

        now = datetime.datetime.now()
        db.execute("INSERT INTO users_history (user_id, date, type, symbol, price, shares_number) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], now, "buy", symbol, price, shares_number)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_left, session["user_id"])

        return redirect("/")

@app.route("/history")
@login_required
def history():
    rows = db.execute("SELECT * FROM users_history WHERE user_id = ?", session["user_id"])
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    if request.method == "POST":
        input_symbol = request.form.get("symbol")
        get_quote = lookup(input_symbol)
        if not get_quote:
            return apology("symbol does not exist", 400)
        name = get_quote["name"]
        price = get_quote["price"]
        symbol = get_quote["symbol"]
        return render_template("quoted.html", name=name, price=price, symbol=symbol)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        if not username:
            return apology("must provide username", 400)

        elif not password or not confirmation:
            return apology("must provide password", 400)
        elif password != confirmation:
            return apology("passwords don't match", 400)

        rows = db.execute("SELECT username FROM users")

        for row in rows:
            if username == row["username"]:
                return apology("username taken", 400)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        return redirect("/")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        rows = db.execute("SELECT symbol, SUM(shares_number) FROM users_history WHERE user_id = ?", session["user_id"])

        for row in rows:
            if row['SUM(shares_number)'] == 0:
                rows.remove(row)

        return render_template("sell.html", rows=rows)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        get_quote = lookup(symbol)
        price = get_quote["price"]
        now = datetime.datetime.now()
        rows = db.execute("SELECT symbol, SUM(shares_number) FROM users_history WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)

        if shares <= 0:
            return apology("number of shares is not a positive integer", 400)
        elif not shares:
            return apology("input number of shares", 400)
        elif not symbol:
            return apology("invalid symbol", 400)
        elif not get_quote:
            return apology("symbol does not exist", 400)

        if shares > rows[0]["SUM(shares_number)"]:
            return apology("insufficient shares", 400)



        shares = 0 - shares
        db.execute("INSERT INTO users_history (user_id, date, type, symbol, price, shares_number) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], now, "sell", symbol, price, shares)
        return redirect("/")

@app.route("/change", methods=["GET", "POST"])
@login_required
def change():
    if request.method == "GET":
        return render_template("change.html")
    if request.method == "POST":
        password_old = request.form.get("password")
        password_new = request.form.get("password_new")
        password_confirm = request.form.get("password_confirm")

        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if password_new != password_confirm:
            return apology("passwords don't match", 304)
        elif not check_password_hash(rows[0]["hash"], password_old):
            return apology("invalid password", 400)
        elif not password_new:
            return apology("enter new password", 400)
        else:
            db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(password_new), session["user_id"])
            return redirect("/")
