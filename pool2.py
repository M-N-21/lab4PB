from multiprocessing import Pool, cpu_count

start_time = time.time()

def square(x):
    """Function to return the square of the argument"""
    print("Worker %s calculating square of %s" % (current_process().pid, x))
    return x * x

if __name__ == "__main__":
    nprocs = 2
    #print the number of cores
    print("Number of workers equals %d" % nprocs)

    # create an array of 5000 integers, from 1 to 5000

    r = range(1, 21)

    #create a pool of workers
    with Pool(processes=nprocs) as pool:

        result = pool.map(square, r)

    total = reduce(lambda x, y: x + y, result)

    print("The sum of the square of the first 20 integers is %s" % total)
    print("\n--- %s seconds" % (time.time() - start_time))
