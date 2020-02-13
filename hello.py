print("To begin, insert your name, please!")
name=input()
print(f"Hello, {name}!")
i=28
print(f"i is {i}")
f=2.8
print(f"f is {f}")
b=True
print(f"b is {b}")
n=None
print(f"n is {n}")
x= -28
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
name="Alice"
Coordinates=(10.0,20.0)
names=["Alice", "Bob", "Charlie"]
for i in range(5):
    print(i)
names=["Alice", "Bob", "Charlie"]
for name in names:
    print(name)
s= set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)
ages={"Alice":22, "Bob":27}
ages["Charlie"]=30
ages["Alice"]+=1
print(ages)
def square(x):
    return x * x
for i in range(10):
    print("{} squared is {}".format(i, square(i)))
class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
p= point(3,5)
print(p.x)
print(p.y)
