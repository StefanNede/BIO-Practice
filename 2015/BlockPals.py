# Round 1 2015 q1 - 23/23

count = 0
def solve(word:str) -> int:
    global count
    for i in range(1, len(word)//2 + 1):
        if word[:i] == word[len(word)-i:]:
            count += 1
            solve(word[i:len(word)-i])

word = input()
solve(word)
print(count)