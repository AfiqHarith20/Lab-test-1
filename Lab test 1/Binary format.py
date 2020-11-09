def decimalTobinary(num):
    if num > 1:
        decimalTobinary(num // 2)
    print (num % 2, end='')

#input decimal number
number = int(input("Please enter any decimal number: "))

decimalTobinary(number)
