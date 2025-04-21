"""
A Monte-Carlo simulation is a simulation that takes many random data points to approximate a real value. We can use this to approximate pi. We know that the area of a unit circle is pi, and the smallest square surrounding it has a side length of 2. That means that, if you take a random point in that square, there is a pi/4 chance that it will be inside the circle. Based on some number of random samples in that square, and the number of samples which are inside of an inscribed unit circle, approximate pi.
"""

import random

samples = 1000000
inside_circle = 0

for i in range(samples):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if(x**2 + y**2 <= 1):
        inside_circle += 1

pi = 4 * inside_circle / samples
print(pi)