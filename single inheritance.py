class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "eating food")


class dog(animal):
    def bark(self):
        print("woof! woof!")


a1 = animal("tommy")
d1 = dog("mike")
d1.eat()
d1.bark()
a1.eat()
