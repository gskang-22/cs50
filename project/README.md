# LOST ARK gold tracker
#### Video Demo:  https://youtu.be/m5vTIA3Jlx8

#### Description:
Decided to make this after seeing my gold magically disappear for the past 6 months...

Using Django, this web application keeps track of your gold expenses and income in the mmorpg game LOST ARK.
By tracking your incomes and expenses, as well as the where and when you spent/ earned your
gold, you might be able to manage you gold more wisely. After all, gold is THE currency in Lost Ark.


This app has a total of 3 apps: expenses, income, and authentication. Using a username, email, and password,
you can register for an account. Then, you would be sent to the index expenses page along with a "login
successful" message.

For both expenses and income, by using a paginator, clutter is reduced and you only see 3 rows of your
transactions. You are free to toggle between the different pages, and also to the first and last page

You are also able to create, edit and delete any transactions. The transactions have a total of 4 elements:
amount (of gold), description (details about the transaction), date (of transaction) that is, by default, today's date,
and finally source (for income) / categories (for expenses).

You can also search for a transaction using the search bar at the top right that without needing a submit button.
This search field searches through all 4 elements of expenses/ income and returns you the appropriate transaction
records. If no transaction fits the seach requirements, 

Moreover, you can also view your transactions in the form of "doughnut" tables that helps you understand your
spending and earning better visually.

Overall, hope you find this app useful (and enjoy the "dark mode" design) :)