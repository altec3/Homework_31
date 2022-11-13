import csv
import json
from typing import List, Dict, Any


def convert_csv_to_json(csv_file: str) -> str:
    """ Converts structure of file from CSV to JSON """

    json_list = []
    with open(csv_file, encoding='utf-8') as csvf:
        csv_read = csv.DictReader(csvf)

        for row in csv_read:
            for k, v in row.items():
                if v == 'TRUE':
                    row[k] = True
                elif v == 'FALSE':
                    row[k] = False
                elif k == 'location_id':
                    row[k] = [int(v)]
            json_list.append(row)

    return json.dumps(json_list, indent=4, ensure_ascii=False)


def create_fixtures(input_file: str, output_file: str, model: str) -> None:
    """ Creates Django fixtures from a json file """

    data = []
    json_list: List[Dict[str, Any]] = json.loads(input_file)
    for item in json_list:
        json_dict: Dict[str, Any] = {"pk": item.pop("id"), "model": model, "fields": item}
        data.append(json_dict)

    with open(output_file, 'w', encoding='utf-8') as f:
        fixtures = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(fixtures)
