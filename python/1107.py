from typing import Any, Self
from dataclasses import dataclass

# class Bar:
#     def __init__(self) ->None:
#         self.name ="Bar" #name:name, value:Bar
        
#     # event -> 객체 맴버 변수에 값을 넣을떄
#     def __setattr__(self,name: str, value: Any) ->None:
#         object.__setattr__(self, name:str, value: Any) -> None:
#         print({name},{value})
    
#     def __getattribute__(self,name str) -> Any:
#         try:
#             value = object.__getattribute__(self,name)
#             print({value})
#             return value
#         except AttributeError:
#             print({name})
#         print(f"Get: {name}")
        
        
    
    
# obj = Bar()
# #obj.bar ?존재하지 않는다

# obj.bar = 3   #name: bar, value:3

# #obj.bar ?존재하지 않는다
# print(obj.tag) #no attribute

# import random
# from collections import OrderedDict
# class Module:
#     _parameters:OrderedDict
#     def __init__(self,input:int, output:int) -> None:
#         object.__setattr__(self, "_parameters", OrderedDict)
        
#         self.weight = [random.gauss(0,1) for _ in range(input)]
#         self.bias = [random.gauss(0,1) for _ in range(output)]
        
#     def __setattr__(self,name: str, value: Any) ->None:
#         #name -> weight or bias -> ordereddic에 저장
#         #이외는 그냥 저장 
#         if name in ["weight", "bias"]:
#             self._parameters[name] = value
#         object.__setattr__(self, name, value)   
        
#     def __getattribute__(self, name:str) ->Any:
#         if name in["weight","bias"]:
#                    return self._parameters[name]
               
#         return self.name
    
#     def paramters(self):
#         yield from self._parameters.items()
        
                       
# module = Module(3, 1)

# for w,b in module.paramters():
#     print(w, b)

# class Cal:
#     def __enter__(self) ->Self:
#         print("Bar: enter")
#         return self

#     def div(self, x, y) ->float:
#         return x/y
    
#     def __exit__(self, exc_type, exc_value, traceback)->bool:
#         print("exit: type[{exec_type}],val:[{exec_value}],\
#             trace:[{traceback}]")
#         return False

# with Cal() as obj:
#     obj.div(2,2 )



# @dataclass(order=True)
# class Student: #data 저장용 클래스가 된다
    
#     id:str #인스턴스 맴버 변수
#     name:field(compare = False, repr=False ) #인스턴스 맴버 변수
#     age:int#인스턴스 맴버 변수
    
#     data:list = field(default_factory=list)
    
#     def __eq__(self,value:"Student") -> bool:
#         return self.id == value.id
    
#     def __le__(self,value:"Student") -> bool:
#         return self.age <= value.age
    
# std1 = Student("123","kim",23)
# std2 = Student("234","lee",34)

# print(std1)

# print(std2.name,std2.age,std2.id)


# def decorator(func):
#     print("decorator")

# @decorator
# def test():
#     print("test")


def bar(func):
    def wrapper(msg:str):
        print("write log")
        func(msg)
    return wrapper
@bar
def test(msg:str): #test = bar(test)
    print("msg")
test("hello")
print(test.__name__)