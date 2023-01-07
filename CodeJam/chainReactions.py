from collections import deque, defaultdict

def getInitiators(fun, points, abysPointers):
    # checked = [i for i in range(len(points) - len(abysPointers))] # the pointers left to check
    init = [i for i in range(len(points)) if points[i]-1 in abysPointers]
    # check if anything more points to the elements in init
    # if so ammend init

    return init


def solve(fun, points):
    '''
    get the initiators
    first idea - DFS the possibilities with them
    second idea - BFS psbs
    third idea - some type of heuristic search 
    '''
    # the indexes of the ones that point to abysses
    # can't store their values because there might be abysPointers of the same value
    abysPointers = [i for i in range(len(points)) if points[i] == 0] 
    initiators = getInitiators(fun, points, abysPointers)
    print(initiators)
    return 0

t = int(input())
for i in range(t):
    n = int(input())
    fun = [int(a) for a in input().split(" ")]
    points = [int(b) for b in input().split(" ")] # not 0 indexed

    print(f"Case #{i+1}: {solve(fun,points)}")