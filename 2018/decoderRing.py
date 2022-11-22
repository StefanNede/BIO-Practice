# BIO round 1 q2 - 24/24
# weirdly easy
import string

ALPHA = list(string.ascii_uppercase)

class Encode:
    def __init__(self, n, word):
        self.dial1 = []
        self.dial2 = []
        self.n = n
        self.word = word
        self.encrypted = ""

    def generateDial1(self):
        self.dial1 = [letter for letter in ALPHA]

    def generateDial2(self):
        inter = [letter for letter in ALPHA]
        position = 0
        while len(inter) > 1:
            position += self.n-1
            position %= len(inter)
            self.dial2.append(inter.pop(position))
        self.dial2.append(inter[0])
    
    def shuffle(self):
        # shuffle self.dial2 so that after each encryption 
        self.dial2.append(self.dial2.pop(0))

    def encodeWord(self):
        for i in range(len(self.word)):
            change = self.dial2[self.dial1.index(self.word[i])]
            self.encrypted += change
            self.shuffle()


def main():
    n, word = input().split(' ')
    n = int(n)
    e = Encode(n, word)
    e.generateDial1()
    e.generateDial2()
    dial2 = e.dial2
    print("".join(dial2[:6]))
    e.encodeWord()
    encodedW = e.encrypted
    print(encodedW)

main()