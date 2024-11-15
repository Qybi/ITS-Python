'''
Serie di Collatz dice che:

f(x) = x/2 se x è pari
f(x) = 3x+1 se x è dispari

Per ogni x appartaente ai numeri naturali, la serie di Collatz termina sempre con 1
F composto F composto ... F(x) = 1
'''

def collatz(x, depth):
    print(f" --> {x}", end=' ')
    # global depth
    if x == 1:
        return depth
    elif x % 2 == 0:
        collatz(x//2, depth+1) # // is the integer division
    else:
        collatz(3*x+1, depth+1)


while True:
    print ("\n| ----------------------------------------------------------- |")
    print ("| Collatz series |")
    print ("| 1 - Print collatz series for a given number |")
    print ("| 2 - Given a depth value, return the respective number |")
    print ("| 3 - Edit Collatz coefficients and prints the menu |")
    print ("| ----------------------------------------------------------- |")
    command = input("Insert a command: ")
    match command:
        case '1':
            depth = 0
            x = int(input("Insert a number: "))
            depth = collatz(x, depth)
            print(f"\nCollatz series for {x} has a depth of {depth}")
            continue
        case '2':
            x = int(input("Insert a number:"))
            # starting from 1, we will iterate through the collatz series until we reach the given depth
            continue
        case '3':
            continue
        case default:
            print ("Invalid command")
            continue
