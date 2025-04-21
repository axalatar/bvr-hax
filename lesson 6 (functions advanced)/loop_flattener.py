def flatten(nested):
    flattened = []
    stack = [nested]
    
    while len(stack) != 0:
        current = stack.pop()
        if(isinstance(current, list)):
            stack.extend(current)
        else:
            flattened.append(current)

    return flattened[::-1]