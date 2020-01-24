from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from reader_storage import Storage


db = create_engine('postgresql://postgres:pass@localhost/all_books')
Base = declarative_base()

class MyBook(Base):
    __tablename__ = 'allmybooks'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    title = Column(String)

#creating a session/connection with engine
Session = sessionmaker(db)  
session = Session()

# Base.metadata.create_all(db)

class Postgres(Storage):
    book_counter = 0

    def __init__(self):
        self.book_record = []
        self.book = {}
        self.id = None
        self.title = None
        self.author = None
        self.connection = db.connect()
        Base.metadata.create_all(db)
   

    def create(self, **kwargs):
        self.id=kwargs['id']
        self.title=kwargs['title']
        self.author=kwargs['author']
        result = session.query(MyBook).filter(MyBook.id == self.id)
        for row in result:
            if row.id:
                print(row.id)
                return 'id already exists'
        abook= MyBook(id=self.id, title = self.title, author = self.author)  
        session.add(abook)  
        session.commit()
        return self.fetch(id = self.id)
        # return 'record inserted'
        
    

    def fetch(self, **kwargs):

        if  'id' in kwargs and len(kwargs) == 1 :
            self.id = kwargs['id']
            result = session.query(MyBook).filter_by(id = self.id)
            if result:
                for book in result:
                    self.book['id'] = book.id
                    self.book['title'] = book.title
                    self.book['author'] = book.author
                    self.book_record.append(self.book)
                return self.book_record
            return 'No Record Found'


        if  'title' in kwargs and len(kwargs) == 1 :
            self.title = kwargs['title']
            result = session.query(MyBook).filter_by(title = self.title)
            if result:
                for book in result:
                    self.book['id'] = book.id
                    self.book['title'] = book.title
                    self.book['author'] = book.author
                    self.book_record.append(self.book)
                return self.book_record
            return 'No Record Found'            


        if  'author' in kwargs and len(kwargs) == 1:
            self.author = kwargs['author']
            result = session.query(MyBook).filter_by(author = self.author)
            if result:
                for book in result:
                    self.book['id'] = book.id
                    self.book['title'] = book.title
                    self.book['author'] = book.author
                    self.book_record.append(self.book)
                return self.book_record
            return 'No Record Found' 


    def delete(self, **kwargs):

        if  'id' in kwargs and len(kwargs) == 1:
            self.id = kwargs['id']
            for book in session.query(MyBook).filter_by(id = self.id):
                session.delete(book)
                session.commit()
                return self.fetch(id = self.id)      
            return 'no record found'


        if  'author' in kwargs and len(kwargs) == 1:
            self.author = kwargs['author']
            for book in session.query(MyBook).filter_by(author = self.author):
                session.delete(book)
                session.commit()
                return 'delete successful'                
            return 'no record found'

        if  'title' and  'author' in kwargs  and len(kwargs) == 2:
            self.title = kwargs['title']
            self.author = kwargs['author']
            for book in session.query(MyBook).filter_by(author = self.author).filter_by(title = self.title):
                session.delete(book)
                session.commit()
                return 'delete successful'                
            return 'no record found'


    def fetch_all(self):
        books = session.query(MyBook).all()
        for book in books :
            self.book['id'] = book.id
            self.book['author'] = book.author
            self.book['title'] = book.title
            self.book_record.append(self.book)
        return self.book_record
           


# print(add_up(1,2))
# a=Postgres()
# b=InMemory()
# print(a.create(id=8,author='Aka', title='Python Introduction'))
# print(a.create(id=29,author='sola',title='The begining of snake'))
# print(a.fetch(id='1'))
# print(a.delete(id='1'))
# print(a.delete(author='Aka',title ='Python Introduction'))
# print(a.fetch_all())

