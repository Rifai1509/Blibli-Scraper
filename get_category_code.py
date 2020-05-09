import requests
import json

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    
}

res = requests.get('https://www.blibli.com/backend/common/categories', headers=headers)
json_res = res.json()

datas = json_res['data']
ids = []
for data in datas:
    id = data['id']
    ids.append(id)

print('found category: {}'.format(ids))


all_codes = []
for id in ids:
    print('getting children from {}'.format(id))
    res = requests.get('https://www.blibli.com/backend/common/categories/{}/children'.format(id), headers=headers)
    json_res = res.json()
    datas = json_res['data']
    codes = []
    for data in datas:
        code = data['categoryCode']
        codes.append(code)
    all_codes += codes

with open('all_codes.json', 'w') as outfile:
    json.dump(all_codes, outfile)
