class Animals():

    def __init__(self, name, age=0, num_legs=4, tail=1):
        # setting attribute name to instances of Dog class
        self.name = name
        self.age = age
        self.paws = num_legs
        self.tail = tail

    def stretch(self):
        return 'yyyyyaaaauuu \n'

    def jumps(self):
        return 'I always land on my paws \n'

    def eat(self, food=''):
        return 'I\'m hungry' + food + '\n'

    def sleep(self):
        return 'zzZZzzZZz ZZzzzZZzz\n'
