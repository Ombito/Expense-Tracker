from expense  import User, Expense, Category, engine, sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)

    #add new expense transaction to the database
def add_expense():
    username = input("Enter your username: ")
    date = input("Enter the date of transaction - (YYYY-MM-DD): ")
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter amount: "))
    category = input("Enter the category: ")

       
    session = Session()

        # check if the username exists and save data to database
    user = session.query(User).filter_by(username=username).first()
    if user:
        
        date = datetime.strptime(date, "%Y-%m-%d").date()

        new_expense = Expense(user=user, category=category, date=date, description=description,amount=amount)
        session.add(new_expense)
        session.commit()
        print("\n\nExpense added successfully.")
    else:
        print("User not found. Please enter a valid user ID.")


    #fetch all expenses for a user
def view_expenses():
    username = input("Enter your username: ")
    session = Session()

    user = session.query(User).filter_by(username=username).first()
    if user:
        expenses = session.query(Expense).filter_by(user_id=user.user_id).all()
        if expenses:
            print("\nExpense List: ")
            for expense in expenses:
                print(f"Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}")
        else:
            print("No expenses found for this user.")
    else:
        print("User not found. Please enter a valid user ID.")


    # delete the selected expenses and commit to the database
def delete_expense():
    username = input("Enter your username: ")
    description = input("Enter the description of the expense you want to delete: ")
    amount = float(input("Enter amount of the expense: "))

    session = Session()
       
    user = session.query(User).filter_by(username=username).first()

    if user:
            expenses_to_delete = session.query(Expense).filter(Expense.user == user, Expense.description == description, Expense.amount <= amount).all()

            if expenses_to_delete:
                print("\nExpenses to delete:")
                for expense in expenses_to_delete:
                    print(f"ID: {expense.id}, Category: {expense.description}, Amount: {expense.amount}")
                
                expense_ids = [expense.id for expense in expenses_to_delete]
                confirm = input("\n\nDo you want to delete these expenses? (yes/no): ").lower()

                if confirm == "yes":
                    for expense_id in expense_ids:
                        expense = session.query(Expense).filter_by(id=expense_id, user=user).first()
                        if expense:
                            session.delete(expense)

                    session.commit()
                    print("Expenses deleted successfully!")
                else:
                    print("Deletion canceled.")
            else:
                print("No expenses found with the given category and amount.")
    else:
            print("User not found. Please check your username.")

def update_expense():
    username = input("Enter your username: ")
    description = input("Enter the description of the expense you want to delete: ")
    
    session = Session()
    user = session.query(User).filter_by(username=username).first()

    if user:
        expense = session.query(Expense).filter(Expense.user == user, Expense.description == description).first()
        if expense:
            print(f"Current Expense Details:")
            print(f"Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}")
            
            new_date = input("Enter the new date (YYYY-MM-DD) or press Enter to keep the current date: ")
            new_description = input("Enter the new description or press Enter to keep the current description: ")
            new_amount = input("Enter the new amount or press Enter to keep the current amount: ")

            if new_date:
                expense.date = datetime.strptime(new_date, "%Y-%m-%d").date()
            if new_description:
                expense.description = new_description
            if new_amount:
                expense.amount = float(new_amount)
            
            session.commit()
            print("Expense updated successfully.")
        else:
            print("Expense not found for this user.")
    else:
        print("User not found. Please check your username.")





    #The selection menu
def main_menu():
    while True:
        print("\n\nSelect an option...\n")
        print("0. Sign-In")
        print("1. Enter a new expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Update expense")
        print("5. Search for an expense")
        print("6. Quit\n")

        choice = int(input())

        if choice == 0:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            session = Session()
            user = session.query(User).filter_by(username=username, password=password).first()

            if user:
                print("\nSIGN-IN SUCCESSFUL. WELCOME,", username + "!")
            else:
                print("\nSign-in failed. Please check your username and password.")

        elif choice == 1:
            add_expense()

        elif choice == 2:
            print("View your expenses")
            view_expenses()

        elif choice == 3:
            print("Select an expense to delete " )
            delete_expense()

        elif choice == 4:
            print("Select an expense to update " )
            update_expense()

        elif choice == 5:
            print("Select an expense to search" )
            search_expense()

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main_menu()