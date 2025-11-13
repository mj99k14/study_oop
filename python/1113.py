from typing import Any,Self

# class Bar:
#     def __init__(self,name:str) ->None:
#         self.name:str = name
        
#     @property
#     def name(self):
#         return self._name +"안녕하세요"
    
#     @name.setter
#     def name(self,value:str):
#         self._name:str = value
    

# obj = Bar("yc jung")
# print(obj.name) 


#python  -> function -> first-class citizen

#nested function
def out_func():
    name = "out_func"
    def in_func(id:int): #nested function
        print("in_func:id ->{id} at {name}")
        
        
    return in_func

my_func_1 = out_func()

#     print("out_func")
#     in_func()
# out_func()

my_func_1(1)
my_func_1(2)

#python  -> function -> first-class citizen
def login(func):
    def warpper():
        print("befor login")
        func()
        print("after login")
    return warpper


@login # 인터프린터가 코드 해석 시 해당 함수(매서드) 호출한다
#bar = login(bar)
def bar():
    print("bar")
    
bar()
bar()

# @login 
# def foo():
#     print("foo")
    
# @login
# def pos():
#     print("foo")