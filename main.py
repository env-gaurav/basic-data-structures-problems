# Reverse the digits
def reverseTheDigit(num):
    result = 0
    while num > 0:
        r = num%10
        result = result*10+r
        num = num//10
    return result

# Addition of digits
def additionOfDigits(num):
    result = 0
    while num > 0:
        r = num%10
        result = result + r
        num = num//10
    return result

def productOfDigits(num):
    result = 1
    while num>0:
        r = num%10
        result = result*r
        num = num//10
    return result

def isPalindrome(num):
    cp = num
    result = reverseTheDigit(num)
    if result == cp:
        return True
    else:
        return False


num = 12345
print("Reversed Digit:", reverseTheDigit(num))
print("Sum of Digits:", additionOfDigits(num))
print("product Of Digits:", productOfDigits(num))
print("Palindrome:", isPalindrome(num))
print("Palindrome:", isPalindrome(121))