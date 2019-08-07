#code
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    minele = min(a)
    maxele = max(a)
    h = ['No'] * (maxele + 1)
    for i in a:
        h[i] = 'Yes'
    for j in range(minele,maxele+1):
        if h[j]=='Yes':
            continue
        else:
            break
    print(h[j])
