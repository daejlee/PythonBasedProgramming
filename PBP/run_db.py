#가독성을 위해 메뉴 선택 관련 상수 지정
ADD = 1
SEARCH = 2
DELETE = 3

def add_data():
    print("[데이터 추가]")
    new_name = input("이름을 입력하세요 > ")
    new_age = int(input("나이를 입력하세요 > "))
    new_score = float(input("점수를 입력하세요 > "))
    with open("db.txt", "a") as file:
        file.write("{}, {}, {}\n".format(new_name, new_age, new_score))
        print("추가됨.")

def search_data():
    print("[데이터 검색]")
    flag = False    #검색이 제대로 행해졌는지 체크할 플래그
    val = input("검색할 데이터의 key와 value를 입력하세요 >").split(":")
    with open("db.txt", "r") as file:
        for l in file:
            (name, age, score) = l.strip().split(", ")
            if (val[0] == "name" and val[1] == name) or \
                (val[0] == "age" and val[1] == age) or \
                (val[0] == "score" and val[1] == score):
                print("name: {}, age: {}, score: {}".format(name, age, score))
                flag = True
        if flag == False:
            print("입력한 데이터가 존재하지 않습니다.")

def delete_data():
    print("[데이터 삭제]")
    flag = False    #삭제가 행해졌는지 체크할 플래그
    del_name = input("삭제할 데이터의 이름을 입력하세요 > ")
    with open("db.txt", "r") as file:
        lines = file.readlines()    #파일 전체를 리스트 형식으로 저장
    with open("db.txt", "w") as file:
        for l in lines:
            (name, age, score) = l.strip().split(", ")
            if name != del_name:
                file.write(l)
            else:
                flag = True
    if flag == False:
        print("입력한 데이터가 존재하지 않습니다.")
    else:
        print("삭제 완료.")

print("간단한 데이터베이스 만들기")
while True:
    print("\n메뉴\n1. 데이터 추가\n2. 데이터 검색\n3. 데이터 삭제")
    menu = int(input("메뉴를 입력하세요 > "))
    if menu == ADD:
        add_data()
    elif menu == SEARCH:
        search_data()
    elif menu == DELETE:
        delete_data()