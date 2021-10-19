# free-proxy-list
# https://free-proxy-list.net/

#測試
# ipify
# 'https://api.ipify.org?format=json'
import requests
import re


url = "https://free-proxy-list.net/"

res = requests.get(url)

m = re.findall("\d+\.\d+\.\d+\.\d+:\d+",res.text)

iplist = []
for ip in m:
    try:
        res = requests.get('https://api.ipify.org?format=json', proxies={'https':'https://'+"20.94.229.106:80"},timeout=2)
        iplist.append(res)
        print("[get] :", ip)
    except:
        print("fail")