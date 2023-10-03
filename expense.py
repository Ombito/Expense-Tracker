from sqlalchemy import Column, Integer, String, create_engine, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base
engine = create_engine("sqlite:///my_database.db")

    #create expenses table
class Transaction(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, server_default=func.now())
    category = Column(String())
    amount = Column(Integer())
    description = Column(String())

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = sessionmaker()(bind=engine)
    session.commit()