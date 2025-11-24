# main.py
from expense_manager import add_expense, view_expenses
from report_generator import monthly_report
from budget_manager import set_budget, check_budget


def menu():
    while True:
        print("\n=== Smart Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Report")
        print("4. Set Budget")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_report()
            check_budget()
        elif choice == "4":
            set_budget()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")


if __name__ == '__main__':
    menu()
