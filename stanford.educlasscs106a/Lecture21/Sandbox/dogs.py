class Dog:
    def __init__(self):
        self.times_barked = 0

    def bark(self):
        print('woof')
        self.times_barked += 1


def main():
    jupiter = Dog()
    juno = Dog()
    jupiter.bark()
    juno.bark()
    jupiter.bark()
    print(jupiter.__dict__)
    print(juno.__dict__)

