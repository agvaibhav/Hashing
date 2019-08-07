#code
'''
ques
Given an array containing N words consisting of lowercase characters.
Your task is to find the most frequent word in the array.
If multiple words have same frequency, then print the word whose
first occurence occurs last in the array as compared to the other strings
with same frequency.
'''

from collections import OrderedDict

t = int(input())
for _ in range(t):
    n = int(input())
    words = input().split()
    d =  OrderedDict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    max = 0
    for k,v in d.items():
        if v>max:
            max = v
            res = k
        elif v == max:
            res = k
    print(res)
