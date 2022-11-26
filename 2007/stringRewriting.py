# BIO round 1 q3 - 17/25
import string

ALPHA = list(string.ascii_uppercase)[:5]
RULES = {"A": "B",
         "B": "AB",
         "C": "CD",
         "D": "DC",
         "E": "EE"}


class Solve:
    def __init__(self, string, position):
        self.string = string
        self.position = position

    def rewrite(self):
        resString = ""
        for el in self.string:
            resString += RULES[el]
        self.string = resString

    def getNumOccurences(self):
        # gets the number of A,B,C,D,E occuring in the first self.position
        # characters of self.string
        occ = [0, 0, 0, 0, 0]
        resString = self.string[:self.position]
        for el in resString:
            occ[ALPHA.index(el)] += 1
        return occ


def main():
    string = input()
    s, p = [int(i) for i in input().split(' ')]
    so = Solve(string, p)
    for i in range(s):
        so.rewrite()
    print(so.string)
    print(len(so.string))
    res = so.getNumOccurences()
    for r in res:
        print(r, end=" ")


main()
