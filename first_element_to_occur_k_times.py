#code
from collections import OrderedDict

t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d = OrderedDict()
    for i in a:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1
    found = 'no'
    for key,v in d.items():
        if v==k:
            print(key)
            found = 'yes'
            break
    if found == 'no':
        print(-1)
