# class Bar:
#     # 맴버 변수(속성) ->1. 인스턴스 맴버 변수 (매서드, 소멸자에서 만들 수 있음 )
#     cls_br = 100; 
#                     #  2. 클래스 맴버변수
#     #클래스 맴버 변수
#     #실무 ->여기
    
#     def __init__(self):
#         # 초기화 작업
#         #인스턴스 맴버 변수: 실무 ->여기
#         pass
#     def __del__(self):
#         # 객체 소멸 전 자원 정리
#         pass
#     # 맴버 매서드 ->1. 클래스 매서드 2. 인스턴스 매서드 (클래스 오브젝트에 올라감)

#     #인스턴스 맴버 매서드
#     def instance_method(self):
#         pass
    
#     @classmethod
#     #클래스 맴버 매서드
#     def clss_method(cls):
#         pass
    
#     #매서드 -> 맴버 매서드(인스턴스, 클래스), 스태틱(static) 매서드
    
#     #static method
#     @staticmethod
#     def static_method():
#         pass
    
# obj = Bar()


# class Parent:
#     def prt_name(self):
#         print(self.name)

# class Child(Parent):
#     def __init__(self):   # 올바른 생성자
#         self.name = "Child"

# obj = Child()
# obj.prt_name()


class Bar:
    def __init__(self):
        self.name = "YC Jung"

    def prt_info(self):
        print(self.name, self.age)

class Foo(Bar):
    def __init__(self):
        self.age = "18"
        super().__init__()


obj = Foo()
obj.prt_info()