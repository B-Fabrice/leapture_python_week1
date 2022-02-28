#future module help use to run python code from different versions similar

import __future__
from __future__ import print_function, division

print(__future__.all_feature_names)

# we use print function as 'print "hello world"' in python 2
# but because we have import print_function, following code will run even it is python 3 code
print('hello world')
