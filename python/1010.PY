# # 추상화 (Abstract) -> OOP
# # 미완성 + 강제 구현

# from abc import ABC, abstractmethod

# # ABC -> ABstract Class
# class Bar(ABC):
#     @property # Getter
#     @abstractmethod
#     def test():
#         pass
    
#     @test.setter # Setter
#     @abstractmethod
#     def _(self, value):
#         ...
    
# class Foo(Bar):
#     @property # 부모의 데코레이터와 같아야 한다.
#     def test():
#         …


# obj = Foo() # -> Error


# class Bar:
#     #반드시 자식 클래스에서 구현되기를 바란다
#     def test(self):
#         raise NotImplementedError
# class Foo(Bar):
#     ...
    
# obj = Foo()
# obj.test()


# 동적 타이핑언어가 좋긴하지만 코드의 규모가 커질수록 관리의어려움이있다

from typing import Union


def sum(a : Union[int,float],b : Union[int ,float]) ->  int | float:
    return a / b 




print(sum(1,1))
print(sum(1,1.0))
print(sum("1","1")) # ->error


