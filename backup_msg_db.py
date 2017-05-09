#  set up sqlite objects and import them to run.py 


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
from datetime import datetime



engine = create_engine('sqlite:///msg.db', echo=False)

Base = declarative_base()

class input_msg(Base):
    """
    A table to store data on craigslist listings.
    """

    __tablename__ = 'msg'
    
    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    msg = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()