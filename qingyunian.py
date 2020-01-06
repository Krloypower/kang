import json
from pyquery import PyQuery as pq

url = 'http://www.bimibimi.tv/bangumi/2132/play/1/35/'
doc = pq(url=url)
print(doc("#video"))
