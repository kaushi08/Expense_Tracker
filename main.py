import os

FILE_NAME = "expenses.txt"


def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                amount, category, description = line.strip().split(",")
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "description": description
                })

    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        for expense in expenses:
            file.write(
                f"{expense['amount']},{expense['category']},{expense['description']}\n"
            )


def add_expense(expenses):
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    save_expenses(expenses)

    print("\nExpense added successfully!\n")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.\n")
        return

    print("\n===============================")
    print("       EXPENSE LIST")
    print("===============================")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']} | {expense['category']} | {expense['description']}"
        )

    print()


def total_expense(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expense: ₹{total:.2f}\n")


def delete_expense(expenses):
    view_expenses(expenses)

    if len(expenses) == 0:
        return

    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(expenses):
        deleted = expenses.pop(index)
        save_expenses(expenses)
        print(f"\nDeleted: {deleted['description']}\n")
    else:
        print("Invalid expense number.\n")


def main():
    expenses = load_expenses()

    while True:

        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()