"""Take an input of a score on a test from 1-100, and output the user’s letter grade. If the grade is at or below an F, print that the student failed. If the score is outside the range, print that the student cheated."""

score = int(input())

if(score > 100 or score < 0):
    print("Student cheated")
elif(score > 93):
    print("A")
elif(score > 83):
    print("B")
elif(score > 73):
    print("C")
elif(score > 63):
    print("D")
else:
    print("Student failed")