class Cat():

    def __init__(self, name='', age='', fur=''):
        # setting attribute name to instances of Dog class
        self.name = name
        self.age = age
        self.paws = '4'
        self.fur = fur
        self.tail = 'fluffy tail'
        self.whiskers = 'long whiskers'
        self.cat_eyes = 'perusing eyes that can tell the future'

    def stretch(self):
        return 'yyyyyaaaauuu \n'

    def jumps(self):
        return 'I always land on my paws'

    def eat(self, food=''):
        return 'I\'m hungry' + food

    def sleep(self):
        return 'zzZZzzZZz ZZzzzZZzz'

    def pur(self):
        return 'pet me pet'
