import pandas as pd
import json
import requests
import csv
import urllib.parse

osAccessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJvcy5jbGllbnQuc2RrZGVtbyIsInVpZCI6MCwicHJvZHVjdElkIjoiTl9QUk9EMV83IiwiaXNzIjoieHktb3MtdWNlbnRlciIsImV4cCI6MTU3Njc0NzE0OCwiZGV2aWNlSWQiOiI1NjJiOWE2Y2E1OGQ5MDkyMSJ9.wWu2YJXYPpRg9puugRaZZENdazAnkX3TvSdILJbm4R0"


def xiaoya(q):
    url = "http://api.ximalaya.com/smart-os-gateway/smart-os-openapi/text/query"
    global osAccessToken
    querystring = {
        'params': '{"appVersion":"2.1.3","childMode":false,"deviceId":"8d3e29b09d905002","deviceType":2,"dt":1561347428,"ip":"111.204.31.18","isChildMode":false,"lat":"","lng":"","osClientId":"os.client.000187","osOpenId":"","productId":"N_PROD1_7","romVersion":"1.2.0","sn":"562b9a6ca58d90921","speakerVersion":"0.3.0","sysType":1,"sysVersion":"9","uid":"2229252","xn":"","osAccessToken":"' + osAccessToken + '"}',
        'aotuman': 'true', 'text': q}

    headers = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "1120aee0-d977-4f45-a5ee-43ed85aaa0be,7adec8f2-7432-4b4d-8bb1-f1b5130fba67",
        'Host': "api.ximalaya.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    dump = {}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        dump = json.loads(response.text)
        text_ = dump['response']['outputSpeech']['text']
    except BaseException:
        print(dump)
        if dump.get("error") == '5004':
            osAccessToken = access_token()
        return dump.get("message")
    else:
        return text_


def access_token():
    url = "http://api.ximalaya.com/smart-os-gateway/xy-os-ucenter/account/guest-login"

    querystring = {
        "params": '{"appVersion":"2.1.3","childMode":false,"deviceId":"8d3e29b09d905002","deviceType":2,"dt":1561347428,"ip":"111.204.31.18","isChildMode":false,"lat":"","lng":"","osClientId":"os.client.000187","osOpenId":"","productId":"N_PROD1_7","romVersion":"1.2.0","sn":"562b9a6ca58d90921","speakerVersion":"0.3.0","sysType":1,"sysVersion":"9","uid":"2229252","xn":"","osAccessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJvcy5jbGllbnQuc2RrZGVtbyIsInVpZCI6MCwicHJvZHVjdElkIjoiTl9QUk9EMV83IiwiaXNzIjoieHktb3MtdWNlbnRlciIsImV4cCI6MTU3Njc0NTE4MSwiZGV2aWNlSWQiOiI1NjJiOWE2Y2E1OGQ5MDkyMSJ9.B3q1Q1h57FGQZkMBVT284j_XRoepfqvUEWTQfPgEm7Y"}',
        "sig": "111", "aotuman": "1"}

    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "349030de-c060-4a75-b172-28907474540f,c270a1b2-6dea-4f28-8a32-4104d1ee58c2",
        'Host': "api.ximalaya.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    try:
        response = requests.request("POST", url, headers=headers, params=querystring)
        dump = json.loads(response.text)
        token_ = dump['osAccessToken']
    except BaseException:
        return "error"
    else:
        return token_


if __name__ == '__main__':
    a = 1
    print(a is None)
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
            xy = xiaoya(first)
            print(xy)
            if xy is not None and xa_result.find(xy) < 0:
                xa_result = xa_result + xy + '\t'
            else:
                xa_result = xa_result + "\t"
        print(xa_result)
        text_result = text_result + xa_result + '\n'
    f = open("/Users/xmly/Desktop/xiaoya_num3_result.txt", 'w')
    f.write(text_result)
    f.close()
