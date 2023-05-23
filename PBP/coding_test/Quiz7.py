dict_lst = [
    {'name': '민수', 'age': 24, 'score': 3.9},
    {'name': '영희', 'age': 16, 'score': 3.1},
    {'name': '철수', 'age': 21, 'score': 4.3},
    {'name': '길동', 'age': 29, 'score': 4.1},
]
print("간단한 데이터베이스 검색 기능 구현")
print("[데이터 검색]")
search_val = input("검색할 데이터의 이름을 입력하세요 >")
for item in dict_lst:
    if item['name'] == search_val:
        print(item)
