# python execrises from www.practicepython.org

# Execrise 1 

name = input("What is your name?")

age = int(input("How old are you today?"))

year = 2020 + (100 - age)

message = f"{name} did you know you will be 100 years old in the year {year}"

print(message)

number = int(input(f"{name}, how about you give me another number?"))

for i in range(number):
    print(message)
