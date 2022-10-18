import time
#naive solution is to iterate over each value with while loop and check if palindrome

# current errors:
# - doesn't work if middle number is 9 - 1 is isn't carried over
# - doesn't work if input is 2 digit multiple of 10


def leftVright(left, right):
    # the incoming values are going to be lists
    left = ''.join([str(i) for i in left])
    right = ''.join([str(i) for i in right])
    #print(left, right)
    if int(right[::-1]) > int(left):
        return True
    return False

def getPal(num):
    
    '''
    start in the middle and if the right side is greater than the left side reversed
    then increment the index by 1 and now you can switch each corresponding case
    to be the left one
    e.g. 3210124 -> 321 1 124 -> 321 1 123
    
    9 -> 0 and increment index either side by 1
    '''
    if len(num) == 1 and num[0] < 9:
        return num[0]
    
    # for loop to go from middle to start (index 0)
    middleIndex = (len(num)-1)//2
    tailMiddleIndex = -1-middleIndex
    if num[tailMiddleIndex] >= num[middleIndex] or leftVright(num[:middleIndex], num[tailMiddleIndex+1:]):
        num[middleIndex] += 1
        num[tailMiddleIndex] = num[middleIndex]
        
    for i in range((len(num)-1//2)):
        tailP = -1-i
        num[tailP] = num[i]
    return int(''.join([str(i) for i in num]))


num = int(input())
num += 1
num = [int(x) for x in str(num)]
print(getPal(num))