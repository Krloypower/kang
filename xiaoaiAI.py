import pandas as pd
import json
import requests
import csv
import urllib.parse


def xiaoaiAI(q):
    url = 'https://xiaoai.mi.com/vs/v1/product/test/answer'

    payload = 'app_type=DeviceOAuth&env_stage=production&product_id=354325156606249984&query=' + urllib.parse.quote(
        q) + '&session_id=9ce12fa41c5c4a5e9a29fc07e70a276f&xiaoai_open_ph=Yr7gy9BM605OqIKXvkY6IQ%3D%3D'
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'charset': "UTF-8",
        'Cookie': "mstuid=1550489136961_6069; muuid=1550489136883_2635; Hm_lvt_16239c691cd667025dc31ebf599c8fff=1564367303; _ga=GA1.2.1473215538.1564367305; _gid=GA1.2.646028588.1576750533; serviceToken=bbMzdd2LioDGBNzuVv/X+i5KiGsKeisw7pt6s5YQKzIZKmOwXsW4XmtuLU6UibKSu5bzj1t2IHmMEm84kXliHaJCBxDqyRrS1YXM6f7sk5SzE0lNJps0Inw/IzXv/AR81eVEXddPoAlFQ930CXHQhCey5bSksscN3xnzzfkEF9tFaWPhXMgC7obpkWyaDXVT++moNibbi7JtklAnM03wVfXBEeiOJUvRVCOm+NYF0qEPVjCM5at+aseudIyEiUMNcs/V7RtRzfdNNSp1M8ycdokHBUjgsfV+/37Y8s/PEB0=; cUserId=E_GilVV-WDTWiHU68pw0YziDm9E; xiaoai_open_slh=U/qg5XWQboXRx+qD5EuIVEW/q/0=; xiaoai_open_ph=Yr7gy9BM605OqIKXvkY6IQ==",
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "2acc6365-8ffa-4997-9f54-49de3a590c82,97b14e62-75cc-4b99-8224-2ff1d31b3361",
        'Host': "xiaoai.mi.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "181",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        dump = json.loads(response.text)
        text_ = dump['answer'][0]['text']
    except BaseException as e:
        print(e)
        return "error"
    else:
        return text_


if __name__ == '__main__':
    text_io = open("/Users/xmly/Desktop/xiaoai.txt")
    text_result = ''
    while True:
        line = text_io.readline()
        if not line:
            break
            pass
        line_split = line.split("\t")
        first = line_split[0]

        xa_result = first + "\t"
        for num in range(3):
            xa = xiaoaiAI(first)
            print(xa)
            if xa is not None and xa_result.find(xa) < 0:
                xa_result = xa_result + xa + '\t'
            else:
                xa_result = xa_result + "\t"
        print(xa_result)
        text_result = text_result + xa_result + '\n'
    f = open("/Users/xmly/Desktop/xiaoai_num3_result.txt", 'w')
    f.write(text_result)
    f.close()
