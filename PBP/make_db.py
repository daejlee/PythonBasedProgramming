#CSV형식으로 기본 DB 생성.
with open("db.txt", "w") as file:
    file.write("{}, {}, {}\n".format("name", "age", "score"))
    file.write("{}, {}, {}\n".format("철수", 21, 4.3))
    file.write("{}, {}, {}\n".format("영희", 16, 3.1))
    file.write("{}, {}, {}\n".format("민수", 24, 3.9))
    file.write("{}, {}, {}\n".format("길동", 29, 4.1))
