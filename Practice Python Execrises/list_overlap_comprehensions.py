# python execrises from www.practicepython.org

# Execrise 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

num_a = list(set(a))
num_b = list(set(b))

c = [i for i in num_a if i in num_b ]

print(c)