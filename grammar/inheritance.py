class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    # Python doesn't like empty objects, so we can just add pass to do nothing with it atm
    # pass
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.be_annoying()

###############################


class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef makes fried rice")

    # overriding
    def make_special_dish(self):
        print("The chef makes orange chicken")


myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()

