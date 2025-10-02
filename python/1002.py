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



def bar(x:int):
    print("x")
def bar(y:float):
    print("y")
def bar(z: str):
    print("z")
bar(3)




