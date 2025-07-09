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