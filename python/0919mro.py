# class A:
#     def __init__(self):
#         print("A")

# class B(A):
#        def __init__(self):
#         print("B")


# class C(A):
#     def __init__(self):
#         print("C")

# class D(C,B):
#     def __init__(self):
#         print("D")
#         super().__init__()


# obj = D()


# class Parent:
#     def prt(self):
#         print("Parent")
# class Child(Parent):
#     def prt(self):
#         print("child")
    
    
# obj = Child()
# obj.prt()

    
# class A(object):
#     N
# class B(A):
#     pass

# class C(B):
#     pas


import math

def vacationRental(people, day):
    perDay = 0
    if day <= 3:
        perDay = 80
    elif day >= 10:
        perDay = 50
    else:
        perDay = 60
    
    return math.trunc((people + perDay * day) * 1.12)
