# google: python 3 module index

# built-in module
import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


dice = Dice()
print(dice.roll())
