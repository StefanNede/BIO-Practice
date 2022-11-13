# gets the longest and non overlapping repeating substring
# O(nlogn) - uses dp
from collections import defaultdict
import time 

def nonDP(string):
    # O(n^2) but much slower
    substrings = defaultdict(lambda:0)
    resLength = 0
    resString = ""
    for i in range(len(string)+1):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            substrings[substring] += 1
            if substrings[substring] > 1 and (j-i) > resLength:
                resLength = (j-i)
                resString = substring
    
    return resString

def dp(string):
    # dp - currently in O(n^2) but can be done in O(nlogn) with suffix array
    n = len(string)
    LCSRe = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    res = "" # To store result
    res_length = 0 # To store length of result
 
    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
             
            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if (string[i - 1] == string[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
 
                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
                 
            else:
                LCSRe[i][j] = 0
 
    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if (res_length > 0):
        for i in range(index - res_length + 1,
                                    index + 1):
            res = res + string[i - 1]
 
    return res

string = input()
start = time.time()
res = dp(string)
end = time.time()
print(res, end-start)

start = time.time()
res = nonDP(string)
end = time.time()
print(res, end-start)