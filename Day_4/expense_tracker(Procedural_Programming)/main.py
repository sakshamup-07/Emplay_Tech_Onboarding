
import json

expenses = []

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    expenses = []


def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero")
            else:
                break

        except ValueError:
            print("Please enter a valid number")

    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty")

    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        print("\n----- ALL EXPENSES -----")

        for i, expense in enumerate(expenses, start=1):
            print(
                i,
                "| Amount:", expense["amount"],
                "| Category:", expense["category"],
                "| Description:", expense["description"]
            )


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses:", total)


def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)

            with open("expenses.json", "w") as file:
                json.dump(expenses, file, indent=4)

            print("Deleted:", deleted["description"])

        else:
            print("Invalid expense number")

    except ValueError:
        print("Please enter a valid number")


while True:
    print("\n-- EXPENSE TRACKER ")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
