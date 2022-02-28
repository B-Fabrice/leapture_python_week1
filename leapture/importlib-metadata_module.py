# importlib-metadta is a library that provides for access to installed package metadata

from importlib.metadata import metadata, version

#version function can help us to check version of our package
print(version('future'))
print(version('attrs'))
print(version('pillow'))

#you can also get metadata as shown below
print(list(metadata('pillow')))