import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?fromdate=1687824000&todate=1687996800&order=desc&sort=activity&tagged=Python&site=stackoverflow')

json_dict = response.json()
for x in response.json()["items"]:
  print(x['title'])