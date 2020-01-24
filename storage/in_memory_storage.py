from storage.reader_storage import Storage

class InMemory(Storage):

    all_books = [{'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'} ]

    book_counter = 0

    def __init__(self):
        self.id = None
        self.booktitle = None
        self.record = {}
        self.book_record = []

    
    def create(self,**kwargs):

        self.record['id'] = kwargs['id']
        self.record['title'] = kwargs['title']
        self.record['author'] = kwargs['author']
        InMemory.book_counter += 1
        InMemory.all_books.append(self.record)
        return InMemory.all_books
    
    def fetch(self, **kwargs):

        if  'id' in kwargs and len(kwargs) == 1:
            self.book_record = [book for book in InMemory.all_books if kwargs['id'] == book['id']]
            return self.book_record

        if  'title' in kwargs and len(kwargs) == 1:
            self.book_record = [book for book in InMemory.all_books if kwargs['title'] == book['title']]
            return self.book_record

        if  'author' in kwargs and len(kwargs) == 1:
            self.book_record = [book for book in InMemory.all_books if kwargs['author'] == book['author']]
            return self.book_record



    def delete(self, **kwargs):

        if  'id' in kwargs and len(kwargs) == 1:
            self.book_record = [(count, book) for count, book in enumerate(InMemory.all_books) if kwargs['id'] == book['id']]
            InMemory.all_books.pop(self.book_record[0][0])
            return InMemory.all_books
            

        if  'author' in kwargs and len(kwargs) == 1:
            self.book_record = [(count, book) for count, book in enumerate(InMemory.all_books) if kwargs['author'] == book['author']]
            InMemory.all_books.pop(self.book_record[0][0])
            return InMemory.all_books

        if  'title' and  'author' in kwargs and len(kwargs) == 2:
            self.book_record = [(count, book) for count, book in enumerate(InMemory.all_books) if kwargs['title'] == book['title'] and kwargs['author'] == book['author']]
            InMemory.all_books.pop(self.book_record[0][0])
            return InMemory.all_books

    def fetch_all(self):
        return InMemory.all_books
