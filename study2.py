import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
requests_get = requests.get(url)
json = requests_get.json()
print(json)
cnames = list(map(lambda x: x['cname'], json))
enames = list(map(lambda x: x['ename'], json))


def downloadPic():
    i = 0
    for j in cnames:
        # 创建文件夹
        os.mkdir('/Users/xmly/PycharmProjects/kang/' + cnames[i])
        # 进入文件夹
        os.chdir('/Users/xmly/PycharmProjects/kang/' + cnames[i])
        i += 1
        for k in range(10):
            link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(link)
            if im.status_code == 200:
                # 写入文件
                open(str(k) + '.jpg', 'wb').write(im.content)
