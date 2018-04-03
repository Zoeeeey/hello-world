import requests
import time

def getURL(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return True
    except:
        return False

def timecounter(n):
    if getURL(url):
        t1 = time.time()
        for i in range(n):
            getURL(url)
        t2 = time.time()
    else:
        return "爬取失败"
    result = t2 - t1
    return "爬取用时"+str(result)

if __name__=='__main__':
    url = input('请输入你要爬取的初始网址')
    while True:
        try:
            m = int(input("你想爬取网站多少次？"))
            time = timecounter(m)
            print(time)
            break
        except:
            print("请输入一个数字")


