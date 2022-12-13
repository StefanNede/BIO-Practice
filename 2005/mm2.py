# full marks
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(scenes):
    # convert back into lists so we can change the elements
    scen = []
    for s in scenes:
        scen.append(list(s))
    
    # base case
    finished = True
    for actor in scen:
        if actor[1] > actor[0]: return 0
        if actor[1] < actor[0]:
            finished = False
    if finished:
        return 1
    
    res = 0
    # look at all the more senior actors in order and then make a move
    for i in range(len(scen)):
        canChange = True
        lessSenior = scen[i]
        for senior in scen[:i]:
            if senior[1] <= lessSenior[1]:
                canChange = False
        if canChange:
            # make a copy of the scenes list
            copyScenes = []
            for j in range(len(scen)):
                inter = []
                for k in range(len(scen[j])):
                    inter.append(scen[j][k])
                copyScenes.append(inter)
                
            # if more senior has done more than a less senior one
            # then less senior can do a scene
            copyScenes[i][1] += 1

            # convert back into tuple
            scenes = []
            for s in copyScenes:
                scenes.append(tuple(s))
            scenes = tuple(scenes)
            res += solve(scenes)
    return res

actors = int(input())
s = [int(i) for i in input().split(" ")]
scenes = []
# store scenes in format [totalScenes, scenesDone]
for i in range(len(s)):
    scenes.append((s[i],0))

print(solve(tuple(scenes)))