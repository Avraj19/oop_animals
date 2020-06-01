from animal_class import Animals


class Cat(Animals):

    def __init__(self, name='', age=1, fur='White with gary strips', tail='fluffy tail'):
        super().__init__(name, age=1, num_legs=4, tail=1)
        # setting attribute name to instances of Dog class
        self.__name = name
        self.age = age
        self.fur = fur
        self.tail = tail
        self.whiskers = 'long whiskers'
        self.cat_eyes = 'perusing eyes that can tell the future'

    def set_name(self, name):
        self.__name = name
        return 'name has been changed to ' + name

    def get_name(self):
        return self.__name

    def pur(self):
        return 'pet me pet\n'
