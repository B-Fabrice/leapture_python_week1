from speaklater import make_lazy_string

s = u'Hello world'
a = make_lazy_string(lambda: s)
print(a)

#if we make change of our string, lazy string will change too

s = u'Change have made!'
print(a)