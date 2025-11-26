class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"publisher name",self.name)

class Book(Publisher):
      def __init__(self,name,title,author):
           super().__init__(name)
           self.publisher=self.name
           self.title=title
           self.author=author

      def display(self):
           print("book title",self.title)
           print("book author",self.author)
           print("book publisher",self.publisher)          

b1 = Book("Penguin Publications", "Python Basics", "John Doe")
b1.display()