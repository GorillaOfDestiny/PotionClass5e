import json
from tqdm.auto import tqdm
import os



potions_dir = "potion_jsons/"
potions_file = "potions.json"
if not os.path.isfile(potions_file):
    url = r"https://www.dnd5eapi.co/api/2014/equipment-categories/potion"
    os.system(f'curl -X GET "{url}" -H "Accept: application/json" --output potions.json')

with open(potions_file,"r") as f:
    json_data = json.load(f)

f.close()

if not os.path.isdir(potions_dir):
    os.mkdir(potions_dir)

for potion_data in tqdm(json_data["equipment"],desc = "Getting potion data"):
    url = "https://www.dnd5eapi.co/api/2014/magic-items/"+potion_data["index"]

    pname = potion_data["index"]
    os.system(f'curl -X GET "{url}" -H "Accept: application/json" --output {potions_dir}{pname}.json')