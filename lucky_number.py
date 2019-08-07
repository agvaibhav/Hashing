
def subsequences(inp, out, i, j):
    # base case
    if i==len(inp):
        subsequence.append(''.join(out))
        return

    # rec case
    # include current char
    out[j] = inp[i]
    subsequences(inp, out, i+1, j+1)

    # exclude current char
    out[j]=''
    subsequences(inp, out, i+1, j)


def digit_product(arr):
    pro = []
    for i in arr:
        product = 1
        for j in i:
            product = product * int(j)
        pro.append(product)
    return pro
    

if __name__=='__main__':
    t = int(input('write the no of test cases'))
    for _ in range(t):
        inp = input()
        out = ['']*(len(inp))
        subsequence = []
        subsequences(inp, out, 0, 0)
        subsequence.pop()
        product_array = digit_product(subsequence)
        lucky = {}
        count =1
        for p in product_array:
            if p in lucky:
                count = 2
                break
            else:
                lucky[p] = 1
        if count == 1:
            print(1)
        else:
            print(0)
