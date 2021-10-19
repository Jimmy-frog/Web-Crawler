import requests
import prettytable
from bs4 import BeautifulSoup
from datetime import datetime

data = datetime.now()

para = {'ID': data}
     
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

url ="https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html"


col = ["city","temp"]

table =prettytable.PrettyTable(col, encoding="utf-8")
table.align["city"] = 'l'
table.align["temp"] = 'r'   
res = requests.get(url,params = para,headers=header)
soup = BeautifulSoup(res.text,"html.parser")

city = soup.find_all('th')
temp = soup.find_all('span',class_='tem-C is-active')
to = zip(city,temp)
for i ,j in to:
    table.add_row((i.text,j.text))
    
print(table)
