#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    h1 ={}
    h2 = {}
    for i in a:
        if i in h1:
            h1[i] += 1
        else:
            h1[i] = 1
    for j in b:
        if j in h2:
            h2[j] += 1
        else:
            h2[j] = 1
    if h1==h2:
        print(1)
    else:
        print(0)
