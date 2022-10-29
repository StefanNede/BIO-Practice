# 2018 bio round 1 q1 - 22/26 because of some weird rounding stuff idfk
# q1b) 5 - 2 marks
# q1c) 96 49 - 3 marks
import math

# A full mark solution I looked at just works with them all *100 so you can just
# use math.ceil and then at the end divides the answer by 100 to get the decimal
# idfk how python rounds but screw them 
def solution(interest:int, repayments:int) -> float:
    # math.ceil always rounds up
    debt = 100
    amountRepaid:float = 0.0

    while debt > 0:
        interestAdded = (interest/100) * debt
        debt += math.ceil(interestAdded*100)/100  
        repaymentToBeAdded = (repayments/100) * debt
        repaymentToBeAdded = math.ceil(repaymentToBeAdded*100)/100
        amountToBeRepaid = min(max(repaymentToBeAdded,50), debt)
        # print(debt, amountToBeRepaid)
        
        amountRepaid += amountToBeRepaid
        debt -= amountToBeRepaid

    return math.ceil(amountRepaid*100)/100
        

i, r = [int(j) for j in input().split(' ')]

print(solution(i,r))