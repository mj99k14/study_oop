class Foo:
    name ="Class object"


obj = Foo()

obj.name = "Foo instance"

print(obj.name)
print(Foo.name)
