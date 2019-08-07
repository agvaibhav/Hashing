#code
t = int(input())
for _ in range(t):
    m,n = list(map(int,input().split()))
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    res = 'Yes'
    for i in a2:
        if i in a1:
            continue
        else:
            res = 'No'
    print(res)
