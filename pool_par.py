from functools import reduce
from multiprocessing import Pool, cpu_count

import time

start_time = time.time()

def square(x):
    """
    Calculate the square of a number.

    Args:
        x (int): The number to square.

    Returns:
        int: The square of the number.
    """
    return x * x

def main():
    """
    Calculate the sum of the squares of the first 5000 integers.

    This function uses the `Pool` class from the `multiprocessing` module to distribute the
    calculation of the squares of the numbers across multiple cores. This can significantly
    improve the performance of the program, especially on computers with multiple cores.
    """
    # Get the number of available cores
    num_cores = cpu_count()

    # Create a pool of workers
    with Pool(num_cores) as pool:
        # Generate a list of the first 5000 integers
        numbers = range(1, 5001)

        # Calculate the squares of the numbers in parallel
        squares = pool.map(square, numbers)

        # Calculate the sum of the squares
        total = reduce(lambda x, y: x + y, squares)

    # Print the sum of the squares
    print("The sum of the squares of the first 5000 integers is", total)

    # Print the execution time
    print("\n--- %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    main()
