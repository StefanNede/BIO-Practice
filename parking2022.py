# PARKING - BIO round 1 2022 q3
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
inp = input().split(" ")
parked, index = inp[0], int(inp[1])


def noLaterCars(parked, ltr, index, indexOfLetter):
    for i in range(index+1, indexOfLetter):
        #print(parked[i], ltr)
        if parked[i] > ltr:
            return False
    return True

#print(noLaterCars('dacb', 'a', 0))

# returns the indexes that the car at the index we gave could have preferred
def getPositions(parked, indexOfLetter):
    '''
    e.g. cabd ---- what are the places that car b could prefer
    either position of index 1 or 2
   
    therefore the code has to go over each parked space and if the car parked there
    is closer to the beginning of the alphabet then it got there first so that space
    could have been preferred by our current car (the index of which is passed to the function)
   
    however a car can't have preferred an already taken spot if any of the spots following it
    are lower in the alphabet than it is because it would've taken those spots but it didn't
    e.g. dacb for b:
    b can't have preferred position B because it would've then gone to position C but it
    didn't and it was open when car b arrived
    '''
    possibleIndexes = []
    if parked[indexOfLetter] == 'a':
        return [indexOfLetter]
    for j in range(indexOfLetter+1):
        #print(parked, parked[indexOfLetter], j)
        if parked[j] <= parked[indexOfLetter] and noLaterCars(parked, parked[indexOfLetter], j, indexOfLetter):
            #print(parked, parked[indexOfLetter], j)
            possibleIndexes.append(j)
    #print(parked[indexOfLetter], possibleIndexes)
    return possibleIndexes
#print(getPositions('cabd', 2))

psbs = []
counter = 1
def getParked(parked, psb = [''] * len(parked), i = 0):
    global psbs, counter
    #print(psb, psbs)
    if i >= len(parked):
        # once we have gone over each car
        # print(psb, psbs)
        if counter == index:
            #print(psb, counter)
            print(''.join(psb))
        counter += 1
        #psbs.append(psb)
        return
        # print(psbs)
    indexOfLetter = parked.index(alpha[i].lower()) # gives the position the car is when parked
    #print(alpha[i].lower(), indexOfLetter, alpha[indexOfLetter])
    #print(indexOfLetter)
    possiblePositions = getPositions(parked, indexOfLetter)
    #print(possiblePositions)
    for position in possiblePositions:
        psb[i] = alpha[position]
        getParked(parked, psb, i+1)
    #return
   

def test():
    pass

getParked(parked)
#print(res)
#print(psbs)
#print(''.join(psbs[index-1]))