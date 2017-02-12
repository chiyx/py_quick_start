class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return "Hello world"

instance = MyClass()
print(instance.i)
instance.i = 100
print(MyClass.i)
print(instance.i)

def h():
    return "Hello H"

# instance.f = h
instance.b = "x"

print(instance.f())
print(MyClass.f(instance))
print(instance.b)
print(instance.__class__)

