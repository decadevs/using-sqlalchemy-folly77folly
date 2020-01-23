from sqlalchemy import create_engine
from reader_storage import Storage

db = create_engine('postgresql://postgres:pass@localhost/all_books')
# ('postgresql+psycopg2://postgresql:pass@localhost:5432/all_books')

db.execute("CREATE TABLE IF NOT EXISTS books (id text, title text, author text)")  

class Postgres(Storage):


    book_counter = 0

    def __init__(self):
        self.book_record = []


    
    def create(self,**kwargs):

        # self.record['id'] = kwargs['id']
        # self.record['title'] = kwargs['title']
        # self.record['author'] = kwargs['author']
        # InMemory.book_counter += 1
        ids=kwargs['id']
        t=kwargs['title']
        a=kwargs['author']
        db.execute(f"INSERT INTO books (id, title, author) VALUES ('{kwargs['id']}', '{kwargs['title']}', '{kwargs['author']}')")
    
    def fetch(self, **kwargs):

        if  'id' in kwargs :
            result = db.execute(f"SELECT * FROM books where id = '{kwargs['id']}' ")
            if result:
                return [book for book in result]
            return 'No Record Found'

        if  'title' in kwargs :
            result = db.execute(f"SELECT * FROM books where title = '{kwargs['title']}' ")
            if result:
                for book in result:
                    self.book_record.append(book)
                return self.book_record

        if  'author' in kwargs :
            result = db.execute(f"SELECT * FROM books where author = '{kwargs['author']}' ")
            if result:
                for book in result:
                    self.book_record.append(book)
                return self.book_record


    def delete(self, **kwargs):

        if  'id' in kwargs:
            result = db.execute(f"DELETE FROM books where id = '{kwargs['ID']}' ")
            return 'delete successful'


        if  'author' in kwargs:
            result = db.execute(f"DELETE FROM books where author = '{kwargs['author']}' ")
            return 'delete successful'

        if  'title' and  'author' in kwargs:
            result = db.execute(f"DELETE FROM books where title = '{kwargs['title']}' and author = '{kwargs['author']}'")
            return 'delete successful'


    def fetch_all(self):
        result = db.execute(f"SELECT * FROM books where author = '{kwargs['author']}' ")
        if result :
            return [book for book in result]             


# print(add_up(1,2))
a=Postgres()
# b=InMemory()
# print(a.create(id=4,title='sola',author='sdkjhsjhfjsdhfksdhfsdfksdhfsdjfskh'))
# print(a.create(id=1,title='sola',author='kemi'))
# print(a.fetch(id=1))
print(a.delete(author='Aka',title ='Python Introduction'))

