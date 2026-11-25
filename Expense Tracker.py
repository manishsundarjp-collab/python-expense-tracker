print("----------Personal Expense-----------")

print("1. Add Expense")
print("2. View Expense")        
print("3. View Total Spending")
print("4. View Spending by Category")
print("5. Exit")

records=int(input("Enter the number of records you want to add: "))

expenses = []

choice = input("Enter your choice (1-5): ")

for i in range(records):
         if choice == '1':
             name = input("Enter expense name: ")
             amount = float(input("Enter expense amount: ")) 
             category = input("Enter expense category: ")
             expenses.append((name, amount, category))
             print("Expense added successfully.")

         elif choice == '2': 
             print("Your Expenses:")
             for expense in expenses:
                 print(f"{expense[0]}: ${expense[1]:.2f} ({expense[2]})")

         elif choice == '3':
                total = sum(expense[1] for expense in expenses)
                print(f"Total Spending: ${total:.2f}")

         elif choice == '4':
                category = input("Enter category to view spending: ")
                category_expenses = [expense for expense in expenses if expense[2] == category]
                if category_expenses:
                    print(f"Expenses in {category}:")
                    for expense in category_expenses:
                        print(f"{expense[0]}: ${expense[1]:.2f}")
                else:
                    print(f"No expenses found in {category}.")

         elif choice == '5':
            print("Exiting the program.")
            print("Thank you for using the Personal Expense Tracker.")
            break

         else:
            print("Invalid choice. Please enter a number between 1 and 5.")         
