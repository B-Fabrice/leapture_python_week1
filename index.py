from attrs import make_class
from babel import Locale

D = make_class('st', ['name', 'age'])
x = D('Amina', 12)
print(x.name)

