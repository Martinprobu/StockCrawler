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

def run_url(gain, log, limit_time_start) :
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
    urlMain = 'https://xueqiu.com/cubes/discover/rank/cube/list.json?category=12&count=10&market=cn&profit=' + gain

    res = get_json(urlMain)
    # print(res)

    for list in res['list']:
        print("name : %s, gain : %s"%(list['name'], gain))
        #print(list['daily_gain'])
        #print(list['monthly_gain'])
        #print(list['last_user_rb_gid'])

        name = list['name']
        daily_gain = list['daily_gain']
        monthly_gain = list['monthly_gain']
        symbol = list['symbol']
        gid = list['last_user_rb_gid']

        urlUser = 'https://xueqiu.com/cubes/rebalancing/show_origin.json?rb_id=' + str(gid)
        time.sleep(random.random() * 2)
        res = get_json(urlUser)
        # print(res)
        createTime = time.localtime(res['rebalancing']['created_at']/1000)
        create_time = int(time.mktime(createTime))

        if create_time > limit_time_start :
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

if __name__ == '__main__':
    while 1 == 1:
        gain = 'daily_gain'
        log = '../log/xueqiu202206_daily_gain.log'
        limit_daily_time_start = run_url(gain, log, limit_daily_time_start)
        time.sleep(random.random() * 2)

        gain = 'monthly_gain'
        log = '../log/xueqiu202206_monthly_gain.log'
        limit_monthly_time_start = run_url(gain, log, limit_monthly_time_start)
        time.sleep(random.random() * 2)

        gain = 'annualized_gain_rate'
        log = '../log/xueqiu202206_year_gain.log'
        limit_year_time_start = run_url(gain, log, limit_year_time_start)

        time.sleep(random.random() * 5 * 60)