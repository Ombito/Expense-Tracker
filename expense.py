from sqlalchemy import Column, Integer, String, create_engine, Date, Float, func, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///my_database.db")

    #association table
expense_category = Table(
    'expense_category', 
    Base.metadata,
    Column('expense_id', Integer, ForeignKey('expenses.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

    # class table
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

    # user table
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer(), primary_key=True)
    username = Column(String())
    password = Column(String()) 
    email = Column(String())

    expenses = relationship('Expense', back_populates='user')

    # category table
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())

    expenses = relationship('Expense', secondary='expense_category', overlaps="categories")

def seed_initial_data():
    
    user1 = User(username='alvin', email='alvin@gmail.com', password='password') 
    user2 = User(username='grace', email='grace@gmail.com', password='password')  
    user3 = User(username='james', email='james@gmail.com', password='password') 
    user4 = User(username='ahmed', email='ahmed@gmail.com', password='password')
    user5 = User(username='sofia', email='sofia@gmail.com', password='password') 
    user6 = User(username='diana', email='diana@gmail.com', password='password')
    user7 = User(username='felix', email='felix@gmail.com', password='password') 
    user8 = User(username='caroline', email='caroline@gmail.com', password='password')


    
    session.add_all([user1, user2, user3, user4, user5, user6, user7, user8])
    session.commit()


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

seed_initial_data()
