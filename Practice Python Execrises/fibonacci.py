# python execrises from www.practicepython.org

# Execrise 13

user_number = int(input("Enter the number of Fibonacci numbers you want to see:"))

def fib(n):
    '''Function prints n number of Fibonnaci numbers.'''
    count = 0
    pos1, pos2 = 0 , 1

    while count < n:
        print(f"{pos1}")

        update_pos = pos1 + pos2

        pos1 = pos2
        pos2 = update_pos
        count += 1

fib(user_number)


def fib2(n):
    '''Function returns a list n number of Fibonnaci numbers.'''
    count = 0
    pos1, pos2 = 0, 1
    n_fib = []
    while count < n:
        n_fib.append(pos1)

        update_pos = pos1 + pos2
        pos1, pos2 = pos2, update_pos
     
        count += 1

    return n_fib

print(fib2(user_number))
