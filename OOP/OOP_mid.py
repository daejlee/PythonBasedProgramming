list1 = [int(item) for item in input().split((","))]

res_list = []

val = 0

for item in list1:
    val += item
    res_list.append(val)

print(res_list)

R, C = [int(item) for item in input().split(",")]
matrix = []
matrix = [[int(input()) for i in range(C)] for j in range(R)]
temp = 0
for i in range(R):
    for k in range(C):
        if i > k:
            temp = matrix[i][k]
            matrix[i][k] = matrix[k][i]
            matrix[k][i] = temp

print(matrix)

x1, y1, x2, y2 = [int(item) for item in input().split(",")]

def dis(x1, y1, x2, y2):
    out = 0
    x_offset = x1 - x2
    y_offset = y1 - y2
    out = (x_offset * x_offset + y_offset * y_offset) ** (1/2) #** 제곱 연산자 기억
    return out

print("Distance:", dis(x1, y1, x2, y2))

num = int(input())
flag = 0
for i in range(2, num):
    if num % i == 0:
        print("Not Prime.")
        flag = 1
        break
if num == 1:
    print("Not Prime")
elif flag == 0:
    print("Prime.")

src = str(input())

def compact(src):
    if src == '':
        return src
    out = src[0]
    if len(src) == 1:
        out += '1'
        return out
    prev_c = src[0]
    cnt = 0
    for c in src:
        if prev_c != c:
            out += str(cnt)
            out += c
            cnt = 1
        else:
            cnt += 1
        prev_c = c
    out += str(cnt)
    return out

print("{}".format(compact(src)))

2
4
2
1
2
1
2
3, 5 -> 첨자로 접근하지 않고, key, value로 접근한다.
2   #3
1 #strip과 rstrip의 차이는..1, 2 둘 다 가능
