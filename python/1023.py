# # x: int = 1

# # def test(x1: float, x2: int) -> float:
 
 
# class bar:


#     def __init__(self,name: str,age:int) ->None:
#         self.name:str = name
#         self.age:int = age


# from typing import Any


# # x: int | float| str| Any = 1 # 이럴경우 Any만 쓰던지 아니면 int | float| str쓰셈


# from typing import Union

# y: Union[int, float ] = 1


# #collection -> expression, type of the elements in a collection
# #list , tuple,set,dict

# x:list =[1,2,3,4]

# x =[2.0]

# c:dict[str,str] = {"name": "ycjung"}
# y :tuple [int,int,int ...]= (1,2,3,4)


# from typing import Optional, Union
# X:Optional[float] = 2

# # def add_user(name:str) ->Union[str,None]:
# #     ...
    
# def add_user(name:Optional[str]) ->Optional[str]:
#     ...
    
    
    
    
    

# def test(): ...


# a= test

# a()

# def run(func):
#     return func


# run(test)