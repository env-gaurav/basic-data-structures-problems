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

def countDigits(num):
    result = 0
    while num>0:
        r = num%10
        result = result + 1
        num = num//10
    return result

def largestDigit(num):
    largest = 0
    while num>0:
        r = num%10
        if r>largest:
            largest = r
        num = num//10
    return largest

def firstAndLastDigit(num):
    ld= num%10
    while num>=10:
        num = num//10
    fd = num
    return fd,ld

def armstrong(num):
    cp = num
    result= 0
    power = countDigits(num)
    while num>0:
        r= num%10
        result = (r**power)+ result
        num = num//10
    return result == cp

def isArmstrong(num):
    check = armstrong(num)
    if check == True:
        return f"{num} is an Armstrong number"
    else:
        return f"{num} is not an Armstrong number"

def countOddEven(num):
    even = 0
    odd = 0
    while num>0:
        r = num%10
        if r%2 == 0:
            even= even+1
        else:
            odd = odd+1
        num=num//10
    return even,odd


num = 12345

print(countOddEven(num))
print(isArmstrong(153))
print("First and Last Digit:",firstAndLastDigit(num))
print("Largest Digit:", largestDigit(num))
print("Reversed Digit:", reverseTheDigit(num))
print("Sum of Digits:", additionOfDigits(num))
print("product Of Digits:", productOfDigits(num))
print("Palindrome:", isPalindrome(num))
print("Palindrome:", isPalindrome(121))
print("Number of digits:",countDigits(num))