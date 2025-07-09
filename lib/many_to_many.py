class Author:
    all = []
    def __init__(self,name):
        self.name = name
       
class Book:
    all = []
    def __init__(self,title):
        self.title = title


class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        self.author = author #instance of Author class
        self.book = book #instance of Book class
        self.date = date #string
        self.royalties = royalties #integer

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book 
    @book.setter
    def book(self,value):
        if not isinstance(value,Book):
            raise Exception
        self._book = value