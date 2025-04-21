class Dog:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(self.name + " is playing")

    def sleep(self):
        print(self.name + " is sleeping")

    def day_cycle(self):
        self.sleep()
        self.play()
        self.play()
        self.play()
        self.sleep()

class Puppy(Dog):
    def day_cycle(self):
        self.sleep()
        self.play()
        self.sleep()
        self.play()
        self.sleep()