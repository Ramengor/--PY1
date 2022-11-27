import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    f = open(filename, 'r')
    headers = next(f)[:-1].split(delimiter)
    items = []
    size = len(headers)
    for line in f:
        line = line[:-1].split(delimiter)
        item = {}
        for i in range(size):
            item[headers[i]] = line[i]
        items.append(item)
    f.close()
    return items
    # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
