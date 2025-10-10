# 추상화 (Abstract) -> OOP
# 미완성 + 강제 구현

from abc import ABC, abstractmethod

# ABC -> ABstract Class
class Bar(ABC):
    @property # Getter
    @abstractmethod
    def test():
        pass
    
    @test.setter # Setter
    @abstractmethod
    def _(self, value):
        ...
    
class Foo(Bar):
    @property # 부모의 데코레이터와 같아야 한다.
    def test():
        …


obj = Foo() # -> Error