#!/usr/bin/env python

class AddressBook(object):
    def add(self, **L):
        self.book.append(L)
    
    def find_by(self, **L):
        book = self.book
        for d in book:
            flag = 0
            for k, v in L.items():
                if not d[k] == v:
                    flag = 1
                    break
            if flag == 0:
                print(d)

    def __init__(self):
        self.book = list(dict())


c = AddressBook()

c.add(name='ynon', email='ynon@ynonperek.com', likes='red')
c.add(name='bob', email='bob@gmail.com', likes='blue')
c.add(name='ynon', email='ynon@gmail.com', likes='blue')

c.find_by(name='ynon')
# returns:
# [
#   {'name': 'ynon', 'email': 'ynon@ynonperek.com', 'likes': 'red'},
#   {'name': 'ynon', 'email': 'ynon@gmail.com', 'likes': 'blue}
# ]

c.find_by(likes='blue')
# returns:
# [
#   { 'name': 'bob', 'email': 'bob@gmail.com', 'likes': 'blue' },
#   {'name': 'ynon', 'email': 'ynon@gmail.com', 'likes': 'blue}
# ]



