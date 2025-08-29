# class Foo:
#     #constructor #callback함수 -> 내가 만든 함수를 다른 사람이 호출
    
#     #매직 (Magic) Method -> __ 시작
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        


# obj = Foo("kmj", 27)


# class Foo:
    
#     bar = 2
#     #constructor
#     def __init__(self):
#         #!)instance MV
#         self.university ="gsc";
    
#     #member variable

#     #2)class MV
#     age = 20
#     name = "kmj"
    
    
#     #Member method
#     #1) instance MM
#     #2) class MM
    
#     #destructor

class Foo:
    x =100
    def __init__(self):
        self.x =20
        
    def text(self):
        self.y  =30    
obj = Foo()

print(obj.x)
obj.text()
print(obj.y)


class Student:
    count = 0
    
    def __init__(self):
        Student.count += 1
        self.id = Student.count
        self.name = "wonjun"
        self.korean = 100
        self.math = 100
        self.english = 100
        self.sum = self.english + self.math + self.korean