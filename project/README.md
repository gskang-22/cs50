# LOST ARK gold tracker
#### Video Demo:  https://youtu.be/m5vTIA3Jlx8

#### Description:
Decided to make this after seeing my gold magically disappear for the past 6 months...

Using Django, this web application keeps track of your gold expenses and income in the mmorpg game LOST ARK.
By tracking your incomes and expenses, as well as the where and when you spent/ earned your
gold, you might be able to manage your gold more wisely. After all, gold is THE currency in Lost Ark.

This app has a total of 3 apps: expenses, income, and authentication. Using a username, email, and password,
you can register for an account. The password has to be longer than 6 characters, while the email is validated
via validate_email provided by Django. The form also compared with the database and ensures that there are no
repeating usernamees or email addresses. With a register/ login link button below the input fields, changing between
the pages are made convenient and easy.

Upon successful login, you would be sent to the index expenses page along with a "login successful" message.

For both expenses and income, by using Django's paginator, clutter is reduced and you only see the first 3 rows of your
transactions, which are sorted by date in descending order. You are free to toggle between the different pages, and also
able to skip to the first and last pages.

You are also able to create, edit and delete any transactions. The transactions have a total of 4 elements:
amount (of gold), description (details about the transaction), date (of transaction), that is today's date by default,
and finally source (for income) / categories (for expenses) that allows users to understand where their gold came from/
"disappeared" to.

You can also search for a transaction using the search bar at the top right without the need for a submit button.
This search field searches through all 4 elements of expenses/ income and returns the appropriate transaction
records. If no transaction fits the search requirements, a "No results found" text will pop-up.

Moreover, you can also view your transactions in the form of "doughnut" graphs that helps you understand your
spendings and earnings better visually. These graphs group your expenses/income according to their categories/ sources. 
With differing colors and a black background, the graphs made easier to understand.

With a sidebar with links to the pages for expenses and income, as well as to the "doughnut" charts for visual display,
users are able to easily move between the different app pages with a click of a button. The presence of "breadcrumbs" near
the top of the page also helps add to the user's convenience.

Overall, hope you find this app useful (and enjoy the "dark mode" design) :)

