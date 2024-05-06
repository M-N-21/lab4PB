from functools import reduce
import time

start_time = time.time()

def main():
    """
    Calcule la somme des carrés des 5000 premiers entiers positifs.
    """
    # Génère une liste des 5000 premiers entiers positifs.
    r = range(1, 5001)

    # Calcule le carré de chaque entier dans la liste.
    result = map(lambda x: x * x, r)

    # Calcule la somme des carrés des 5000 premiers entiers positifs.
    total = reduce(lambda x, y: x + y, result)

    # Affiche la somme des carrés des 5000 premiers entiers positifs.
    print("The sum of the square of the first 5000 integers is %s" % total)

    # Affiche le temps d'exécution du programme.
    print("\n--- %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    main()
