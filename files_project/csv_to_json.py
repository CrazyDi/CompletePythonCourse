import csv
import json


csv_file = open('csv_file.txt', 'r')
reader = csv.reader(csv_file)
result_list = list(reader)
csv_file.close()

result_json = []
for line in result_list:
    result_json.append({"club": line[0], "city": line[1], "country": line[2]})

json_file = open('json_file.txt', 'w')
json.dump(result_json, json_file)
json_file.close()
