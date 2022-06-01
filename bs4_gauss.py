import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

ratings = soup.find_all("div", attrs={"class":"rating_type"})

total_rate = 0
for rating in ratings:
    rate = rating.find("strong").get_text()
    print(rate)
    total_rate += float(rate)
    
print("전체 점수 : ", total_rate)
print("평균 점수 : ", total_rate / len(ratings))
