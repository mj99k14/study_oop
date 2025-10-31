

# class  Bar:
#     def __str__(self)->str:
#         return f"Bar"
    

# obj = Bar()

# print(obj)


# obj2 = object()
# print(obj2.__str__())

# print(obj.__str__())


# from typing import Any


# class Student:
#     def __init__(self, id:int) -> None: #반환하면 안된다
#         self.id:int = id
#         self.kor:int = 0
#         self.eng:int = 0
#         self.math:int = 0

#     def __call__(self, kor:int, eng:int, math:int):
#         self.kor = kor
#         self.eng = eng
#         self.math = math

#     def __str__(self):
#         return f"kor: {self.kor}, eng: {self.eng}, math: {self.math}"

#     # 이 함수는 == 연산자가 호출되면 자동으로 실행되는 매직 메서드이다.
#     def __eq__(self, value: "Studnet") -> bool: 
#         return self.id == value.id


# obj = Student(1)
# obj(10, 20, 30)

# print(obj)



# #Iteration: 순회
# x = [_for _in range(10)]
# for v in x:
#     print(v)


# class  Bar:
#     def __init__(self,data:Sequence[int]) ->None:
#         self.data:Sequence = data
        
#     def __len___(self)->int:
#         return len(self.data)

# obj = Bar([1,2,3,4])
# print(len(obj))


# Iteration : 순회

# Iteration : 순회

from typing import Sequence

class Bar:
    def __init__(self, data:Sequence[int]) -> None:
        self.data:Sequence = data

    def __iter__(self): # 이게 구현되어 있어야 순회가 가능함.
        return BarIterator(self.data)

    
class BarIterator:
    def __init__(self, data:Sequence) -> None:
        self.data:Sequence = data
        self.index:int = 0

    def __next__(self)->int:
        # self.data 리스트의 0번쨰 요소에서 마지막 요소까지 순회
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        
        raise StopIteration
    
obj = Bar([1, 2, 3, 4])

for v in obj: # -> instance of Bar
    print(v) # 1, 2, 3, 4


# 이거는 인덱스가 초기화가 안돼서 다 돌았다고 판단해 출력물이 없다.
for v in obj: # -> instance of Bar
    print(v) # 1, 2, 3, 4

# x = [10, 20, 30]

# foo = iter(x)
# while True:
#     try:
#         print(next(foo)) # 현재값을 출력하고 다음 값으로 shift 하는 역할
#     except StopIteration: # 내부의 값들을 전부 다 돌았다면 StopIteration이라는 예외를 발생하고 정지
#         break