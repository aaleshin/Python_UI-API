import random
import string

def generate_random_string():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(6))
    return rand_string
