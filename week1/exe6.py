import yaml
import json

devices = range(8)
devices[-1] = {
'brand': 'arista',
'model': '7150s'
}

with open("exe6-yml.yml", "w") as f:
   f.write(yaml.dump(devices, default_flow_style=False))

with open("exe6-json.json", "w") as f:
   json.dump(devices, f)


