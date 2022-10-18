import time

class Palindrome:
    def __init__(self, num):
        self.num = num + 1

    def isPalindrome(self):
        '''
        checks if inputted num is a palindrome
        :int num:
        :return bool:
        '''
        secondHalf = 0
        if self.num == 0:
            return False
        if self.num < 0 or self.num%10 == 0:
            return False

        while secondHalf < self.num:
            secondHalf = secondHalf*10 + self.num%10
            self.num //= 10

        return secondHalf == self.num or secondHalf//10 == self.num

    def isPalindrome2(self):
        return str(self.num)[::-1] == str(self.num)

    def getNearestPal(self):
        pass

    def getPal(self):
        while self.isPalindrome2() == False:
            self.num += 1
        return self.num

def checkPal():
    num = int(input())
    pal = Palindrome(num)
    start = time.time()
    res = pal.getPal()
    end = time.time()
    print(res, end - start)

def main():
    # checkPal()
    pass

if __name__ == '__main__':
    main()
