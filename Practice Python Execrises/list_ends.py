# python execrises from www.practicepython.org

# Execrise 7

a = [5, 10, 15, 20, 25]

def first_and_last(a_list):
    b = []
    length = len(a_list)
    
    # first attempt
    # b.append(a_list[0])
    # b.append(a_list[length -1])
    
    
    # second attempt-- works but its a reach, but its different
    d =list(enumerate(a_list))
    c = [d[0][1], d[length -1][1]]

    return c

print(first_and_last(a))