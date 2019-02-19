#!/usr/bin/env python
import jinja2

my_vars = {
   "router1": "cisco 881, fremont, ca"
}

my_template = '''
{{ router1 }}
{{ router1 | upper }}
{{ router1 | capitalize }}
{{ router1 | center( 80) }}
{{ router1 | upper | center( 80) }}
{{ route2 | default('not defined') }}
{{ "%30s %30s" | format(router1, "hello") }}
'''

template = jinja2.Template(my_template)
print(template.render(my_vars))


