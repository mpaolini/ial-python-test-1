import requests

resp = requests.get('http://ialpython.apiary.io/laboratories')
lab = resp.json()

lab_2 = []

for d in lab:
	for x in d:
		if x == "network_status":
			if d[x] == "down":
				lab_2.append(d["name"])

print lab_2