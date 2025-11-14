# def is_login(func):
#     # print("is login")
#     # func()
#     def wrapper(msg:str):
#         print("before")
#         func(msg)
#         print("after")
#     return wrapper

    
# @is_login #-> do_something = is_login_in
# def do_something(msg:str):
#     print("do something:{msg}")
        
# do_something("hello1")
# do_something("hello2")


# def test():
#     print("test")
    
# def bar(x, y):
#     print(f"bar:{x, y}")
    
# bar(2, 3)

# test = bar

# test(2, 3)

# def f_a(func):
#     def wrapper():
#         print(f"f_a:{func}")
#         func()
#     return wrapper
#     print("f_a")
    
# def f_b(func):
#     def wrapper():
#         print(f"f_b:{func}")
#         func()
#     return wrapper
    
# @f_a
# @f_b #bar = f_a(f_b(bar))

# def bar():
#     print("bar")
    
    
def strip(func):
    def wrapper(msg:str):
        func( msg.strip())
    return wrapper

def upper(func):
    def wrapper(msg:str):
        func( msg.upper())
    return wrapper

@upper
def prt_something1(msg:str):
    print(f"prt1:{msg}")
    
@strip
def prt_something2(msg:str):
    print(f"prt2:{msg}")

@upper
@strip 
def prt_something3(msg:str):
    print(f"prt3:{msg}")
    
prt_something1("        test1         ")
prt_something2("        test2         ")
prt_something3("        test3         ")