# 23/23
count = 0
def solve(word):
    global count
    endPoint = (len(word)//2)+1
    for i in range(1, endPoint):
        if word[:i] == word[-i:]:
            count += 1
            solve(word[i:-i])
    return count

word = input()
print(solve(word))