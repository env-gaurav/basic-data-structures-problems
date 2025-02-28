# Reverse the digits
def reverseTheDigit(num):
    result = 0
    while num > 0:
        r = num%10
        result = result*10+r
        num = num//10
    return result

# Addition of digits
def addition(num):
    result = 0
    while num > 0:
        r = num%10
        result = result + r
        num = num//10
    return result

num = 12345
print("Reversed Digit:", reverseTheDigit(num))
print("Sum of Digits:", addition(num))