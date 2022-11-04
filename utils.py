import csv
import json
from typing import Union, List, Dict, Any


def convert_csv_to_json(csv_file: str, json_file: str) -> None:
    json_list = []

    with open(csv_file, encoding='utf-8') as csvf:
        csv_read = csv.DictReader(csvf)

        for row in csv_read:
            for k, v in row.items():
                if v == 'TRUE':
                    row[k] = True
                elif v == 'FALSE':
                    row[k] = False
            json_list.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        json_str = json.dumps(json_list, indent=4, ensure_ascii=False)
        jsonf.write(json_str)


def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def convert_json_to_fixtures(input_file: str, output_file: str, model: str) -> None:
    data = []
    json_list: List[Dict[str, Any]] = read_json(input_file)
    for item in json_list:
        temp = {"pk": item.pop("id"), "model": model, "fields": item}
        data.append(temp)

    with open(output_file, 'w', encoding='utf-8') as f:
        fixtures = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(fixtures)
