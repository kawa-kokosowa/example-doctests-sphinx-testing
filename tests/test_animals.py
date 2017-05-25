"""Here's a typical set of unit tests...

"""

import doctestdemo


def test_animal():
    """Test animal..."""

    cow = doctestdemo.animals.Animal('moo')    
    assert cow.sound == 'moo'
