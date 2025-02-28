# Reverse the digits
num = 12345
result = 0
while num > 0:
    r = num%10
    result = result*10+r
    num = num//10

print(result)