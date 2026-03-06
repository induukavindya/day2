# Budget Calculator Script
# This script calculates the remaining balance after subtracting expenses from the total monthly budget.

def main():
    # Ask for total monthly budget
    try:
        budget = float(input("Enter your total monthly budget: LKR"))
    except ValueError:
        print("Invalid input for budget. Please enter a number.")
        return

    expenses = []
    expense_count = 1
    while True:
        user_input = input(f"Enter expense {expense_count} (or type 'done' to finish): LKR")
        
        if user_input.lower() == "done":
            if not expenses:
                print("Please enter at least one expense.")
                continue
            break
        
        try:
            expense = float(user_input)
            if expense < 0:
                print("Expense cannot be negative. Please try again.")
                continue
            expenses.append(expense)
            expense_count += 1
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")
            continue

    # Calculate total expenses
    total_expenses = sum(expenses)

    # Calculate remaining balance
    remaining_balance = budget - total_expenses

    # Check for low funds
    if remaining_balance < 500:
        print("Warning: Low Funds")

    # Display remaining balance
    print(f"\nTotal Expenses: LKR{total_expenses:.2f}")
    print(f"Remaining Balance: LKR{remaining_balance:.2f}")

if __name__ == "__main__":
    main()