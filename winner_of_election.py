#code
t = int(input())
for _ in range(t):
    n = int(input())
    cand = input().split()
    votes = {}
    for i in cand:
        if i in votes:
            votes[i] += 1
        else:
            votes[i] = 1
    res = []
    max = 0
    for k,v in votes.items():
        if v>max:
            while len(res)!=0:
                res.pop()
            max = v
            res.append([k,v])
        if v==max:
            res.append([k,v])
    res.sort()
    print(*res[0])
