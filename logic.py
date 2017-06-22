iint = int(input("Enter a positive Integer: "))

def diinter(iint):
    for i in range(1, iint):
        if iint % i == 0:
            print("{} is a divisor of {}".format(i, iint))


diinter(iint)