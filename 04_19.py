def	get_divs():
	while True:
		try:
			divisor = float(input("피제수(a) 입력> "))
			dividend = float(input("제수(b) 입력> "))
		except:
			print("정수 또는 실수만 입력하세요.")
		else:
			break
	return ([divisor, dividend])

print("나눗셈 예외처리 a / b")
divs = get_divs()
while divs[1] == 0:
	print("0으로 나눌 수 없습니다.")
	divs = get_divs()
res = divs[0] / divs[1]
print(res)
