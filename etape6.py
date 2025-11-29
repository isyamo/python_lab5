classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5]
]
classe.sort(key=lambda ligne: ligne[2], reverse=True)
print(classe)

# Calcul de la moyenne des notes en parcourant les sous-listes
somme_notes = 0
for etudiant in classe:
    somme_notes += etudiant[2]  
moyenne = somme_notes / len(classe)
print(f"Moyenne des notes : {moyenne:.2f}")

recherche_nom = input("Entrez le nom de l'étudiant à rechercher : ")
trouve = False
for nom, age, note in classe:  
    if nom == recherche_nom :
        print(f"Étudiant trouvé : Nom={nom}, Âge={age}, Note={note}")
        trouve = True
        break
if not trouve:
    print("Étudiant non trouvé.")

classe_copie= classe[:]
classe_copie[0][1]=27
print(classe)

classe_dict = []
for etudiant in classe:
    etudiant_dict = {
        "nom": etudiant[0],
        "age": etudiant[1],
        "note": etudiant[2]
    }
