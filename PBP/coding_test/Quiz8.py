ADD = 1
SEARCH = 2
DELETE = 3
dict_lst = [
    {'name': '민수', 'age': 24, 'score': 3.9},
    {'name': '영희', 'age': 16, 'score': 3.1},
    {'name': '철수', 'age': 21, 'score': 4.3},
    {'name': '길동', 'age': 29, 'score': 4.1},
]
while True:
    print("간단한 데이터베이스 만들기\n메뉴\n1. 데이터 추가\n2. 데이터 검색\n3. 데이터 삭제")
    SELECT = int(input("메뉴를 선택하세요 > "))
    if SELECT == ADD:
        print("[데이터 추가]")
        new_dict = {}
        new_dict['name'] = input("이름")
        new_dict['age'] = int(input("나이"))
        new_dict['score'] = float(input("성적"))
        dict_lst.append(new_dict)
        print("추가됨.")
    elif SELECT == SEARCH:
        print("[데이터 검색]")
        search = input("검색할 데이터의 key와 value를 입력하세요 >").split(":")
        for item in dict_lst:
            if item[search[0]] == search[1]:
                print(item)
    elif SELECT == DELETE:
        print("[데이터 삭제]")
        search = input("삭제할 데이터의 이름을 입력하세요 >")
        for i in range(len(dict_lst)):
            if dict_lst[i]['name'] == search:
                del dict_lst[i]
                break
        print("삭제됨")
#리스트 관련 메소드 숙달. ex) del(a[i]), a.pop(i), slice (a=[1:])..