# python execrises from www.practicepython.org

# Execrise 11

user_number = int(input("Enter a number:"))

def is_prime(number):
    """A function to determine whether a number is a prime Number."""
    a = [i for i in range(2, number + 1) if number % i == 0]

    if number == 1:
        print(f"{number} is Prime.")
        return a
    elif len(a) == 1:
        print(f"{number} is Prime.")
        return a
    else:
        print(f"{number} is not Prime.")
        return a

print(is_prime(user_number))