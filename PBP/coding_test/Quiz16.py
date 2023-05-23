class MyMath:
    def get_divs(self, num):
        lst = []
        for i in range(1, num):
            if num % i == 0:
                lst.append(i)
        return lst

    def is_complete_number(self, num):
        if sum(self.get_divs(num)) == num:
            return True
        return False

m = MyMath()
limit = int(input("숫자를 입력하시오: "))
for i in range(limit):
    if m.is_complete_number(i):
        print(i)