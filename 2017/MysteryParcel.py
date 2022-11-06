from functools import lru_cache

def solve(p, i, n, w):
    '''
    this question is asking the number of ways to make w from p different items 
    where items can weight between 1 and i 
    and where each parcel needs to contain n items 
    e.g. if w is 3 and p is 2 and n is 4 then 1,2 and 3 cannot make up a parcel because there would only be 3 items in it 
    '''
    if p == 1:
        res = 0
        if i == 1:  
            # then for each value of i all the items have to weigh this
            for j in range(1, i+1):
                weightsAdded = j*n
                if weightsAdded == w:
                    res += 1
        return res


p, i, n, w = [int(i) for i in input().split(' ')]
res = solve(p, i, n, w)
print(res)