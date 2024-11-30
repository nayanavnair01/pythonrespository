'''
author: nayana v nair
date:30/11/2024
'''
def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
def max_of_three(a,b,c):
    return max_of_two(a, max_of_two(b, c))
print(max_of_three(3, 6, 7))
