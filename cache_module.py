# cachetools provide various collections of decorators
# this can be good for us for memory organisation
from cachetools import cached

@cached(cache={})
def fibon(n):
    return n if n < 2 else fibon(n-1) + fibon(n-2)

#from above, fibon function can take much size in memory as it is called
#but with cached decorators, will keep our fibon caches empty from our memory

print(fibon(32))