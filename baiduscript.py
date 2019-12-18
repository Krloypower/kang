import pandas as pd
import json
import requests
import csv

url = "https://aip.baidubce.com/rpc/2.0/unit/bot/chat"

data = pd.read_csv("/Users/xmly/Desktop/搜狗随机.csv")

def ai_answer(q,answer):
    arr = []
    querystring = {"access_token":"24.3988ca5e01db3b3a976158681f3d05b5.2592000.1576063149.282335-17748161"}
    payload = "{\n    \"version\": \"2.0\",\n    \"bot_id\": \"88575\",\n    \"log_id\": \"uuid_1231_sdfka\",\n    \"request\": {\n        \"user_id\": \"kang.ouyang\",\n        \"query\": "  "\"" + q + "\""   ",\n        \"query_info\": {\n            \"type\": \"TEXT\",\n            \"source\": \"KEYBOARD\"\n        },\n        \"bernard_level\": 1\n    }\n}"
    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Content-Length': "306",
        'Connection': "keep-alive",
        }
    response = requests.request("POST", url, data=payload.encode(), headers=headers, params=querystring)
    dump = json.loads(response.text)
    say = dump['result']['response']['action_list'][0]['say']
    confidence = dump['result']['response']['action_list'][0]['confidence']
    intent = dump['result']['response']['schema']['intent']
    domain_confidence = dump['result']['response']['schema']['domain_confidence']
    flag = answer == say
    arr.append(q)
    arr.append(answer)
    arr.append(say)
    arr.append(flag)
    arr.append(confidence)
    arr.append(intent)
    arr.append(domain_confidence)
    return arr



if __name__ == '__main__':
    result = []
    for i in range(len(data)):
        q = data['data_xy_b_content_asr_nlp.b_query'][i]
        an = data['data_xy_b_content_asr_nlp.b_answertext'][i]
        try:
            answer = ai_answer(q, an)
        except BaseException:
            print("错误error", q, an)
        else:
            print(answer)
            result.append(answer)
    csv_open = open("/Users/xmly/Desktop/搜狗随机result.csv", "w")
    writer = csv.writer(csv_open)
    writer.writerow(["q", "answer", "say", "flag", "confidence", "intent", "domain_confidence"])
    writer.writerows(result)
    csv_open.close()

