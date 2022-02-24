from attrs import make_class
from babel import Locale
from cachetools import cached, LRUCache, TTLCache
from cffi import FFI
import click

# attrs can be used to make simple class
D = make_class('st', ['name', 'age'])
x = D('Amina', 12)
# print(x.name)

# babel include module called Locale
# locale = Locale('en', 'BR')
# print(locale.territories['BR'])

# cachetools provide various collections of decorators
@cached({})
def fibon(n):
    return n if n < 2 else fibon(n-1) + fibon(n-2)

# cffi
# ready file of different datatype from different os

#CLICK Command Line Interface Creation Kit
@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)

if __name__ == '__main__':
    hello()

# This client library is designed to support the Facebook Graph API and the official Facebook JavaScript SDK, 
# which is the canonical way to implement Facebook authentication.

