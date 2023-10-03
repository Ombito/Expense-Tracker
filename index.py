from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base
engine = create_engine("sqlite:///my_database.db")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    date = Column(datetime, server_default=func.now())
    category = Column(String())

while True:
    print("Select an option\n")
    print("1. Enter a new expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Quit\n")

    choice = int(input())

    if choice == 1:
        date = input("Enter the date of transaction - (YYYY-MM-DD): ")
        description = input("Enter the description of the expense: ")
        category = input("Enter the category")

    elif choice == 2:
        pass

    elif choice == 3:
        pass

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter a valid number.")