import json
import os

def load_expenses(filename="expenses.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (Food, Transport, Entertainment, etc.): ").strip()
        description = input("Enter a brief description: ").strip()
        
        expenses.append({"amount": amount, "category": category, "description": description})
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numerical value for amount.")

def analyze_expenses(expenses):
    category_totals = {}
    total_spent = 0
    
    for expense in expenses:
        total_spent += expense["amount"]
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    
    print("\nExpense Summary:")
    print(f"Total Spent: ${total_spent:.2f}")
    print("Category-wise Spending:")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            analyze_expenses(expenses)
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
