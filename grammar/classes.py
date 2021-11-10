class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()

point2 = Point()
point2.move()

#######################


class Student:
    def __init__(self, name, major, gpa, is_on_probation):      # init function
        self.name = name        # self.name => attribute
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False


student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Phyllis", "Art", 3.8, True)

print(student1.name)
print(student2.gpa)

print(student1.on_honor_roll())
print(student2.on_honor_roll())



