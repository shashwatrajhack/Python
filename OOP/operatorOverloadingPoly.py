# how to achieve operator overloading

class Book:
    def __init__(self,pages,title):
        self.pages = pages
        self.title = title

    def __add__(self,other):   #b1+b2
        total = self.pages+other.pages
        return Book(title="All books",pages=total)
    
    def __str__(self):
        return str(self.pages)

b1 = Book(200,"One Indian Girl")
b2 = Book(300,"Alchemist")
b3 = Book(800,"Sapiens")
b4 = Book(100,"Attitude is Everything")

# print("No. of pages : ",b1.pages+b2.pages);

# how to achieve this so here comes the role of operator overloading where we will define the operator according to the need;
print("No. of pages : ",b1+b2+b3+b4);

