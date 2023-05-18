class MyMath:
	#인자로 받은 숫자의 약수 리스트를 구하는 함수
	def get_measure(self, val):
		measures = []
		for i in range(1, val):
			if val % i == 0:
				measures.append(i)
		return measures
	#인자로 받은 숫자가 완전수인지 판별하는 함수
	def is_perfect_number(self, val):
		if (sum(self.get_measure(val)) == val):
			return True
		return False
	#인자로 받은 숫자 N 이하의 모든 완전수를 출력하는 함수
	def print_all_perfect_number(self, val):
		buf_lst = []
		for i in range(1, val):
			if self.is_perfect_number(i):
				buf_lst.append(i)
		print (buf_lst)

m = MyMath()
m.print_all_perfect_number(int(input("자연수를 입력하세요> ")))