# class Bar:
#     name = "kmj"

#     def __init__(self):
#         self.age = 20
        
#     def hello(self):
#         print(self.name)



# obj = Bar()
# obj.hello()

# class Bar:
#     category = "animal"

#     def __init__(self, name):
#         self.name = name
    
#     def hello(self):
#         print("Hello,", self.name)


# obj1 = Bar("dog")
# obj2 = Bar("cat")

# class Foo:
#     univ = "YJU"
    
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
        
#     def prt_info(self):
#         self.age = 20
#         print(self.id, self.name, self.age)
        
# obj = Foo()
# obj.prt_info()
# class Foo:
#     univ = "YJU"
#     dept = "GSC"
    
#     def __init__(self, name):
#         self.name = name
        
#     def prt_info(self, age):
#         self.age = age
#         print(self.name, self.age)
        
# obj1 = Foo("kim")
# obj1.prt_info(20)
# obj2 = Foo("Hong")
# obj2.prt_info(30)

class bar:
    univ = "YJU"
    dept = "GSC"
    
    def __init__(self, name):
        self.name = name
        
    def prt_info(self, age):
        self.age = age
        print(self.name, self.age)
        
obj1 = bar("kim")
obj1.prt_info(20)
obj2 = bar("Hong")
obj2.prt_info(30)