from babel import Locale

# babel include module called Locale
# this is used as shown in below example

a = Locale('rw', 'RW')
print(a.territories['RW'])

print(Locale.parse('zh_TW'))

#Locale display names
b = Locale.parse('uk_UA')
#display country name
print(b.get_display_name('en_US'))
#display country language name
print(b.get_language_name('en_US'))

# Calendar display names
months = b.months['format']['wide'].items()
for m in months:
    print(m)
