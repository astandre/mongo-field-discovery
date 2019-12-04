import pymongo
import csv
from pathlib import Path

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

DB = "ocdb"
# DB = "test"

# COLLECTION_NAME = "definitions"
COLLECTION_NAME = "active"
# COLLECTION_NAME = "cursos"
# COLLECTION_NAME = "definition"

mydb = myclient[DB]
mycol = mydb[COLLECTION_NAME]
block_types = []


def evaluate(data):
    fields = []
    if type(data) is dict:
        keys = list(data.keys())
        print(keys)
        for key in keys:
            aux = {
                "key": key,
                "type": type(data[key]).__name__
            }
            # print(aux)
            if aux not in fields:
                fields.append(aux)

            fields_aux = evaluate(data[key])
            for field_aux in fields_aux:
                field_aux["key"] = key + "." + str(field_aux["key"])
                if field_aux not in results:
                    fields.append(field_aux)

    elif type(data) is list:
        for val in data:
            evaluate(val)
    # else:

    return fields


def write_results(results):
    file = f"data/{DB}.{COLLECTION_NAME}.csv"
    basedir = Path("./data")
    if not basedir.exists():
        basedir.mkdir(parents=True, exist_ok=True)
    with open(file, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['key', 'type']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)


results = []
control_fields = []

for x in mycol.find():
    # print(x)
    current_results = evaluate(x)
    for field_aux in current_results:
        if field_aux not in results:
            results.append(field_aux)
            control_fields.append(field_aux["key"])
        # if str(field_aux["key"]) not in control_fields:

results = sorted(results, key=lambda k: k['key'])

write_results(results)
print(control_fields)
print(len(control_fields))
