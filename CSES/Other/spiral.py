def main(y:int, x:int) -> int:
    '''
    1, 3, 7, 13, 21 
    steps: 2, 4, 6, 8 = n**2 
    difference: 0, -1, -2, -3 = -n+1 
    
    if upper is odd, the numbers increase upwards, and decrease to the left
    if upper is even, the numbers decrease upwards, and increase to the left
    '''
    res = 0 
    upper = max(y,x)
    m_upper = upper**2 - upper + 1 
    res = m_upper
    if upper%2 == 1:
        y_change = abs(y-upper)
        x_change = abs(x-upper)
        res -= x_change
        res += y_change
    else:
        y_change = abs(y-upper)
        x_change = abs(x-upper)
        res += x_change
        res -= y_change
    return res

n = int(input())
for i in range(n):
    inp = input().split()
    y, x = int(inp[0]), int(inp[1])
    print(main(y,x)) 
