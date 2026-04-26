import json
from tqdm.auto import tqdm
import os


# Opening JSON file
f = open('spells.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
print(data['results'])
# Closing file
f.close()

for d in tqdm(data['results']):
    spell_name = d['index']
    url = d['index']
    os.system(f'curl -X GET "https://www.dnd5eapi.co/api/2014/spells/{url}" -H "Accept: application/json" --output spells/{spell_name}.json')
