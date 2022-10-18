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

    def getPalSmart(self, num, headP=0):
        '''
        num - list of ints
        get smaller next front half and then put it onto the last half in reverse
        e.g. 17 -> next smallest front half is 2. put 2 into second half ---> 22
        '''
        # print(num)
        if headP >= len(num) // 2:
            print(''.join([str(i) for i in num]))
            return
        if num[headP] != num[-1 - headP] and num[headP] > num[-1 - headP]:
            num[-1 - headP] = num[headP]
        elif num[headP] != num[-1 - headP] and num[-1 - headP] > num[headP]:
            num[headP] += 1  # e.g. 17 --> 22
            num[-1 - headP] = num[headP]

        self.getPalSmart(num, headP + 1)

    def getPalNaive(self):
        while self.isPalindrome2() == False:
            self.num += 1
        return self.num

def checkPal():
    num = int(input())
    pal = Palindrome(num)
    # dumb version
    start = time.time()
    res = pal.getPalNaive()
    end = time.time()
    print(res, end - start)
    # smarter version
    num += 1
    num = [int(x) for x in str(num)]
    pal.getPalSmart(num)

def main():
    checkPal()
    #pass

if __name__ == '__main__':
    main()
