class Person:
    def __init__(self, name, age):
        self.name = name
        self.years_old = age

    def say_info(self):
        print("My name is " + self.name + " and I am " + str(self.years_old) + " year(s) old")
    
    def age(self, years):
        for i in range(years):
            print("Happy birthday " + self.name + ", you turned " + str(self.years_old + i + 1))
        self.years_old += years

p = Person("John", 20)
p.say_info()
p.age(5)
p.say_info()