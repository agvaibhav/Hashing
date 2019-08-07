#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    found = 'no'
    for k,v in d.items():
        if v%2!=0:
            print(k)
            found = 'yes'
            break
    if found == 'no':
        print(0)
