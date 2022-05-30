import sys
import json


def list_dict(dicts):
    for i in dicts:
        for j in values['values']:
                if i['id'] == j['id']:
                    i['value'] = j['value']
                    break
        # print(i)
        if 'values' in i.keys():
            list_dict(i['values'])


if __name__ == "__main__":
    with open(file=sys.argv[1], mode="r") as tests_json:
        tests = json.load(tests_json)

    with open(file=sys.argv[2], mode="r") as values_json:
        values = json.load(values_json)

    report = tests.copy()
    list_dict(dicts=report['tests'])

    with open(file="report.json", mode="w") as report_json:
        json.dump(report, report_json)
