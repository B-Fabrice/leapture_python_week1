#attr help us to deal with classes without boilerplate

from attrs import make_class, asdict, define

# let's define our own class
@define
class worker:
    id: int
    name: str

# create class object
a = worker(12, 'amina')
print(a)

# we can use make_class method to create class with object direct
D = make_class('st', ['name', 'age'])
x = D('Amina', 12)

#this will give as st object with values
print(x)

#this will print st object as dictionary
print(asdict(x))
