# BIO round 1 q3 - 17/23

res = []

# dfs solution
def solveDFS(s, nums):
    global res
    if s == 0:
        res.append(nums)
        return
    else:
        for i in range(1, min(s, 9)+1):
            solve(s-i, nums+str(i))

def getNumStarting(start, s):
    '''
    returns the number of possibilities starting with a string
    e.g. '11' represents it starting with 1 1
    '''
    pass

# fast solution
def solve(s, nums):
    '''
    use a similar strat to modern art:
    - need to get the number of possibilities starting with something
    - then ammend s accordingly
    '''
    return 

s, n = [int(i) for i in input().split(' ')]
#solveDFS(s, '')
#print(' '.join(res[n-1]))