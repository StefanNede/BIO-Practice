# success
import string
alpha = list(string.ascii_lowercase)
n = int(input())
for i in range(n):
    length = int(input())
    s = list(input())
    s.sort()
    print(alpha.index(s[-1])+1)