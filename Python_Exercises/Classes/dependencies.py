#!/usr/bin/env python

class Widget(object):
    def __init__(self, name, dependency = None, isbuilt = False):
        self.name = name
        self.dependency = dependency
        if self.dependency is None:
            self.dependency = []
        self.isbuilt = isbuilt

    def add_dependency(self, *L):
        for d in L:
            self.dependency.append(d)

    def build(self):
        for d in set(self.dependency):
            if(d.isbuilt == False):
                d.build()
                print(d.name)
                d.isbuilt = True
    


def main():

	luke    = Widget("Luke")
	hansolo = Widget("Han Solo")
	leia    = Widget("Leia")
	yoda    = Widget("Yoda")
	padme   = Widget("Padme Amidala")
	anakin  = Widget("Anakin Skywalker")
	obi     = Widget("Obi-Wan")
	darth   = Widget("Darth Vader")
	_all    = Widget("All")


	luke.add_dependency(hansolo, leia, yoda)
	leia.add_dependency(padme, anakin)
	obi.add_dependency(yoda)
	darth.add_dependency(anakin)

	_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
	_all.build()

if __name__ == "__main__":
    main()
