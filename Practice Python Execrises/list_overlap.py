# python execrises from www.practicepython.org

# Execrise 5
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(set([i for i in a for j in b if i == j])) 

print(c)

# random rgenerated list, used set to remove depulicates
d = list(set([random.randrange(25) for i in range(15)]))
e = list(set([random.randrange(25) for i in range(15)]))

print(f"First list {d}")

print(f"Second List {e}")

f = [i for i in d for j in e if i == j]
print(f)