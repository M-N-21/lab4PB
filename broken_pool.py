from multiprocessing import Pool

def square(x):
    """
    Retourne le carré de l'argument.

    Args:
        x: Le nombre dont on veut calculer le carré.

    Returns:
        Le carré de x.
    """
    return x * x

def cube(x):
    """
    Retourne le cube de l'argument.

    Args:
        x: Le nombre dont on veut calculer le cube.

    Returns:
        Le cube de x.
    """
    return x * x * x

if __name__ == "__main__":
    r = [1, 2, 3, 4, 5]

    with Pool() as pool:
        result = pool.map(square, r)
        print("Résultat du carré : %s" % result)

    with Pool() as pool:
        result = pool.map(cube, r)
        print("Résultat du cube : %s" % result)
