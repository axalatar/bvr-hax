def fibonacci_recursive(max_depth, prev_num=0, num=1, depth=0):
    if(depth >= max_depth):
        return prev_num
    return fibonacci_recursive(max_depth, prev_num=num, num=prev_num+num, depth=depth+1)
    
print(fibonacci_recursive(100))