from sqlalchemy import Column, Integer, String, create_engine, Date, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base
engine = create_engine("sqlite:///my_database.db")

    #create expenses table
class Transaction(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    date = Column(Date, server_default=func.now())
    category = Column(String())
    description = Column(String())
    amount = Column(Float())
    

    def __repr__(self):
        return f"Expense: {self.amount}"
    
class User(Base):
    __table__name__ = "users"

    id = Column(Integer(), primary_key = True)
    username = Column(String())
    email = Column(String())


class Category(Base):
    __table__name__ = "categories"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    description = Column(String())
    


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)
    session.commit()