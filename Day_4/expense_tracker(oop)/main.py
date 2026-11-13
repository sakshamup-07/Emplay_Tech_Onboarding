
from expense_manager import ExpenseManager

manager = ExpenseManager()

while True:
    print("\n----- EXPENSE TRACKER -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_expense()

    elif choice == "2":
        manager.view_expenses()

    elif choice == "3":
        manager.total_expenses()

    elif choice == "4":
        manager.delete_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
