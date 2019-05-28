def collatz(number):
    if number%2 == 0:
        return number // 2
    else:
        return 3* number + 1
number = input()

while (collatz(int(number)) != 1):
    number = collatz(int(number))
    print(number)
    print (collatz(int(number)))

    
