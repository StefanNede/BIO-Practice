# BIO round 1 q1 - 23/23

def solve(p):
    # default values
    beforeLeft = [1,0]
    beforeRight = [0,1]

    for letter in p:
        overall = [beforeLeft[0]+beforeRight[0],beforeLeft[1]+beforeRight[1]]
        if letter == 'L':
            beforeLeft = overall
        else:
            beforeRight = overall
     
    # need to add the final beforeR or beforeL that we got by going over the final letter
    overall = [beforeLeft[0]+beforeRight[0],beforeLeft[1]+beforeRight[1]]

    return overall

p = input()
res = solve(p)
print(f"{res[0]} / {res[1]}")