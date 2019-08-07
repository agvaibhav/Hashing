#code
'''
ques
Given a string str and another string patt.
Find the character in patt that is present at the minimum index in str.
If no character of patt is present in str then print ‘No character present’.
'''

t = int(input())
for _ in range(t):
    string = input()
    patt = input()
    d = {}
    for i in range(len(string)):
        if string[i] not in d:
            d[string[i]] = i
    minindex = float('inf')
    for char in patt:
        if char in d:
            if d[char] < minindex:
                minindex = d[char]
                res = char
    if res is not None:
        print(res)
    else:
        print('$')
