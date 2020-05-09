from requests import get

page = 1
item_per_page = 10
start = page*item_per_page-item_per_page
url = f"https://www.blibli.com/backend/search/products?page={page}&itemPerPage={item_per_page}&start={start}&category=SI-1000059"
headers = {'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'no-cache',
'channelid': 'mobile-web',
'pragma': 'no-cache',
'referer': 'https://www.blibli.com/c/2/handphone/HA-1000002/54593?page=1&itemPerPage=24&start=0&category=HA-1000002&sort=7',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
'x-b3-traceid': '14749c5f157d91c4'}

r = get(url, headers=headers)
products = r.json()['data']['products']
for p in products:
    try:
        url = f"https://blibli.com{p['otherOfferings']['allOfferPageUrl']}"
    except:
        url = 'no url'
    print(url)

