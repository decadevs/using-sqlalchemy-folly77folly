from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class AllBooks(base):
    __tablename__ = 'allbooks'

    ids = Column(String, primary_key=True)
    title = Column(String)
    author = Column(String)