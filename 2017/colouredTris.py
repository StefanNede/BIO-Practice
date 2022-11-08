# 2017 bio round 1 q1 - 23/23

psbs = {'RR':'R',
        'RB':'G',
        'RG':'B',
        'BB':'B',
        'BR':'G',
        'BG':'R',
        'GG':'G',
        'GR':'B',
        'GB':'R'}

def solve(n):
    temp:str = ''
    while len(n) > 1:
        for i in range(len(n)-1):
            pair = n[i:i+2]
            lower = psbs[pair]
            temp += lower
        n = temp
        temp = ''
    return n

sRow = input()
print(solve(sRow))