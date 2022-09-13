import requests
import json
#import Levenshtein
#import openpyxl
#from openpyxl.styles import Font


# post 方式
def post_json(key_word):
    params = {"keyword": key_word,
              "openWhiteList": False, "platform": "pc",
              "requestType": "search", "size": 3,
              "vid": "rBIKGF6lR+5p7zgKD0K2Ag=5", "visitIP":"192.168.54.17"}
    # params post传的参数
    x = requests.post("http://******/probase/query-intent", data=json.dumps(params))
    EntityResult = json.loads(x.text)['entityResolutionResult']   # json转为字典


# get方式
def get_json():
    url = 'http://httpbin.org/get'
    data = {
        'name':'zhangsan',
        'age':'25'
    }
    response = requests.get(url, params=data)
    print(response.url)
    print(response.text)

# get方式
def get_json2():
    url = 'http://httpbin.org/get'
    response = requests.get(url)
    print(response.url)
    print(response.text)
'''
s = requests.Session()
headers = {'Host':'www.xxx.com'}
postdata = {'name':'aaa'}
url = 'http://xxxxx'
s.headers.update(headers)
r = s.post(url, data=postdata)
'''
get_json2()

with open('log/data.log', 'w') as fileObj:
    print('hello world!', file=fileObj)