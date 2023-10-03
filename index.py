
def main():
    while True:
        print("Select an option...\n")
        print("1. Enter a new expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Quit\n")

        choice = int(input())

        if choice == 1:
            date = input("Enter the date of transaction - (YYYY-MM-DD): ")
            description = input("Enter the description of the expense: ")
            amount = float(input("Enter amount: "))

            categories = [ "Transport", "Savings", "Food", "Clothing", "Entertainment", "Rent", "Airtime", "Travel" ]

            while True:
                for i, category_name in enumerate(categories):
                    print(f" {i + 1}. {category_name}")
                break

        elif choice == 2:
            print("Select a category... ")
            input("Enter the category: ")

        elif choice == 3:
            print("Select an expense... " )

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter a valid number.")

main()