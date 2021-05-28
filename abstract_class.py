# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:03:42 2021

@author: admin
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self): pass

class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price = price
    
    def display(self):
        print(f'Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}')        

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
