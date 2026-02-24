import json


data = {"name": "Magzhan", "age": 17}
json_str = json.dumps(data)


parsed = json.loads(json_str)


pretty = json.dumps(data, indent=4)


with open("data.json", "w") as f:
    json.dump(data, f)


with open("data.json", "r") as f:
    file_data = json.load(f)


data_list = {"numbers": [1, 2, 3, 4]}


nested = {
    "user": {
        "name": "Magzhan",
        "city": "Atyrau"
    }
}


sorted_json = json.dumps(data, sort_keys=True)


obj = {"status": True}
json_obj = json.dumps(obj)


type_check = type(parsed)