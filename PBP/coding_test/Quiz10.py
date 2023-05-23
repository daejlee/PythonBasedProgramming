f = open("./Quiz10_db.txt", "w")
f.write("name,age,score\n")
f.write("철수,21,4.3\n")
f.write("영희,16,3.1\n")
f.write("민수,24,3.9\n")
f.write("길동,29,4.1\n")
f.close()

ADD = 1
SEARCH = 2
DELETE = 3

while True:
    print("간단한 데이터베이스 만들기\n메뉴\n1. 데이터 추가\n2. 데이터 검색\n3. 데이터 삭제")
    SELECT = int(input("메뉴를 선택하세요 > "))
    if SELECT == ADD:
        print("[데이터 추가]")
        f = open("./Quiz10_db.txt", "w")
        f.write(input("이름")+ ',' + input("나이") + ',' + input("성적"))
        f.close()
        print("추가됨.")
    elif SELECT == SEARCH:
        print("[데이터 검색]")
        search = input("검색할 데이터의 key와 value를 입력하세요 >").split(":")
        f = open("./Quiz10_db.txt", "r")
        buf_lst = f.readlines()
        for line in buf_lst:
            lst = line.split(",")
            if search[0] == "name" and search[1] == lst[0] or \
                    search[0] == "age" and search[1] == lst[1] or \
                    search[0] == "score" and search[1] == lst[2]:
                print(line)
        f.close()
    elif SELECT == DELETE:
        print("[데이터 삭제]")
        search = input("삭제할 데이터의 이름을 입력하세요 >")
        f = open("./Quiz10_db.txt", "r")
        buf_lst = f.readlines()
        f.close()
        f = open("./Quiz10_db.txt", "w")
        for line in buf_lst:
            lst = line.split(",")
            if search == lst[0]:
                print("삭제됨")
            else:
                f.write(line)
        f.close()
