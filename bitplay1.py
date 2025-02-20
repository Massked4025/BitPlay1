def numberofbits(n):
    one = 0
    zero = 0
    while (n):
        if (n & 1 == 1):
            one += 1
        else:
            zero += 1
        n>>=1
    print("Number of ones: ", one)
    print("Number of zeros: ", zero)

n = int(input("Enter your number: "))
numberofbits(n)

#Set Bit or Not

def setornot(number, n):
    mask = 1
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << (n - 1)):
            print("Set")
        else:
            print("Not Set")
number = int(input("Enter your number: "))
n = int(input("Enter the bit position: "))
setornot(number, n)