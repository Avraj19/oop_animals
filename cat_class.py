class Cat():

    def __init__(self, name='', age='', paws='', fur=''):
        # setting attribute name to instances of Dog class
        self.name = name
        self.age = age
        self.paws = paws
        self.fur = fur

    def stretch(self):
        return 'yyyyyaaaauuu \n'

    def eat(self, food=''):
        return 'I\'m hungry' + food
