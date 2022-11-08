def solve(n):
    '''gets number of discrete integer partitions for a number n'''
    # summands = [0...n]
    # operands = [0...n]
    if n <= 1: return 1
    memo = [[0]*(n+1)]*(n+1)
    memo[0] = [1] + [0]*(n)
    memo[1] = [1]*(n+1)
    for i in range(2, len(memo)):
        summands = [k for k in range(i+1)]
        for j in range(len(memo[i])):
            operand = j
            if operand < summands[-1]:
                memo[i][j] = memo[i-1][j]
            else:
                combsExcluding = memo[i-1][j]
                combsIncluding = memo[i][operand-summands[-1]]
                memo[i][j] = combsExcluding + combsIncluding
    return memo[-1][-1]


n = int(input())
print(solve(n))