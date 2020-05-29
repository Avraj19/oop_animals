class Cat():

    def __init__(self, name='Fluffy'):
        # setting attribute name to instances of Dog class
        self.name = name
        self.age = 1
        self.paws = '4'
        self.fur = 'White with gary strips'
        self.tail = 'fluffy tail'
        self.whiskers = 'long whiskers'
        self.cat_eyes = 'perusing eyes that can tell the future'

    def stretch(self):
        return 'yyyyyaaaauuu \n'

    def jumps(self):
        return 'I always land on my paws \n'

    def eat(self, food=''):
        return 'I\'m hungry' + food + '\n'

    def sleep(self):
        return 'zzZZzzZZz ZZzzzZZzz\n'

    def pur(self):
        return 'pet me pet\n'
