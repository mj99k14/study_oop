# def test():...

# #bar 변수에 test함수 주소값을 할당
# bar = test


# bar()

# def run(my_Func): 
#     my_Func()
    
# #test 함수를 run 함수의 매개변수에 할당 
# run(test)\
    
    
#Callable
# def test(x:int,y:float,z:str) ->str:
#     return f"{x},{y},{z}"

# from typing import Callable

# # my_func -> argument ->3개 반환형은 문자열
# # callabe[매개변수 자료형, 반환값 자료형]
# # callabe[[매개변수 ,자료형, 매개변수2 자료형] 반환값 자료형]
# # def run(my_func,a:int,b:float,c:str) ->None:
# def run(my_func:Callable[[int,float,str],str], a:int,b:float,c:str):
#     print(my_func(a,b,c))
    
# run(test)

# def test2(x,y):
#     ...
    
# run(test2)



# x = {"name":"ycjung", "age":20, "gender":"M"}


#TypedDic -> 스키마 정의 ->dictionary -> json

# from typing import TypedDict

# class User(TypedDict):
#     name:str
#     age:int
#     gender:str
    


# x:User = {"name":"ycjung", "age": 20,"gender":"M"}
# x = {"name":"ycjung", "age": 20,"gender":"M"}

# from typing import NamedTuple

# class User(NamedTuple):
#     name:str
#     age:int
#     gender:str
    
# u1 = User("ycjund",2,"M")

# print(u1.name,u1.age,u1.gender)

# def create_user(name:str,age:int,gender:str) ->User:
#     return User(name,age,gender)

# name, age , gender = create_user("ycjung" , 2 ,"m")

# print(1+1)
# print((1).__add__(1)) # 매소드안에()에 숫자가들어감


class Vector:
    def __init__(self,x:int, y:int) -> None:
        self.x:int = x
        self.y:int = y
        
    def __add__(self,r_operand:"Vector"):
        x = self.x + r_operand.x
        y = self.y + r_operand.y

        return Vector(x,y)        
v1 = Vector(1,2)
v2 = Vector(3,4)

v3 = v1 + v2
#v1.__Add__(v2)

v4 = v1 + v2


# x3 = v1.x + v2.x
# y3 = v1.y + v2.y

# v3 = Vector(x3,y3)

