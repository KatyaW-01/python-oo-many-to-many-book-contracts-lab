class Author:
    all = []
    def __init__(self,name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        related_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                related_contracts.append(contract)
        return related_contracts


    def books(self):
        related_books = []
        for contract in Contract.all:
            if contract.author == self:
                related_books.append(contract.book)
        return list(set(related_books))

    def sign_contracts(self,book,date,royalties):
        pass

    def total_royalties(self):
        total_royalties = 0
        for contract in Contract.all:
            if contract.author == self:
                total_royalties += contract.royalties
        return total_royalties
       
class Book:
    all = []
    def __init__(self,title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        related_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                related_contracts.append(contract)
        return related_contracts

    def authors(self):
        related_authors = []
        for contract in Contract.all:
            if contract.book == self:
                related_authors.append(contract.author)
        return list(set(related_authors))
        #removes duplicates but still keeps it a list


class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        self.author = author 
        self.book = book 
        self.date = date 
        self.royalties = royalties 
        Contract.all.append(self)

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

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,value):
        if not isinstance(value,str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,value):
        if not isinstance(value,int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls):
        pass
    