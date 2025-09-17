# CS50 Project: LOST ARK Gold Tracker

#### 🎥 Video Demo: [Watch Here](https://youtu.be/m5vTIA3Jlx8)

---

## 📝 Description

I decided to make this app after seeing my gold magically disappear for the past 6 months…

Using **Django**, this web application keeps track of your gold **expenses and income** in the MMORPG game **LOST ARK**.  
By tracking when, where, and how your gold is spent or earned, you can manage your gold more wisely — after all, gold is the ultimate currency in Lost Ark.

---

## ⚙️ Features

### Account & Authentication
- Register with a **username**, **email**, and **password** (password must be longer than 6 characters).  
- Email validation using Django's `validate_email`.  
- Prevents duplicate usernames or emails in the database.  
- Convenient **register/login toggle button** for easy navigation.  
- Successful login redirects you to the index expenses page with a **"login successful"** message.

### Expenses & Income Tracking
- **Paginator** shows only the first 3 rows of transactions per page (sorted by date, newest first).  
- Navigate between pages easily or jump to the first/last page.  
- **Create, edit, delete transactions** with the following fields:  
  - **Amount** (gold)  
  - **Description**  
  - **Date** (defaults to today)  
  - **Source** (for income) / **Category** (for expenses)  
- **Instant search bar** searches all fields without a submit button. Displays "No results found" if nothing matches.

### Visual Analytics
- View your transactions as **doughnut charts** grouped by category/source.  
- Visually track spendings and earnings with clear colors and a dark background for easy readability.

### Navigation & UI
- Sidebar links to **Expenses**, **Income**, and **Doughnut charts** pages.  
- Breadcrumbs at the top for convenient page context.  
- Dark mode design for an aesthetically pleasing experience.

---

## 💡 Goal

To make tracking gold in LOST ARK **simple, convenient, and visually insightful**, so players can better understand their spending habits.

---

## 📁 Project Structure

The app consists of 3 Django apps:  
1. `expenses` – track and categorize your gold spent  
2. `income` – track and categorize gold earned  
3. `authentication` – register, login, and manage users
