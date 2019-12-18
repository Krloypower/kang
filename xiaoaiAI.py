import pandas as pd
import json
import requests
import csv
import urllib.parse



def xiaoaiAI(q):
    url = 'https://xiaoai.mi.com/vs/v1/product/test/answer'

    payload = 'app_type=DeviceOAuth&env_stage=production&product_id=354325156606249984&query='+urllib.parse.quote(q)+'&session_id=9ce12fa41c5c4a5e9a29fc07e70a276f&xiaoai_open_ph=%2BMOKom76tBdZvu9AR%2Bf3Qw%3D%3D'
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'charset': "UTF-8",
        'Cookie': "mstuid=1550489136961_6069; muuid=1550489136883_2635; Hm_lvt_16239c691cd667025dc31ebf599c8fff=1564367303; _ga=GA1.2.1473215538.1564367305; _gid=GA1.2.1993106517.1576662448; serviceToken=bbMzdd2LioDGBNzuVv/X+kYjLGIkcMxyJSEm+zxqTY8leaocBQ/urOo3jPWhFuj/zuWALlWOm+0rXgLMs0o4+OTIv/H0eEpxtW8Rfqky0pJTwaVNFDfLwD2r/Uaen+SWxXpTMNxUEEVeZK4Pq8hdfYq8Ny/D3Np6GI5xG49de78uMdaNeCBovOiJgSLW+ZJNB00VDzP8XiPNbjHiyT769/sNqyCiupJtekzSpM83HiW0SZlZ9zCEBcvyfAVSG6U0NbT2vGR6pUeWq4wmEFRjfZ2t1b9yprKK5an7aaTbBk0=; cUserId=E_GilVV-WDTWiHU68pw0YziDm9E; xiaoai_open_slh=zz4UEd5RQEOpAubj5sg7zy9y3+M=; xiaoai_open_ph=+MOKom76tBdZvu9AR+f3Qw==",
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "2acc6365-8ffa-4997-9f54-49de3a590c82,97b14e62-75cc-4b99-8224-2ff1d31b3361",
        'Host': "xiaoai.mi.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "233",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        dump = json.loads(response.text)
        text_ = dump['answer'][0]['text']
    except BaseException:
        return "error"
    else:
        return text_


text_io = open("/Users/xmly/Desktop/xiaoai.txt")
text_result = ''
while True:
    line = text_io.readline()
    if not line:
        break
        pass
    line_split = line.split("\t")
    first = line_split[0]

    print(first)
    ai = xiaoaiAI(first)
    print(ai)
    text_result = text_result + first + "\t" + ai + "\n"
f = open("/Users/xmly/Desktop/xiaoai_result.txt", 'w')
f.write(text_result)
f.close()