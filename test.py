# def formatter_generator(functions):
#     ...


# uppercase = lambda s: s.uppercase()     # uppercase of string
# hyphens = lambda s: '-'.join(list(s))   
# formatter = formatter_generator([uppercase, hyphens])

# formatted = formatter("Hello! My name is Andre.")
# print(formatted) # HELLO! M-y NAME i-s ANDRE.


import time

def time_function(func):
    start = time.time()
    func()
    print(f"It took {time.time() - start} seconds")

import math
def test():
    b=[]
    for i in range(1000000):
        b.append(math.sqrt(i))

time_function(test)