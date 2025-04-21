def apply_function(numbers, func):
    new_numbers = []
    for i in numbers:
        new_numbers.append(func(i))
    return new_numbers