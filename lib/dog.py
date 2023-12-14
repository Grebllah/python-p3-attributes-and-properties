#!/usr/bin/env python3

### `Dog` and `lib/dog.py`

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = "Pooch", breed = "Corgi"):
        self.name = name
        self.breed = breed
    def get_name(self):
        return self._name
    def set_name(self, name):
        if type(name) == str and len(name) < 25 and len(name) > 0:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    def get_breed(self):
        return self._breed
    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        elif breed in APPROVED_BREEDS:
            self._breed = breed
        pass

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


# 1. Define a `name` property for your `Dog` class. The name must be of type `str`
# and between 1 and 25 characters. Your `__init__` method should receive a default
# argument for `name`.
#     - If the name is invalid, the setter method should `print()` "Name must be
# string between 1 and 25 characters."
# 2. Define a `breed` property for your `Dog` class. Your `__init__` method should
#    receive a default argument for `breed`.
#     - If the breed is invalid, the setter method should `print()` "Breed must be
# in list of approved breeds." The breed must be in the following list of dog
# breeds: