#python data structures
#lists
def	lst():
	questions = ['name', 'quest', 'color']
	answers = ['Kim', '파이썬', 'blue']
	#zip
	for q, a in zip(questions, answers):
		print(f"What is your {q}? It is {a}")
		#print -> f !!

	#insert(index, val)
	questions.insert(1, 'coffee')
	answers.insert(1, 'vanilla_latte')
	#index(val)
	if 'blue' in answers:
		n = answers.index('blue')
	#pop(i), remove(value)
	#extend()
	#clear()
	#count()
	#sort()
	#reverse()
	#copy()

	#slicing -> numbers[start:stop:step]
	# !! numbers[::-1] -> 리스트 역순

def	dict():
	caps = {"Korea":"Seoul", "USA":"Washington"}
	#추가
	caps["UK"] = "London"
	#삭제 - 리턴값 존재
	city = caps.pop("UK")
	#항목 방문
	for key, value in caps.items():
		print(key,":",value)
	#기타 연산
	print(caps.keys())
	print(caps.values())
	#get
	print(caps.get("Korea"))

def	tup():
	#생성. 리스트와 비슷하지만 변경이 불가능, 인덱스를 사용.
	fruits = ("apple", "banana", "grape")
	#or fruits = "apple", "banana", "grape"
	#튜플 추가 연산
	fruits += ("pear", "kiwi")
	#튜플 패킹, 언패킹
	t = ('apple', 'banana', 'grape')
	(s1, s2, s3) = t
	#enumurate()
	for i, val in enumerate(fruits):
		print(i, val)

def	set():
	#집합, 고유한 값을 저장
	nums = set([1,2,3,1,2,3])
	print(nums)
	#추가 제거
	nums.add("4")
	nums.remove("4")
	A = {"apple", "banana", "grape"}
	B = {"apple", "banana", "grape", "kiwi"}
	#부분 집합 연산
	if A < B:
		print("A는 B에 포함됨.")
	#합집합, 교집합, 차집합
	C = A | B
	C = A & B
	C = A - B

str1 = {c for c in "Hello World"}
str2 = {c for c in "How are you?"}

inter = str1 & str2
print(inter)