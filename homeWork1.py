import requests
import json
from pprint import pprint


data = {'v': '9793d741120c99fdeef86268d4876a70243d8a6e'}

response = requests.get('https://akabab.github.io/superhero-api/api/all.json', data = data)

name_SH = ['Hulk', 'Captain America', 'Thanos']
int_SH_dict = {}
json_data = response.json()


for super_hero in json_data:
    for name in name_SH: 
        if name == super_hero.get('name'):
            # print(super_hero.get("powerstats").get("intelligence"))
            int_SH_dict[name] = super_hero.get("powerstats").get("intelligence")
max_key = max(int_SH_dict, key=int_SH_dict.get)
print(f'Самый умный герой это {max_key}')
# sorted_tuples = sorted(int_SH_dict.items(), key=lambda item: item[1])
# # print(sorted_tuples)  
# sorted_dict = {k: v for k, v in sorted_tuples}
# # print(sorted_dict)



    # print(type(x))
# data = response.json()
# with open('data.txt', 'w') as f:
#     json.dump(data, f)
    
# # pprint (response.json())