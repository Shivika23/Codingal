class student:
    name = "Stacy"
    grade = 8

    def intro(self):
        print("Hi i am a student")

    def details(self):
        print("My name is ", self.name)
        print("I study in grade ", self.grade)


obj1 = student()
obj1.details()

