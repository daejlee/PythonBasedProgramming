print("계산기 시작")
res = float(input("> "))
for i in range(3):
    elem = input("> ")
    if elem == "":
        break;
    if elem == "+":
        res += float(input("> "))
    elif elem == "*":
        res *= float(input("> "))
    elif elem == "/":
        res /= float(input("> "))
if res == int(res):
    print(f"계산 결과 {int(res)}입니다.")
else:
    print(f"계산 결과 {res:.2f}입니다.")
#f-string 사용방법. 주목