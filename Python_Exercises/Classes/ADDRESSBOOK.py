#!/usr/bin/env python

class AddressBook(object):
    def get_book(self, path):
        book = dict()
        with open(path, 'w+r') as f:
            for info in f.readlines():
                info = info.split()
                book[info[0]] = info[1]
        return book

    def add(self, name, addr):
        with open(self.path, 'a') as f:
            f.write('%s,%s\n' %(name,addr))
        self.book[name] = addr
        
    def email(self, name):
        return self.book[name]


    def __init__(self, path):
        self.path = path
        self.book = self.get_book(path)

    def __getitem__(self, name):
        return self.book[name]



def main():
            ab = AddressBook('contacts.txt')
	    ab.add('Eve', 'eve@gmail.com')
	    ab.add('Alice', 'alice@walla.co.il')

	    print(ab['Eve'])



if __name__ == '__main__':
    main()



