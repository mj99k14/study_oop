class Book:
    count = 0;
    
    def __init__(self,title,author,price,stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        Book.count += 1
    
    def sell(self,amount):
        self.amount = amount
    
        if( self.stock < self.amount ):
            print("재고 부족")
            return
        self.stock -= amount
        
    def add(self,amount):
        self.stock +=amount
        
    def  get_info(self):
        print(f"제목:{self.title},저자:{self.author},가격:{self.price},재고:{self.stock }")
        
              
        
b1 = Book("파이썬입문","김민정","20000","8")
b1.get_info()