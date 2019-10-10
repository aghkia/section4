import urllib.request as req
import simplejson as json
import os.path

#url
url = 'https://jsonplaceholder.typicode.com/comments'

#경로 & 파일명
savename = 'c:/section4/section4_work.json'

if not os.path.exists(url):
    req.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding='utf-8'))
#items = json.loads(open(savename, 'r', encoding='utf-8').read())

#출력
for item in items:
    print(str(item['id']) + '  -  ' + str(item['email']))
