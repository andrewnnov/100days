def prime_checker(number):
    if number == 1 or number == 2:
        print("It is prime number")
    elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
        print("It is prime number")      
    else:
        print("It is not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)


