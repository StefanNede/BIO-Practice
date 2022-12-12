# full marks
from functools import lru_cache

@lru_cache(maxsize=None)
def permuteItems(maxWeight, weight, items):
    # permutes the weight of the items in each parcel
    if weight == 0 and items == 0: return 1
    elif weight <= 0 or items <= 0: return 0
    
    res = 0
    for i in range(1, maxWeight+1):
        # set max weight to i because solutions such as 1 3 and 3 1 would otherwise
        # be counted twice - by doing this only one solution will be found for each pair
        # which is the one that goes bigger smaller (e.g. 3 1)
        res += permuteItems(i, weight-i, items-1)
    return res

@lru_cache(maxsize=None)
def permuteParcels(parcels, maxWeight, items, weight):
    # permutes the number of items in each parcel
    if parcels == 0 and items == 0: return 1
    elif parcels <= 0 or items <= 0: return 0

    res = 0
    for i in range(1, items+1):
        res += permuteParcels(parcels-1, maxWeight, items-i, weight)*permuteItems(maxWeight, weight, i)
    return res
  
parcels, maxWeight, items, weight = [int(i) for i in input().split(" ")]
print(permuteParcels(parcels, maxWeight, items, weight))