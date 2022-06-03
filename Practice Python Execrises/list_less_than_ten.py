# python execrises from www.practicepython.org

# Execrise 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Please enter a number: "))
b = [i for i in a if i < num ]

print(b)