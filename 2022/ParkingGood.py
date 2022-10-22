# Mr Johnson's solution commented 
import time

EMPTY = "_"


def FindParkedCar(finalArrangement, car):
    try:
        return finalArrangement.index(car.lower())
    except:
        # this happens when the algorithm has gone through all cars 
        return None


def GetListHidden(finalArrangement,carsAlreadyParked):
    '''
    returns a list of the possible preferred positions for each car
    e.g. cabd returns [['B'], ['B', 'C'], ['A'], ['A', 'B', 'C', 'D']]
    '''
    numEmptySpaces = carsAlreadyParked.count(EMPTY)
    nonEmptySpaces = len(carsAlreadyParked) - numEmptySpaces
    
    if numEmptySpaces == 0:
        return None

    possiblePreferences = [] # holds all the preferences a car could have
    carToPark = chr(65 + nonEmptySpaces)
    # after the carsAlreadyParked is full we want to go past getting arrangements therefore
    # whereIsCarParkedIndx returns None
    whereIsCarParkedIndx = FindParkedCar(finalArrangement, carToPark)
    
    if whereIsCarParkedIndx != None:
        carsAlreadyParked[whereIsCarParkedIndx] = carToPark
        spaceIndex = whereIsCarParkedIndx
        while spaceIndex > -1 and carsAlreadyParked[spaceIndex] != EMPTY:
            possiblePreferences.append(chr(65 + spaceIndex)) # returns parking space the car is in e.g. for a in cabd returns B
            spaceIndex -= 1
        furtherPreferences = GetListHidden(finalArrangement,carsAlreadyParked)
    
    # furtherPreferences will hold the preferences of all the cars in alphabetical order following the one that is currently being looked at e.g.
    # for cabd:
    # currently looking at a which has preference of 'B' then foro b,c,d these are preferences:
    # [['B', 'C'], ['A'], ['A', 'B', 'C', 'D']]
    
    
    # arrive here after all the cars have been looked at once, and
    # due to recursive stack, will go backwards to the first car - which is what we really want to see
    # because when the carToPark is a then the furtherPreferences will contain the preferences for each car
    
    allPreferences = []
    allPreferences.append(sorted(possiblePreferences))
    
    if furtherPreferences != None:
        for pref in furtherPreferences:
            allPreferences.append(sorted(pref))
            
    return allPreferences
        

def ExtractResultAtPos(results, pos):
    '''
    this shit giga brain
    '''
    
    finalStr = ""
    
    # go backward through preferences
    for resultIndex in range(len(results)-1,-1,-1):
        result = results[resultIndex]
        rem = pos % len(result)
        #print(resultIndex, result, rem)
        finalStr += result[rem]
        if pos != 0:
            pos = (pos - rem) // len(result)
            
    return finalStr[::-1]


def GetList(finalArrangement,pos):
    '''
    for cabd
    results = [['B'], ['B', 'C'], ['A'], ['A', 'B', 'C', 'D']], corresponding to possible preferred positions for cars a,b,c,d
    specificResult = []
    '''
    pos -= 1 # to get it as an index (0 indexing)
    carsAlreadyParked = [EMPTY] * len(finalArrangement)
    results = GetListHidden(finalArrangement,carsAlreadyParked[:]) # returns the possible preferred positions for each car in array\
    
    specificResult = ExtractResultAtPos(results, pos)
    
    return specificResult


inputs = [  ["cabd",5,"BCAA"],
            ["a",1,"A"],
            ["dacb",2,"BDCA"],
            ["fedcba",1,"FEDCBA"],
            ["badcef",90,"BADCEF"],
            ["dabcefgh",5000,"BBDAEFBH"],
            ["hefbdciajg",125,"HDFDBCJAGH"],
            ["bcadefghi",49999,"CAADBDBDD"],
            ["bcdefghijak",1000000,"JAABCAACFAA"],
            ["acbdefghijk",12345678,"ACBDCAEGDED"],
            ["abcdeghfklijnmop",2800700600,"ABCDDHEDKKAANFMH"],
            ["abcdefghijklmnop",12345678901234,"ABACAEFHBFJAMLCB"] ]


question = inputs[0]
result = GetList(question[0], question[1])
#print(result)


#layout = 'Input: {:<30}\tTarget: {:<18}\tCode result:{:<18}\t\tTime:{:>7.2f}'
layout = '{:<35}{:<24}{:<18}{:<7}{:<5}'
print(layout.format ("Input","Target","Code result","Time","Correct?"))
for question in inputs:
    start = time.time()
    result = GetList(question[0],question[1])
    if question[2].strip() == result.strip():
        correct = "True"
    else:
        correct = "False"
    print(layout.format (question[0] + ", " + str(question[1]), 
                        question[2], 
                        result, 
                        time.time() - start,
                        correct))
