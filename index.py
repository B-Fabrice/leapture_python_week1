from attrs import make_class

# attrs can be used to make simple class
D = make_class('st', ['name', 'age'])
x = D('Amina', 12)
# print(x.name)

from babel import Locale
# babel include module called Locale
# locale = Locale('en', 'BR')
# print(locale.territories['BR'])

from cachetools import cached
# cachetools provide various collections of decorators
@cached({})
def fibon(n):
    return n if n < 2 else fibon(n-1) + fibon(n-2)

from cffi import FFI
# cffi
# ready file of different datatype from different os

import click
#CLICK Command Line Interface Creation Kit
@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)

# if __name__ == '__main__':
#     hello()

# This client library is designed to support the Facebook Graph API and the official Facebook JavaScript SDK, 
# which is the canonical way to implement Facebook authentication.

# from __future__ import (absolute_import, division,
#                         print_function, unicode_literals)
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)

# for x in range(1, 10):
#     print(x)

from markupsafe import Markup, escape

#escape replaces special characters and wraps in Markup
escape("<script>alert(document.cookie);</script>")
Markup('&lt;script&gt;alert(document.cookie);&lt;/script&gt;')

# wrap in Markup to mark text "safe" and prevent escaping
Markup("<strong>Hello</strong>")
Markup('<strong>hello</strong>')

escape(Markup("<strong>Hello</strong>"))
Markup('<strong>hello</strong>')

from PIL import Image
import os, sys

img = Image.open('kjsdnkjs.png')
# print(img.format)
# print(img.size)
# print(img.height)
# print(img.width)
# print(img.info)
# img.show()

#Convert img to JPEG

jpgimg = img.convert('RGB')
# jpgimg.save('jpg_converted.jpg')
# jpgimg.show()


#create thumbnails from JPEG

# conimg = img.convert('RGB')
# conimg.thumbnail((70, 70))
# conimg.save('thumbnail.jpg')
# conimg.show()

#resize img
# resizedImg = img.resize((150, 150))
# resizedImg.show()

# pycodestyle is used to show us the style of our file as python file
# pyflakes does the same as the pycodestyle

# from pyrsistent import v, pvector
# v1 = v(2, 4, 7)
# print(v1)
# v2 = v1.append(5)
# print(v2)
# v3 = v2.set(1, 3)
# print(v3)

from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
# now = parse("Sat Oct 11 17:13:46 UTC 2003")
# today = now.date()
# year = rrule(YEARLY,dtstart=now,bymonth=8,bymonthday=13,byweekday=FR)[0].year
# rdelta = relativedelta(easter(year), today)
# print("Today is: %s" % today)
# #Today is: 2003-10-11
# print("Year with next Aug 13th on a Friday is: %s" % year)
# #Year with next Aug 13th on a Friday is: 2004
# print("How far is the Easter of that year: %s" % rdelta)
# #How far is the Easter of that year: relativedelta(months=+6)
# print("And the Easter of that year is: %s" % (today+rdelta))

# import editor
# editor.edit('index.py')

import twitter
print(twitter.Api())

from pytz import timezone, country_names

#country code
# for x in country_names:
#     print(x)

# import qrcode
# img = qrcode.make('index.py')
# img.show()


# from speaklater import make_lazy_string
# s = make_lazy_string('hello world')
# print(s)

import zipfile
import zipp
import io

data = io.BytesIO()
z = zipp.Path('exp.zip')
z.open()

