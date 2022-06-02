import requests
from bs4 import BeautifulSoup 

url = "https://coupang.com"
# url  = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.151 Whale/3.14.134.62 Safari/537.36"}
res = requests.get(url).text
# res.raise_for_status()
print(res)
# soup = BeautifulSoup(res.text, "lxml")
# print(res.text)