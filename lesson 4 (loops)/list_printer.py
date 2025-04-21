"""
Create a list of numbers. Print only the even numbers in the list, and stop printing as soon as you encounter a number greater than 10.
"""

numbers = [1, 8, 3, 2, 5, 12, 5, 3, 10]

for i in numbers:
    if(i % 2 == 1):
        continue
    print(i)

    if(i > 10):
        break