import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Authorization': 'Bearer eyJpZCI6Mn0.ZQq6-g.zylJxppPQGR2w7iQYhMoxXQqcw4',
    'Connection': 'keep-alive',
    'Origin': 'http://10.202.159.9:8080',
    'Referer': 'http://10.202.159.9:8080/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': 'eyJpZCI6Mn0.ZQq6-g.zylJxppPQGR2w7iQYhMoxXQqcw4',
}

params = {
    'province': '',
    'downtown': '',
    'page_num': '1',
    'page_size': '8',
}

response = requests.get('http://127.0.0.1:5000/user/user', params=params, headers=headers)
print(response.json())
