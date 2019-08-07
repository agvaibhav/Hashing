#code
t = int(input())
for _ in range(t):
    s = input()
    char = {}
    for i in range(len(s)):
        if s[i] in char:
            char[s[i]] += 1
        else:
            char[s[i]] = 1
    count = 1
    for k,v in char.items():
        if v>count:
            count = 2
            break
    if count ==1:
        print(1)
    else:
        print(0)
