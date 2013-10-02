"""
Write a function that iterates throgh the numbers 1 through 100. If the number
is divisible by 3, output the string "Fizz". If the number is divisible by 5,
output the string "Buzz". If the number is divisible by both 3 and 5, output
the string "FizzBuzz". If the number is not divisible by either 3 or 5, 
output the number.
"""


def fizzbuzz(numbers=range(1, 101)):
    """
    For each number in a provided range, print "Fizz" if the number is
    divisible by 3, "Buzz" if the number is divisible by 5, "FizzBuzz" if
    the number is divisible by 3 and 5, and the number if neither.
    """
    result = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result


if __name__ == '__main__':
    # Run FizzBuzz for 1 to 100
    print(fizzbuzz())
    print 1