# 2021 round 1 q1 - 24/24
def isPat(string): 
    if len(string) == 1: 
        return True 
    else: 
        for i in range(1,len(string)): # explained on line 21 
            substring1 = string[:i] 
            substring2 = string[i:] 
            if min(substring1) > max(substring2): 
                if isPat(substring1[::-1]) and isPat(substring2[::-1]): 
                    return True 
        return False 

s1, s2 = input().split(' ') 
for test in [s1,s2,s1+s2]: 
    print("YES" if isPat(test) else "NO") 