#!/usr/bin/env python
import jinja2

with open("intf_config_set.j2") as f:
    intf_config = f.read()

intf_vars = {
    'ip_addr': '10.220.88.20',
    'netmask': '255.255.255.0',
}

template = jinja2.Template(intf_config)
output = template.render(**intf_vars)
print(output)

