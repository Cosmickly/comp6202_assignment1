import string
import random

def random_string(length):
    return ''.join(chr(random.randrange(32, 127)) for _ in range(length))

if __name__ == '__main__':
    print(random_string(28))

