import random
import string

def generateName(photoManager=photoManager):
    chars = string.ascii_letters + string.digits

    while True:
        name = ''.join(random.choices(chars, k=6))

        if not photoManager.nameExists(name):
            return name