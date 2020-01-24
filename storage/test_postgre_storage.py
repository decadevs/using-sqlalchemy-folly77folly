import unittest
from postgres_storage import Postgres

class TestPostgre(unittest.TestCase):

    def setUp(self):
        self.book = Postgres()

    def test_create_book(self):
        result = self.book.create(id = 1,title ='Python Introduction',author = 'Aka')
        self.assertDictEqual(result[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})

    def test_fetch(self):
        result = self.book.fetch(id = 1)
        self.assertDictEqual(result , {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})
        result2 = self.book.fetch(author = 'Aka')
        self.assertDictEqual(result2 , {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})        

    def test_fetch_all(self):
        result = self.book.fetch_all()
        self.assertDictEqual(result[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})
        
    def test_delete(self):
        result = self.book.delete(id = 1)
        self.assertListEqual (result, [])    
    


if __name__ == '__main__':
    unittest.main()