# Prime number
import re


def prime_checker(number):
    for n in range(2, number - 1):
        if number % n == 0:
            print("It's not a prime number.\n")
            return 0

    print("It's a prime number.\n")

n = int(input("Check this number: "))
prime_checker(number=n)

