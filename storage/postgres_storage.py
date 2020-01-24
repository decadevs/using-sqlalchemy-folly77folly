from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .reader_storage import Storage


db = create_engine('postgresql://postgres:pass@localhost/all_books')
Base = declarative_base()

class MyBook(Base):
    __tablename__ = 'allmybooks'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    title = Column(String)

# Base.metadata.create_all(db)

class Postgres(Storage):
    book_counter = 0

    def __init__(self):
        self.book_record = []
        self.book = {}
        self.id = None
        self.title = None
        self.author = None
        
        #creating a session/connection with engine
        Session = sessionmaker(db)
        self.session = Session()

        Base.metadata.create_all(db)
   

    def create(self, **kwargs):
        self.id=kwargs['id']
        self.title=kwargs['title']
        self.author=kwargs['author']
        session = self.session
    
        result = session.query(MyBook).filter(MyBook.id == self.id)


        for row in result:
            if row.id:
                return 'id already exists'

        abook= MyBook(id=self.id, title = self.title, author = self.author)  
        session.add(abook)  
        session.commit()
    
        return 'insert record sucessful'

        
    

    def fetch(self, **kwargs):
        session = self.session
        if  'id' in kwargs and len(kwargs) == 1 :
            self.id = kwargs['id']

            result = session.query(MyBook).filter_by(id = self.id)
            
            if result:
                for row in result:
                    self.book['id'] = row.id
                    self.book['title'] = row.title
                    self.book['author'] = row.author
                    self.book_record.append(self.book)
                return self.book_record

            
            return 'Something went wrong'


        if  'title' in kwargs and len(kwargs) == 1 :
            session = self.session
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
            session = self.session
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
        session = self.session
        if  'id' in kwargs and len(kwargs) == 1:
            self.id = kwargs['id']
            for book in session.query(MyBook).filter_by(id = self.id):
                session.delete(book)
                session.commit()
                return 'delete successful'     
            return 'no record found'


        if  'author' in kwargs and len(kwargs) == 1:
            session = self.session
            self.author = kwargs['author']
            for book in session.query(MyBook).filter_by(author = self.author):
                session.delete(book)
                session.commit()
                return 'delete successful'                
            return 'no record found'

        if  'title' and  'author' in kwargs  and len(kwargs) == 2:
            session = self.session
            self.title = kwargs['title']
            self.author = kwargs['author']
            for book in session.query(MyBook).filter_by(author = self.author).filter_by(title = self.title):
                session.delete(book)
                session.commit()
                return 'delete successful'                
            return 'no record found'


    def fetch_all(self):
        session = self.session
        books = session.query(MyBook).all()
        for book in books :
            self.book['id'] = book.id
            self.book['author'] = book.author
            self.book['title'] = book.title
            self.book_record.append(self.book)
        return self.book_record

