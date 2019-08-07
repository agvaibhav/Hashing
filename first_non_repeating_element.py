#code
from collections import OrderedDict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = OrderedDict()
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    res = None
    for k,v in d.items():
        if v == 1:
            res = k
            break
    if res is None:
        print(0)
    else:
        print(res)
