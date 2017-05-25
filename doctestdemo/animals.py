"""This be the animal docstring at module level"""

import random


class Animal:
    """This be the Animal class docstring.

    This is a base class for other animals (classes) to inherit from.

    >>> class Dog(Animal):
    ...     def fetch(self, throw_this):
    ...         return throw_this
    >>> dog = Dog('awoo')
    >>> dog.fetch(44)  # Ha, ha! Get it?
    44
    >>> dog.goes()
    The dog goes "awoo!"

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

        animal_name = self.__class__.__name__.lower()
        print('The %s goes "%s!"' % (animal_name, self.sound))

    def list_of_noises(self, number_of_times):
        """Produce a list of this animal's noise n times.

        Arguments:
            number_of_times (int): How many elements should this
                list be, where each element is the sound this animal
                makes.

        Returns:
            list[str]: A list of this animal's noise n times.

        Example:
            >>> lion = Animal('roar')
            >>> lion.list_of_noises(20)  # doctest: +ELLIPSIS
            ['roar', 'roar', roar', ..., 'roar']

        """

        return [self.sound for i in range(number_of_times)]


class Cat:
    """Cat animal docstring!"""

    def __init__(self):
        # FIXME: this put here to point out bug
        """"Some function description.

        Example:
            >>> lambda x: x  # doctest: ELLIPSIS
            <function <lambda> at 0x...>

        """
        super(Cat).__init__('meow')

    def pet(self):
        """If you pet the cat it purrrrs, where the number of 'r's is
        between 2 and 6 (random).

        Example:
            >>> cat = Cat()
            >>> cat.pet()  # doctest: +SKIP
            purrrr
            >>> cat.pet()  # doctest: ELLIPSIS
            purr...

        """

        print('pur' + ('r' * randint(1, 6)))
   

def random_animal_sound():
    """Use this to produce a random animal sound!

    >>> random_animal_sound()  # doctest: +SKIP
    Moo!

    """

    sounds = ['moo', 'quack', 'bark', 'roar', 'meow']
    return random.choice(sounds)
