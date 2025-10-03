# def bar(a, b, c, *args, e=10, f= 10, **kwargs):
#     pass

# def foo(a, b, c):
#     pass

# foo(1, 2) # -> Error

# def pos(a, b, c=20):
#     pass

# pos(1, 2) # -> OK


# def bar(a,b,c=100,*args):
#     print(a,b,args)


# bar(1,2,3,4,5,6)

#type hinting
x :int = 3

# def sum(a, b):
#     return (float)(a + b )


# type hinting
from typing import Union


# x : int = 3

# def div(a : Union[int, float] , b : Union[int, float]) -> float:
#     return (a / b)

# print (div(4/2))
# print(div(4.0/2.0))
# print(div("4"/"2"))



# def bar(x:int):
#     print("x")
# def bar(y:float):
#     print("y")
# def bar(z: str):
#     print("z")
# bar(3)

# from functools import singledispatch, singledispatchmethod

# # 매개변수 1개 -> 오버로딩 구현
# # 지원 자료형은 int, float

# @singledispatch
# def bar(x):
#     raise TypeError("unsupported type")

# @bar.register(float)
# def _(x : float):
#     print("float")
    
# @bar.register(int)
# def _(x : int):
#     print("int")

# bar(2.0)


from abc import ABC,abstractmethod
# 추상 클래스를 정의
#java -> abstract class Bar{}

#Bar를 추상 클래스로 정의
class Bar(ABC):
    #추상 인스턴스 매서드 정의
    @abstractmethod
    def instance_method(self):
        pass


class MyClass(Bar):
    def instance_method(self):
        print("MyClass : instance_method")

obj = MyClass()
obj = Bar()