import requests
import prettytable
import time
import os

search = input('搜尋:')


para = {'q': '',
        'page': '1',
        'sort': 'sale/dc'}
para["q"] = search      
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

url ="https://ecshweb.pchome.com.tw/search/v3.3/all/results"


while True:
    
    os.system("cls")
    res = requests.get(url,params=para,headers = header)
    
    col = ["name","price"]
    table =prettytable.PrettyTable(col, encoding="utf-8")
    item_list = res.json()['prods']

    table.left_padding_width = 0
    for i in item_list:
        table.add_row((i["name"],i['price']))
        
    table.align["name"] = 'l'    
    table.align["price"] = 'r'
    print(f"現在正在第-{para['page']}-頁")
    print(table)
    x= input('page:')
    para['page'] = x
    time.sleep(0.5)
         
