import requests
# res = requests.get("https://google.com")
res = requests.get("https://nadocoding.tistory.com")
print("응답코드 :", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겨습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status()
print("웹 스크랩핑을 집행합니다.")

print(len(res.text))
print(res.text)

# with open("mygoogle.html", "w", encoding="utf-8") as f:
#     f.write(res.text)