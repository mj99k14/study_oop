# class A:
#     def __init__(self):
#         name = "Test"
#         self.name = "Class A"

#     @classmethod
#     def prt_something(cls):
#         print("Invoked prt_something")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.age = 20

# obj = A()
# A.prt_something()





# class A:
#     def __init__(self):
#         name = "Test"
#         self.name = "Class A"

#     @classmethod
#     def prt_something(cls):
#         print("Invoked prt_something")

# class B(A):
#     def __init__(self):
#         self.age = 20

# class C(B):
#     def __init__(self):
#         self.nick = "Class C"  

# obj = C()

# print(obj.nick) # class C
# print(obj.age)
# print(obj.name)



class A: 
    def __init__(self): # -> private X
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

obj = A()
print(obj.public) # public
# print(obj._protected) # protectd
# print(obj.__private) # Error
print(obj.A__private)