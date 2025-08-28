class Bar :
    def prt_name(self):
        print("Bar")


class Foo:
    def prt_name(self):
        print("foo")
        
        
        
bar_1 = Bar()
foo_1 = Foo()


def prt(obj):
    obj.prt_name()
    
    
print(bar_1)
print(foo_1)