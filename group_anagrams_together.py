#code
'''
ques
Given an array of words, print the count of all anagrams together in sorted order (increasing order of counts).
For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then grouped anagrams are “(dog, god) (cat, tac, act)”. So the output will be 2 3.
'''

def is_anagram(word1,word2):
    Word1 = []
    Word2 = []    
    for i in word1:
        Word1.append(i)
    for i in word2:
        Word2.append(i)
    for i in Word1:
        if i in Word2:
            Word2.remove(i)
        else:
            return False
    if i==Word1[-1] and len(Word2) == 0:
        return True
    else:
        return False
        
t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    d = {arr[0]:1}
    for i in arr[1:]:
        found = 'no'
        for k,v in d.items():
            if is_anagram(k,i):
                d[k] += 1
                found = 'yes'
                break
        if found == 'no':
            d[i] = 1
    d = sorted(d.items(), key=lambda x: x[1])
    for item in d:
        print(item[1], end = ' ')
    print()
