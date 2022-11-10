# BIO final fibonacci's revenge - full marks
def solve(s1:str,s2:str,i:int) -> str:
    prev1 = s2
    prev2 = s1
    res = ''
    i -= (len(prev1)+len(prev2))
    while True:
        prev2, prev1 = prev1, prev2+prev1
        l = len(prev1)
        if l >= i:
            res = prev1[i-1] 
            break
        else:
            i -= l
    return res

s1, s2, i = input(), input(), int(input())
print(solve(s1, s2, i))