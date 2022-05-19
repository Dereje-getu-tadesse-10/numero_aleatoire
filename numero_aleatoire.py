import random
# Numéro aléatoire
random_num = random.randrange(0, 100, 5)

# Message de bienvenue
print('*'*85)
print('*' * 25 + " Bienvenue dans le nombre mystere " + '*' * 26)
print('*'*85)


def nombre_mystere():
    # Nombre de tentatives
    max_tentatives = 7
    # totla de tentatives
    total_tentatives = 0
    while True:
        # recuperation choix du l'utilisateur
        choixUser = int(input("Ton numéro : "))

        # condition de victoire
        if choixUser == random_num:
            print(
                f'Bravo, tu as trouvé le nombre mystère en {total_tentatives} tentatives')
            break

        # condition si le choix de l'utilisateur et superieure ou inferieur au nombre mystere
        if choixUser > random_num:
            max_tentatives -= 1
            total_tentatives += 1
            print(
                f'non le nombre myster et inférieur a {choixUser} il te reste {max_tentatives} tentatives')

        elif choixUser < random_num:

            max_tentatives -= 1
            total_tentatives += 1
            print(
                f'non le nombre myster et supérieur a {choixUser} il te reste {max_tentatives} tentatives')

        # Arret si le nombre de tentative et a 0
        if max_tentatives == 0:
            print(
                f'perdu nombre mystere etait le {random_num}')
            break


nombre_mystere()
