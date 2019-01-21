import yaml
import json
from pprint import pprint

with open('exe6-yml.yml') as f:
   yamal_devices = yaml.load(f)

with open('exe6-json.json') as f:
   json_devices = json.load(f)


print("The following is in yamal format: ")
pprint(yamal_devices)
print('\n')
print('\n')
print("The following is in json format: ")
pprint(json_devices)
