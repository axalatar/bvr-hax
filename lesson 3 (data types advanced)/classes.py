"""
Make a dictionary of your classes, and for each class put your teacher and grade (you can make stuff up if you need). Then, take an input of which class you want to view and whether you want to read from or write to the grade. If you read from it, print the grade and teacher of that class, otherwise take another input of the new grade to set it to.
"""

classes = {
    "math": [95, "Matsu"],
    "english": [93, "Mr. Bollag-Miller"],
    "science": [94, "Ms. Wildes"],
    "spanish": [90, "Ms. Morillo"]
    }

wanted_class = input("Which class do you want to look at? ")
operation = input("Do you want to view or edit? ")

class_data = classes[wanted_class]

if(operation == "edit"):
    new_grade = int(input("What do you want to set the grade to? "))
    class_data[0] = new_grade
elif(operation == 'view'):
    print("The current grade in " + class_data[1] + "'s class is " + str(class_data[0]))
    