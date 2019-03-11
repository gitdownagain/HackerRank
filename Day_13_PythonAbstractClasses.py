# https://www.hackerrank.com/challenges/30-abstract-classes/problem
# https://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

# abc = Abstract Base Class
# https://docs.python.org/3/library/abc.html
# This module provides the metaclass ABCMeta for defining ABCs

# abstract classes aren't initialized
# you subclass them
# jump in the code and see what happens

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)   # super does not use self
        self.price = price
    
    def display(self):
       print( "Title: {}\nAuthor: {}\nPrice: {}".format(self.title,self.author,self.price) )
       # could also use keywords like title=self.title


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
