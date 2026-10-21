n = int(input("Please input a positive integer: "))
number = 1

if n < 0:
    print("This is a negative integer")
else: 
    while n > 0:
        number *= n
        n-= 1
    print("The factorial is", number)