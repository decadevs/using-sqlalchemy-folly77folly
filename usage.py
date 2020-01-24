from storage.postgres_storage import Postgres
from storage.in_memory_storage import InMemory



in_memory_storage = InMemory()

# books_manager = in_memory_storage
books_manager = Postgres()

book = books_manager.create(id=101,author="Aka",title="Python Introduction")
books_manager.fetch_all

# class BooksManager(storage):
#     pass
# print(add_up(1,2))
# a=InMemory()
# b=InMemory()
# print(a.create(id=4,title='sola',author='sdkjhsjhfjsdhfksdhfsdfksdhfsdjfskh'))
# print(b.create(id=1,title='sola',author='kemi'))
# print(a.delete(author='Aka',title ='Python Introduction'))