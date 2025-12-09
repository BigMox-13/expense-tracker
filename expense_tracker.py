print("Welcome to the Daily Expense Tracker!")
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

# Initialize an empty list to store expenses
expenses = []

while True:
    # Get user selection
    selection = input()

    if selection == "1":
        # Add a new expense
        new_expense = float(input())
        expenses.append(new_expense)
        print("Expense added successfully!")

    elif selection == "2":
        # View all expenses
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i +1}. {expenses[i]}")

    elif selection == "3":
        # Calculate total and average expense
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0
            for i in range(len(expenses)):
                total += expenses[i]
            average = total / len(expenses)
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")

    elif selection == "4":
        # Clear all expenses
        expenses = []
        print("All expenses cleared.")

    elif selection == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    else:
        # Invalid choice check
        print("Invalid choice. Please try again.")
