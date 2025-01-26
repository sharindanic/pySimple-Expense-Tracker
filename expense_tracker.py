expenses = []

def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter the expense description: ")
        amount = float(input("Enter the amount: "))
        expenses.append({"date": date, "description": description, "amount": amount})
        print("Expense added!")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}")
    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal Amount Spent: ${total:.2f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
