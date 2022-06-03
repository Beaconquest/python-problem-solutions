# python execrises from www.practicepython.org

# Execrise 2

num = int(input("Please enter a number: "))
check = int(input("please enter another number: "))

if num % 4 == 0:
    print(f"Your number {num} is a multiple of 4.")
elif num % check == 0:
    print(f"Your Number {check} evenly divides into {num}.")
else:
    print(f"Your number {check} does not evenly divide into {num}")
