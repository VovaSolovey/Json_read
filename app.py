import json


# считываем JSON
with open('data.json', 'r', encoding='UTF-8') as f:
	data = json.load(f)



print(data) 