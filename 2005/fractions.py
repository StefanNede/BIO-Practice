# bio round 1 q1 - 24/24

def solve(f:float): 
    numerator = round(f * 10_000)
    denominator = int(10_000)
    print(numerator, denominator)
    hcf = 1
    # simplify numerator and denominator by finding HCF
    for i in range(2, (numerator//2)+1):
        if numerator%i == 0 and denominator%i == 0: hcf = i
    if denominator%numerator == 0: hcf = numerator

    return f"{int(numerator/hcf)} / {int(denominator/hcf)}"

f = float(input())
print(solve(f))