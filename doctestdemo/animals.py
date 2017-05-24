"""This be the animal docstring at module level"""


class Animal:
    """This be the Animal class docstring.

    This is a base class for other animals (classes) to inherit from.

    >>> class Dog(Animal):
    ...     def fetch(self, throw_this):
    ...         return throw_this
    >>> dog = Dog('awoo')
    >>> dog.fetch(44)
    44
    >>> dog.makes()
    'awoo'

    """

    def __init__(self, sound):
        """This is the animal class init method docstring.

        Arguments:
            sound (str): the sound the animal makes!

        """

        self.sound = sound

    def goes(self):
        """As in "the cat goes..." prints the sound.

        """

        print(self.sound)


class Cat:
    """Cat animal docstring!"""

    def __init__(self):
        super(Cat).__init__('meow')

    def pet(self):
        """If you pet the cat it purrs!"""
        print("purrrrr")
