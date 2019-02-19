#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

device_vars = {}

template_file = 'switch_intf_macro.j2'
template = jinja2.Template(template_file)
output = template.render(device_vars)
print(output)

