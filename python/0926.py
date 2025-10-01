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

# class A:
#     def __init__(self):
#         self.__age = None

#     # getter method
#     @property
#     def age(self):
#         return self.__age
        
#     # setter method
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise TypeError("음수 값 오류")
#         self.__age = age


# obj = A()
# print(obj.age)
# obj._A__age = -100 # 막기는 막는게 맞는데 강제적인 것같은거는 막지 못한다.

# def prt(a ,b = 2, c=3):
#     print(a,b,c)
    
# prt(2,3)
# prt(1)
# prt(10,20)

# /: 위치 기반 매개변수 전용 -> / 앞까지의 모든 매개변수는 위치기반 인자 값으로 할당되어야된다
# from typing import Union

# def calculate(x:Union[int, float], y:Union[int, float], /, op ="+"):
#     if op =="+":
#         print(x + y)
#     elif op =="-":
#         print(x -y)
#     else:
#         print("error")
        
# calculate(2,3)
# calculate(10,20,"-")

# def prt(**arg):
#    for key,value in arg.items():
#        print(f"{key},{value}")
    
# prt(d =3 , test ="ddd")
def prt(a, *b, c = 10 , d = 20 , **kwargs):
    print(a, b, c,d, kwargs)

prt(1, 2, 3, 4, 5 , op=200, d =100)
# a에는 1이 들어가고 b에는 2,3,4,5가 다 들어가서 c에 들어갈게 없어서 오류남
d