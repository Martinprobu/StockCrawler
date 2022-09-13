import time
import datetime

from common.WeChatPub import WeChatPub

re = (11-10.65) * 1000
# print(re)


# time = time.time()
# print(time)

r1 = 1650739799031 / 1000
# print (r1)


with open('../log/data.log', 'w') as fileObj:
    print('hello world!', file=fileObj)


n_time = datetime.datetime.now()
# print(n_time)

d_time_start = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M')
d_time_end = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '18:00', '%Y-%m-%d%H:%M')

# 当天时间tuo
o1 = int(time.mktime(datetime.datetime.now().timetuple())) - 120


# dateTime = time.strftime('%Y-%m-%d %H:%M:%S', 1655090382)
        # dateTime = datetime.datetime.fromtimestamp(1655090382)
        # print(dateTime)

time1 = datetime.datetime.strptime('2022-06-14 09:01:01', '%Y-%m-%d %H:%M:%S')
# print(time.mktime(time1.timetuple()))
#time1 = time.strftime(1655097639, '%Y-%m-%d %H:%M:%S')
#print(time1)
print(time.ctime(1655098363))

wechat = WeChatPub()
now = datetime.datetime.now()
timenow = now.strftime('%Y年%m月%d日 %H:%M:%S')
# wechat.send_msg(f"<div class=\"gray\">{timenow}</div> <div class=\"normal\">fail login</div><div class=\"highlight\">请尽快更换新的 cookie</div>", "www.baidu.com")

wechat = WeChatPub()
name = 'test测试'
symbol = 'gggss测试'
create_time = 365654664
wechat.send_msg("name :%s, https://xueqiu.com/P/%s, datetime: %s"%(name, symbol, time.ctime(create_time)), "https://xueqiu.com/P/" + symbol)






