print("=== Bienvenue dans notre système de calcul ===")
print("Choisissez une opération :")
print("1 - Addition")
print("2 - Soustraction")
print("3 - Multiplication")
print("4 - Division")

try:
    choix = int(input("Votre choix (1-4) : "))

    nombre1 = float(input("Saisir le premier nombre (nombre 1) : "))
    nombre2 = float(input("Saisir le second nombre (nombre 2) : "))

    if choix == 1:
        resultat = nombre1 + nombre2
        print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
    elif choix == 2:
        resultat = nombre1 - nombre2
        print(f"Résultat : {nombre1} - {nombre2} = {resultat}")
    elif choix == 3:
        resultat = nombre1 * nombre2
        print(f"Résultat : {nombre1} × {nombre2} = {resultat}")
    elif choix == 4:
        if nombre2 != 0:
            resultat = nombre1 / nombre2
            print(f"Résultat : {nombre1} ÷ {nombre2} = {resultat}")
        else:
            print("Erreur : Division par zéro interdite ")
    else:
        print("Choix invalide ! Veuillez entrer un nombre entre 1 et 4.")

except ValueError:
    print("Erreur : Veuillez entrer uniquement des nombres valides.")
