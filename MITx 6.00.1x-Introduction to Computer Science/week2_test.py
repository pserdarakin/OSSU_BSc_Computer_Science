# Week2
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

#Exercise guess my number(Simple algorithms)
print("Please think of a number between 0 and 100!")
guess = 0
numbers = list(range(101))
low = 0
high = 100

while True:
    guess = (high + low) // 2
    guess_print = print("Is your secret number", guess)
    take_input = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to "
        "indicate I guessed correctly: ")
    if take_input == 'h':
        high = guess
    elif take_input == 'l':
        low = guess
    elif take_input == 'c':
        print("Suck it! I guessed correctly. Long live the computers!")
        break
    else:
        print("Sorry, I did not understand your input.")

# Functions - recpower

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 1:
        return base * exp
    else:
        return base * iterPower(base, exp - 1)


print(iterPower(3, 5))

# functions - iterpower

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    mult = 1
    while exp > 0:
        mult *= base
        exp -= 1
    return mult


print(iterPower(3, 5))

GCD - Iter

def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    # Your code here
    t = 0
    n = 0
    while True:
        n += 1
        if (a % n == 0) and (b % n == 0):
            if n > t:
                t = n
        elif n > a or n > b:
            break
    print(t)


gcdIter(9, 12)

# GCD recursive
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


print(gcdRecur(17,12))

def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    # Your code here
    # bisection search: I need to find first and last char of string and divide 2
    if aStr == "":
        return False
    if len(aStr) == 1:
        return aStr == char

    # Recursive approach
    # Find mid-character
    mid_index = len(aStr) // 2
    mid_char = aStr[mid_index]

    if char == mid_char:
        return True
    elif char < mid_char:
        return isIn(char, aStr[:mid_index])
    elif char > mid_char:
        return isIn(char, aStr[mid_index+1:])



print(isIn('z', 'abcdefg.'))
