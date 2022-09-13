import requests
import datetime
import time
import random

from WeChatPub import WeChatPub


def get_json(url):

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'xueqiu.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'macOS'
    }

    cookies = get_cookies()
    # print(cookies)

    # session = requests.Session()
    # session.get(url, headers=headers) #捕获并且存储cookie

    response = requests.get(url, headers=headers, cookies=cookies).json() #携带cookie发起的请求
    # print(response.url)
    # print(response.text)
    return response

def run_url(gain, log, limit_time_start, start_name) :
    #limit_time_start = time.mktime(datetime.datetime.strptime('2022-06-13 11:10:00', '%Y-%m-%d %H:%M:%S').timetuple())
    #limit_time_start = 0
    #gain = 'monthly_gain'
    #log = '../log/xueqiu202206_monthly_gain.log'
    # 范围时间
    if limit_time_start == 0 :
        limit_time_start = int(time.mktime(datetime.date.today().timetuple()))

    print("start_time : %s, datetime : %s, gain : %s============================== start_time "%(limit_time_start, time.ctime(limit_time_start), gain))
    with open(log, 'a') as fileObj:
        print("start_time : %s, datetime : %s, gain : %s============================== start_time "%(limit_time_start, time.ctime(limit_time_start), gain), file=fileObj)
    

    name = ''
    daily_gain = gain
    monthly_gain = gain
    symbol = start_name
    gid = start_name

    
    time.sleep(random.random() * 2)
    res = get_json(start_name)
    # print(res)
    createTime = time.localtime(res['rebalancing']['created_at']/1000)
    create_time = int(time.mktime(createTime))
    print(time.ctime(create_time))
    print(time.ctime(limit_time_start))
    # print("create_time: %s"%(time.ctime(create_time)), file=fileObj)

    if create_time > limit_time_start :
        # res['rebalancing_histories']['stock_name']
        wechat = WeChatPub()
        wechat.send_msg("name :%s, https://xueqiu.com/P/%s, datetime: %s"%(name, symbol, time.ctime(create_time)), "https://xueqiu.com/P/" + symbol)

        print("name: %s, daily_gain: %s, monthly_gain: %s, symbol: https://xueqiu.com/P/%s, datetime: %s"%(name, daily_gain, monthly_gain, symbol, time.ctime(create_time)))
        with open(log, 'a') as fileObj:
            print("time: %s"%datetime.datetime.now(), file=fileObj)
            print("name: %s, daily_gain: %s, monthly_gain: %s, symbol: https://xueqiu.com/P/%s, datetime: %s"%(name, daily_gain, monthly_gain, symbol, time.ctime(create_time)), file=fileObj)

                    

    prev_time = int(time.time() - 120)
    print("end_time : %s, datetime : %s, gain : %s============================ end_time "%(prev_time, time.ctime(prev_time), gain))
    with open(log, 'a') as fileObj:
        print("end_time : %s, datetime : %s, gain : %s============================ end_time "%(prev_time, time.ctime(prev_time), gain), file=fileObj)

    return prev_time

def get_cookies() :
    f = open('../data/cookies/xueqiu_login2.txt','r')#打开所保存的cookies内容文件
    cookies = {}#初始化cookies字典变量 
    for line in f.read().split(';'):  #按照字符：进行划分读取 
        #其设置为1就会把字符串拆分成2份 
        name,value=line.strip().split('=',1) 
        cookies[name]=value #为字典cookies添加内容
    return cookies



limit_daily_time_start = 0
#limit_daily_time_start = time.mktime(datetime.datetime.strptime('2022-06-16 10:30:00', '%Y-%m-%d %H:%M:%S').timetuple())

limit_monthly_time_start = 0
#limit_monthly_time_start = time.mktime(datetime.datetime.strptime('2022-06-16 10:30:00', '%Y-%m-%d %H:%M:%S').timetuple())

limit_year_time_start = 0
#limit_monthly_time_start = time.mktime(datetime.datetime.strptime('2022-06-16 10:30:00', '%Y-%m-%d %H:%M:%S').timetuple())

start_name = 'https://xueqiu.com/cubes/rebalancing/show_origin.json?rb_id=123546877&cube_symbol=ZH2514120'

if __name__ == '__main__':
    while 1 == 1:
        gain = 'daily_gain_v_one'
        log = '../log/xueqiu202207_ZH2514120.log'
        limit_daily_time_start = run_url(gain, log, limit_daily_time_start, start_name)
        time.sleep(random.random() * 2)

        

        time.sleep(random.random() * 5 * 60)


