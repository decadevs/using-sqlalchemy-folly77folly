from abc import ABC, abstractmethod


class Storage(ABC):
    
    def __init__(self,*kwargs):
        self.id = bookid
        self.booktitle = booktitle
        self.bookauthor = bookauthor

    @abstractmethod
    def create(self, **kwargs):
        pass
    
    @abstractmethod
    def fetch(self, **kwargs):
        pass
    
    @abstractmethod
    def delete(self, **kwargs):
        pass

    @abstractmethod
    def fetch_all(self):
        pass

