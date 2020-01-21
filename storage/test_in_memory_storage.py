import unittest
from in_memory_storage import InMemory

class TestInMemory(unittest.TestCase):

    def setUp(self):
        self.book = InMemory()

    def test_create_book(self):
        result = self.book.create(id = 1,title ='Python Introduction',author = 'Aka')
        self.assertDictEqual(result[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})

    def test_fetch(self):
        result = self.book.fetch(id=1)
        self.assertDictEqual(result[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})
        result2 = self.book.fetch(author = 'Aka')
        self.assertDictEqual(result2[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})        

    def test_delete(self):
        result = self.book.delete(id=1)
        self.assertDictEqual(result[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})

    def fetch_all(self):
        self.assertDictEqual(result[0], {'id' : 1, 'author' : 'Aka', 'title' : 'Python Introduction'})
    
    


if __name__ == '__main__':
    unittest.main()