from expense  import User, Expense, Category, engine, sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)

def add_expense():
    username = input("Enter your username: ")
    date = input("Enter the date of transaction - (YYYY-MM-DD): ")
    description = input("Enter the description of the expense: ")
    amount = float(input("Enter amount: "))
    category = input("Enter the category: ")

       
    session = Session()

        # Check if the user with the given user_id exists
    user = session.query(User).filter_by(username=username).first()
    if user:
        
        date = datetime.strptime(date, "%Y-%m-%d").date()

        new_expense = Expense(user=user, category=category, date=date, description=description,amount=amount)
        session.add(new_expense)
        session.commit()
        print("\n\nExpense added successfully.")
    else:
        print("User not found. Please enter a valid user ID.")


def view_expenses():
    username = input("Enter your username: ")
    session = Session()

        # Check if the user with the given user_id exists
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



def delete_expense():
    username = input("Enter your username: ")
    expense_id = int(input("Enter the ID of the expense you want to delete: "))

    session = Session()

    user = session.query(User).filter_by(username=username).first()
    if user:
        expense = session.query(Expense).filter_by(expense_id=expense_id, username=username).first()
        if expense:
            session.delete(expense)
            session.commit()
            print("Expense deleted successfully.")
        else:
            print("Expense not found for this user.")
    else:
        print("User not found. Please enter a valid user ID.")


def main_menu():
    while True:
        print("\n\nSelect an option...\n")
        print("0. Sign-In")
        print("1. Enter a new expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Quit\n")

        choice = int(input())

        session = Session()


        if choice == 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            add_expense()

            # Check if the entered username and password match a user in the database
            user = session.query(User).filter_by(username=username, password=password).first()

            if user:
                print("\nSIGN-IN SUCCESSFUL. WELCOME,", username + "!")
            else:
                print("\nSign-in failed. Please check your username and password.")



        elif choice == 2:
            print("Select a category... ")
            view_expenses()

        elif choice == 3:
            print("Select an expense... " )
            delete_expense()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main_menu()