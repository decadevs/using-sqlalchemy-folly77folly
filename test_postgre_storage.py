import unittest
from storage.postgres_storage import Postgres

class TestPostgre(unittest.TestCase):

    def setUp(self):
        self.book = Postgres()

    def test_create_book(self):
        result1 = self.book.create(id = 1, title = 'Python Introduction', author = 'Aka')
        result2 = self.book.create(id = 10001, title = 'Akeem is pissed', author = 'Abdulfatai')
        
        self.assertEqual(result1, 'id already exists')
        self.assertEqual(result2, 'insert record sucessful')

    def test_fetch(self):
        result = self.book.fetch(id = 1)
        self.assertDictEqual(result[0] , {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})
      

    def test_fetch_all(self):
        result = self.book.fetch_all()
        self.assertDictEqual(result[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})
        
    def test_delete(self):
        result = self.book.delete(id = 10001)
        self.assertEqual (result, 'delete successful')
    


if __name__ == '__main__':
    unittest.main()