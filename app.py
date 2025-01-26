import json


# считываем JSON
with open('data.json', 'r') as f:
	data = json.load(f)

print(data) 