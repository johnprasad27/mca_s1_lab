class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)    

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        print(self.name,self.title,self.author) 

class Python(Book):
    def __init__(self,name,title,author,no_of_pages,price):
        super().__init__(name,title,author)
        self.no_of_pages=no_of_pages
        self.price=price
    def display(self):
        print(self.name,self.title,self.author,self.no_of_pages,self.price)

b1=Book("john","new","mikael")
b1.display()

p1=Python("basil","old","new author",99,100)
p1.display()