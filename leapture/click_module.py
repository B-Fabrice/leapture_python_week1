# Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.

import click

@click.command()
@click.option('--number', default=1, help='number of count')
@click.option('--name', prompt='enter your name: ', help='get greeting from here')
def greeting(number, name):
    for x in range(number):
        click.echo(f'hello {name}! this is greeting for you')

if __name__ == '__main__':
    greeting()