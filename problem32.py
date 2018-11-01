
"""
Maximum product is either 2digits * 3digits or 1digits*5digits
"""

import sys

def is_pandigital(a,b,c):
    a_str = str(a)
    b_str = str(b)
    c_str = str(c)

    all_numbers = [num for num in a_str+b_str+c_str]


    

    if len(all_numbers) != 9:
        return False
    else:
        for i in range(1,10):
            if str(i) not in all_numbers:
                return False
        return True
       

def all_pandigitals_mult():

    
    pan_numbers = []

    for a in range(1,10):
        for b in range(1000,10000):
            if is_pandigital(a,b,a*b):
                print(a, " x ", b,  " = " , a*b)
                pan_numbers.append(a*b)


    for a in range(10,100):
        for b in range(1,1000):
            if is_pandigital(a,b,a*b):
                print(a, " x ", b, " = ", a*b)
                pan_numbers.append(a*b)

    

    return list(set(pan_numbers))

if __name__ == '__main__':
    list_numbers = all_pandigitals_mult()
    print(list_numbers)


    
    print("______")
    print(sum(list_numbers))

