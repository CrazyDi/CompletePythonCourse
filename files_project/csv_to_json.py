import json


csv_file = open('csv_file.txt', 'r')
result_list = [line.strip() for line in csv_file.readlines()]
csv_file.close()

result_json = list()
for line in result_list:
    result_json.append(dict(zip(["club", "country", "city"], [line.split(',')[0], line.split(',')[2], line.split(',')[1]])))

json_file = open('json_file.txt', 'w')
json.dump(result_json, json_file)
json_file.close()
