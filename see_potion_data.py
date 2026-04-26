import json
import glob
import os

def load_json(file_name):
    with open(file_name,"r") as f:
        json_data = json.load(f)
    f.close()
    return(json_data)

potion_dir = "potion_jsons/"
assert os.path.isdir(potion_dir), "directory {potion_dir} not found"
all_files = glob.glob(potion_dir + "*.json")


potion_dict = {"uniques":[],
               }
for f in all_files:
    json_data = load_json(f)
    if json_data["variant"] == True and "Healing" not in f:
        continue
    elif "Healing" in f:
        potion_dict["healing"] += [json_data['index']]
    elif len(json_data["variants"]) == 0:
        potion_dict["uniques"] += [json_data['index']]
    
    else:
        potion_dict[json_data['index']] = [jdv["index"] for jdv in json_data["variants"]]
print(json.dumps(potion_dict,indent = 4))