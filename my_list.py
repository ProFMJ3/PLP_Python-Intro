# 1. Créer une liste vide
my_list = []

# 2. Ajouter les éléments 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Insérer la valeur 15 à la deuxième position (index 1)
my_list.insert(1, 15)

# 4. Étendre la liste avec une autre liste [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Supprimer le dernier élément de la liste
my_list.pop()

# 6. Trier la liste dans l'ordre croissant
my_list.sort()

# 7. Trouver et afficher l'index de la valeur 30
index_30 = my_list.index(30)

# Affichage des résultats et fin du programme
print("Liste finale :", my_list)
print("Index de la valeur 30 :", index_30)


