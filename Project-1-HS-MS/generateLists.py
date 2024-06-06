import random

# delcare the min and max size the arrays can be
RANGE_MIN = 1000
RANGE_MAX = 10000000


# Function to generate a list of random numbers
# x is the max size of the range of numbers
def generate_random_list(x, size):
    return [random.randint(1, x) for _ in range(size)]
