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





class A:
    def __init__(self):
        name = "Test"
        self.name = "Class A"

    @classmethod
    def prt_something(cls):
        print("Invoked prt_something")

class B(A):
    def __init__(self):
        self.age = 20

class C(B):
    def __init__(self):
        self.nick = "Class C"  

obj = C()

print(obj.nick) # class C
print(obj.age)
print(obj.name)