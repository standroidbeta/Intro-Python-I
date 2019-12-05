# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def is_even_or_odd(num):
    if (num % 2) == 0:
        print(f'{num} is Even')
    else:
        print(f'{num} is Odd.')


is_even_or_odd(num)

