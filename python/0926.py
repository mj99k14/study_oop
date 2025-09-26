# class A:
#     def __init__(self):
#         self.__age = 20

#     def prt(self):
#         print(self.__age)


# obj = A()
# obj._A_age = 100
# obj.prt()
# print(obj.__age)


# naming of a variable
# public -> bar
# protected -> _bar
# private -> __bar (name mangling)

# Getter / Setter -> Method

# class A:
#     def __init__(self):
#         self.__age = 20

#     def get_age(self):
#         return self.age
        
#     def set_age(self, age):
#         if age < 0:
#             raise TypeError("음수 값 오류")
#         self.age = age


# obj = A()
# obj._A__age = 100 # 막기는 막는게 맞는데 강제적인 것같은거는 막지 못한다.


# naming of a variable
# public -> bar
# protected -> _bar
# private -> __bar (name mangling)

# Getter / Setter -> Method

class A:
    def __init__(self):
        self.__age = None

    # getter method
    @property
    def age(self):
        return self.__age
        
    # setter method
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("음수 값 오류")
        self.__age = age


obj = A()
obj._A__age = 100 # 막기는 막는게 맞는데 강제적인 것같은거는 막지 못한다.