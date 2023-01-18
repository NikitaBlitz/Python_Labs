from random import randint, choice


class Person:
    def __init__(self):
        self.name = choice(['Jim', 'Nikita', 'Nick', 'Anna', 'Jack', 'George', 'Oliver'])
        self.age = randint(1, 60)