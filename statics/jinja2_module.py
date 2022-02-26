#jinja include various function as shown below

from jinja2 import Template
import jinja2

# Template function help use to generate dynamic template
t = Template('{{ name }}, welcome to our page')
print(t.render(name='Anna'))

print(dir(jinja2))