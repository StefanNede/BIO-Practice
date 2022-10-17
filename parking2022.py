alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inp = input().split(" ")
parked, index = inp[0], int(inp[1])

psbs = []
def getParked(parked, psb = [''] * len(parked), i = 0):
    global psbs
    print(psb, psbs)
    if i >= len(parked):
        # once we have gone over each car 
        return psb
    
    indexOfLetter = parked.index(alpha[i].lower())
    print(alpha[i].lower(), indexOfLetter, alpha[indexOfLetter])
    
    if i == 0:
        psb[0] = alpha[indexOfLetter]
    for j in range(indexOfLetter+1):
        # find how many positions before where it is are currently occupied
        # for each position add them to a psb and go down that branch
        if psb[j] != '':
            psb[indexOfLetter] = alpha[j]
            return psbs + [getParked(parked, psb, i+1)]
        
    return psbs
psbs = getParked(parked)
print(psbs)
# print(''.join(psbs[index-1]))    

# psbs = getParked(parked)
# print(psbs)
# print(psbs[index])
