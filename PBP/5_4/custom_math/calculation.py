def get_common_multiples():
    vals = input("두개의 숫자를 입력하시오(a, b) >").split(",")
    vals[0] = int(vals[0])
    vals[1] = int(vals[1])
    lcm = get_lcm(vals)
    gcd = get_gcd(vals)
    print(f'최대공약수: {gcd}')
    print(f'최소공배수: {lcm}')

def get_lcm(vals):
    if vals[0] % vals[1] == 0:
        return vals[0]
    elif vals[1] % vals[0] == 0:
        return (vals[1])
    else:
        if vals[0] > vals[1]:
            bigger = vals[0]
            smaller = vals[1]
        else:
            bigger = vals[1]
            smaller = vals[0]
        cnt = 2
        while True:
            if bigger * cnt % smaller == 0:
                return bigger * cnt
            cnt += 1

def get_gcd(vals):
    cnt = 1
    ret = 1
    limit = vals[0] if vals[0] < vals[1] else vals[1]
    while cnt <= limit:
        if vals[0] % cnt == 0 and vals[1] % cnt == 0:
            ret = cnt
        cnt += 1
    return ret