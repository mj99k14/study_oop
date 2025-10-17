
# x:int = 2

# y:float = 3.0

# y ="2"
# y = 2

# z:str =" 2"
# z =10

# a:bool = True

# a ="True"

# b: bytes =b "test"


# def sum(x:int, y:int) -> int:
#     return x + y

# class Bar:
#     def __init__(self,x:int, y: str) ->None:
#         self.x:int = x
#         self.y:str = y

# from typing import List
# y:List = [1,2,3,4] #legacy


# x:list = [1, 2, 3]
# x =(1, 2, 3)

# x ={1, 2, 3}
# x ={1:2, 3:4, 5:6}

# def get_total_Avg(x:int, y:int) ->tuple:
#     sum = x+ y
#     avg = sum/2
#     return sum, avg

# x_tuple:tuple =(1,2,3)
# x_tuple = [1,2,3]
# x_dict:dict = {1:2, 3:4}

# x_set:set = {1,2,3}

# x_range:range = range(2)

# x_list:list = [1, 2.0, "3"]

# x_list_int:list[int| float] = [1,2,3]
# x_list_int = ["2",3,4.0]

# x_list_int:list[int | float | str] = [1, 2, 3]
# x_list_int = ["2", 3, 4.0]

# # Tuple은 자리수(순서, 개수, 자료형)까지 다 맞게 Type Hinting을 해줘야한다.
# x_tuple_int:tuple[int, float, str, int] = (2, 3.0, "4", 3)

# y:tuple[int, ...]
# y = (1, 2, 3)
# y = (2, 3, 4, 5, 6)

# x_dict_str_float:dict[str,float] = {"k1":2.0,"k2":3.0}
# x_dict_str_float ={1:2.0}
# x_set_bool:set[bool] = {True,False}

#Union -> 집합의 원소중 하나이면  ->ok
#모두 해당되지않으면 ->Error

# from typing import  Union
# x: Union[int, float, bool]
# x_new:int | float | bool

# x = 2
# x = 3.0
# x = False
# x = "2"


# #optional -> if else -> if[T] else None
# from typing import Optional

# x_op_int:Optional[int]

# x_op_int = 3
# x_op_int = None
# x_op_int = "4"


# from typing import Any

# x:Any
# x =1
# x=2.0
# x ="d"


#Callanle -> 함수, 매서드 
from typing import Callable
def sum(x:float, y:float) ->float:
    return x +y
def do_something(x:float,y:float,op:Callable[[float,float],float]):
    return op(x,y)

do_something(1,2,sum)