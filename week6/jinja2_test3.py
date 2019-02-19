#!/usr/bin/env python
from jinja2 import FileSystemLoader, StrictUnderfined
from jinja2.environment import Environment

env = Environment(undefined=StrictUdefined)
env.loader = FileSystemLoader('.')

intf_vars = {
        'ip_addr': '10.220.88.20',
        'netmask' : '255.255.255.0',
}

template_file = 'intf_config333.j2'
template = env.get_template(template_file)
output = template.render(**intf_vars)
print(output)

