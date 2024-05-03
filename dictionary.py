maps = {
        "key1": "value1",
        "key2": "value2",
        }

value = maps["key1"]
print(value)

maps["key1"] = "value12"

maps["new_key"] = "new_value"

del maps["key2"]

exists = "key2" in maps

length = len(maps)

keys = maps.keys()

values = maps.values()

items = maps.items()
