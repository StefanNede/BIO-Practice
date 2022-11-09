# BIO round 1 q3 2017 - 25/25
from functools import cache

@cache
def weightCombinations(numberOfItems, maxWeight, weightOfParcel):
    '''gives psbs for how many ways there are of making a weight with the number of items given and the maximum weight they can have (can cycle from 1 to this)'''
    if numberOfItems == 0 and weightOfParcel == 0:
        return 1
    elif numberOfItems <= 0 or weightOfParcel <= 0:
        return 0
    # go over each possible weight
    # the maxWeight gets set to i because otherwise we would get duplicate solutions, such as:
    # 1 1 2 and 1 2 1
    return sum([weightCombinations(numberOfItems-1, i, weightOfParcel-i) for i in range(1, maxWeight+1)])

@cache
def itemCombinations(numParcels:int,maxWeight:int, numberOfItems:int, weightOfParcel:int):
    '''gives psbs for how to distribute items across number of parcels'''
    # cache used because in the for loop at the end there can be duplicates 
    # e.g. 0 3 1 3 -> 0 3 0 3 but 1 3 1 3 -> 0 3 0 3 also
    print(numParcels,maxWeight, numberOfItems, weightOfParcel)
    if numParcels == 0 and numberOfItems == 0:
        # for example if the function before this is left with 1 parcel and 3 items
        # there is only one combination that is possible and that is when 3 items are chosen
        # when that happens the number of parcels will go down to 0, and the number of items to 0 because i in the for loop
        # at the bottom will be at 3
        # therefore we return 1 from here
        return 1
    if numParcels <= 0 or numberOfItems<=0:
        # the alternative case to the one described above
        return 0
    # for every number of items there can be in a parcel we want the possible weight combinations of the items in it
    # that are equal to the weight of the parcel
    return sum([itemCombinations(numParcels-1, maxWeight, numberOfItems-i, weightOfParcel) * weightCombinations(i, maxWeight, weightOfParcel) for i in range(1, numberOfItems+1)])

def solve(p, i, n, w):
    return itemCombinations(p,i,n,w)


p, i, n, w = [int(i) for i in input().split(' ')]
res = solve(p, i, n, w)
print(res)
