class person:
    def __init__(self,name,lname):
        self.firstname=name
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
#use the person class to create an object and then exicuite the print
x=person("cse","pfsd")
x.printname()