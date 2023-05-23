print("나눗셈 예외처리 a / b")
while True:
    try:
        a = float(input("피제수(a) 입력> "))
        b = float(input("제수(b) 입력> "))
        break
    except:
        print("정수 혹은 실수를 입력하세요")
try:
    ret = a / b
    print("{} / {} = {:g}".format(a, b, ret))
except:
    print("0으로 나눌 수 없습니다.")

#try, except 구문 문법 / format()메소드 사용