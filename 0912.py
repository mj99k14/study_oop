# class Bar:
#     #.instance method
#     def i_method(self):
#         self.iValue = 20
    
    
#     #class method    
#     def c_method(cls):
#         cls.cValue = 30
        
# # obj = Bar()
# # Bar.i_method(obj)
# # print(obj.iValue)

# class Bar:
#     # instance method
#     def i_method(self):
#         self.iValue = 20
        
#     # class method
#     @classmethod
#     def c_method(cls):
#         cls.cValue = 30

# obj = Bar()
# obj.i_method()
# obj.c_method()
# del obj.iValue
# del Bar.cValue
# del Bar.i_method
# Bar.cValue = 1000


class Bars:
    
    # Constructor
    def __init__(self, id):
        # Add instance member variables 
        self.id = id
        print(f"Constructor of object {self.id} is invoked")
        
    def __del__(self):
        print(f"Destructor of object {self.id} is invoked")
    
obj1 = Bars(1)
obj2 = Bars(2)
del obj1
print("Program is terminated")
del obj2