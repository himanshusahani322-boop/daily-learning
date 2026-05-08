def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
n = int(input("Enter Number"))
print(check(n))