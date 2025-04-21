numbers = [(10, 2), (5, 20), (8, 5), (3, 2), (9, 5), (1, 15), (4, 7)]
answer = sorted(numbers, key=lambda x: x[1])
print(answer)