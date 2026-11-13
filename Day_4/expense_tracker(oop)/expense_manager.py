
import json
from expense import Expense


class ExpenseManager:

    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)

                for item in data:
                    expense = Expense(
                        item["amount"],
                        item["category"],
                        item["description"]
                    )

                    self.expenses.append(expense)

        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_expenses(self):
        data = []

        for expense in self.expenses:
            data.append(expense.to_dict())

        with open("expenses.json", "w") as file:
            json.dump(data, file, indent=4)

    def add_expense(self):
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

        expense = Expense(amount, category, description)

        self.expenses.append(expense)
        self.save_expenses()

        print("Expense added successfully!")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found")
            return

        print("\n----- ALL EXPENSES -----")

        for i, expense in enumerate(self.expenses, start=1):
            print(i, end=" | ")
            expense.display()

    def total_expenses(self):
        total = 0

        for expense in self.expenses:
            total += expense.amount

        print("Total expenses:", total)

    def delete_expense(self):
        if len(self.expenses) == 0:
            print("No expenses to delete")
            return

        self.view_expenses()

        try:
            choice = int(input("Enter expense number to delete: "))

            if 1 <= choice <= len(self.expenses):
                deleted = self.expenses.pop(choice - 1)

                self.save_expenses()

                print("Deleted:", deleted.description)

            else:
                print("Invalid expense number")

        except ValueError:
            print("Please enter a valid number")
