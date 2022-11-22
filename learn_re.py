import requests
import json



r = requests.post('https://baconipsum.com/api/?type=meat-and-filler')
d = json.loads(r.content)
print(d[0])