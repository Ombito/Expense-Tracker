from sqlalchemy import Column, Integer, String, create_engine, Date, Float, func, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///my_database.db")

expense_category = Table(
    'expense_category', 
    Base.metadata,
    Column('expense_id', Integer, ForeignKey('expenses.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

# Create expenses table
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    date = Column(Date, server_default=func.now())
    category = Column(String())
    description = Column(String())
    amount = Column(Float())

    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    user = relationship('User', back_populates='expenses')
    categories = relationship('Category', secondary=expense_category)

    def __repr__(self):
        return f"Expense: {self.amount}"

# Create a user table
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String()) 
    email = Column(String())

    expenses = relationship('Expense', back_populates='user')

# Create a category table
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())

    expenses = relationship('Expense', secondary='expense_category')

def seed_initial_data():
    # Create some initial users
    user1 = User(username='alvin', email='alvin@gmail.com', password='password') 
    user2 = User(username='grace', email='grace@gmail.com', password='password')  

    
    session.add_all([user1, user2])
    session.commit()


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

seed_initial_data()
