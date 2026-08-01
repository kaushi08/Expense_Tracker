# Expense Tracker

A simple command-line **Expense Tracker** built with Python that helps users record, manage, and track their daily expenses. The application allows users to add, view, calculate, and delete expenses while storing data in a text file, ensuring records are preserved between sessions.

This project is designed for beginners to strengthen their understanding of Python fundamentals, file handling, and data management.

## Features

* Add new expenses
* View all recorded expenses
* Calculate total expenses
* Delete unwanted expense records
* Store expense data in a text file
* Automatically load saved expenses when the application starts
* Simple and interactive menu-driven interface

## Technologies Used

* Python 3
* Built-in `os` module
* Text file storage (`expenses.txt`)

## Concepts Covered

* Variables
* Lists
* Dictionaries
* Functions
* Loops (`while`)
* Conditional statements (`if`, `elif`, `else`)
* File handling (Read and Write)
* CRUD Operations (Create, Read, Update, Delete)
* Basic data management

## Project Structure

```text
ExpenseTracker/
│── main.py
└── expenses.txt
```

## How to Run

1. Clone the repository.
2. Open the project in PyCharm (or any Python IDE).
3. Make sure an empty `expenses.txt` file exists in the project folder.
4. Run the following command:

```bash
python main.py
```

## Sample Output

```text
====== EXPENSE TRACKER ======

1. Add Expense
2. View Expenses
3. Total Expense
4. Delete Expense
5. Exit

Choose an option: 1

Enter amount: ₹250
Enter category: Food
Enter description: Lunch

Expense added successfully!
```

## Future Improvements

* Add the current date automatically
* Edit existing expenses
* Search expenses by category
* Filter expenses by date
* Monthly and yearly expense reports
* Budget tracking with spending alerts
* Data visualization using Matplotlib
* Store data in SQLite instead of a text file
* Graphical User Interface (GUI) using Tkinter or CustomTkinter

## Learning Outcomes

By completing this project, you will gain practical experience with:

* Python programming fundamentals
* File handling and persistent storage
* Working with lists and dictionaries
* Organizing code using functions
* Building menu-driven applications
* Managing structured data in Python

## Author

**Kaushika B**
