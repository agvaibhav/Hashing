#code
def is_digit_set(digit):
    set = ['1','2','3']
    for i in digit:
        if i in set:
            continue
        else:
            return False
    return True
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    res = []
    for i in a:
        if is_digit_set(i):
            res.append(int(i))
    if len(res)==0:
        print(-1)
    else:
        res.sort()
        print(*res)
