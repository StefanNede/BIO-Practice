# bio round 1 q3 -25/25
from functools import lru_cache 

@lru_cache(maxsize=None)
def solve(scenes):
    finished = True
    scenes = list(scenes)
    scenes = [list(s) for s in scenes]
    # print(scenes)
    for actor in scenes:
        totalScenes, scenesDone = actor
        totalScenes = actor[0]
        scenesDone = actor[1]
        if totalScenes < scenesDone: 
            return 0
        elif totalScenes > scenesDone:
            finished = False
    if finished: 
        return 1

    res = 0
    for i in range(len(scenes)):
        canChange = True
        actor = scenes[i]
        # look at all previous actors (senior actors)
        for seniorActor in scenes[:i]:
            # the original actor can change if they have done less scenes than 
            # all their senior actors
            if seniorActor[1] <= actor[1]: 
                canChange = False
        if canChange:
            copyScenes = []
            # if i write copyScenes = scenes, when i change copyScenes it also changes scenes
            # so I need to do this wonderful code
            for j in range(len(scenes)):
                inter = []
                for k in range(len(scenes[j])):
                    inter.append(scenes[j][k])
                copyScenes.append(inter) 
            copyScenes[i][1] += 1
            # print(copyScenes, scenes)
            # print(copyScenes)
            # convert back into hashable tuple
            copyScenes = [tuple(s) for s in copyScenes]
            res += solve(tuple(copyScenes))
    return res

actors = int(input())
s = [int(i) for i in input().split(" ")]
scenes = []
for i in s:
    scenes.append((i, 0))
# need to use tuples as they are hashable
print(solve(tuple(scenes)))