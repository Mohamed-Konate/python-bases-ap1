#les notions de bases de python
"""
 ceci
    est un
        commentaire
            sur plusieurs lignes
"""
#Affichage du texte dans la console

# print("Bonjour le monde")

# Declaration de variable

nom = "Aly" # (string)
age = 25 # (integer)
poids = 65.5 # (float)
majeur = True # Boolean
notes = [14,17,20] # List
notes_validee = (15, 16, 14) # Tuple
famille = {  # Dictionnaire
    "pere":"Seydou Kane",
    "mere":"Fatoumata CISSE"
}
# Presentation de Aly
print("Je m'appelle", nom, "j'ai", age, "ans et je pese", poids, "kg")

# Manipulation des variables notes, notes_validee et famille
print("Mes notes sont", notes)
print("Mes notes validées sont", notes_validee)
print("Ma famille est composée de", famille)

# Selection des elements de la liste notes, notes_validee et famille
print("La premiere note est", notes[0])
print("La deuxieme note validée est", notes_validee[1])
print("Le nom de mon pere est", famille["pere"])
# difference entre les listes et les tuples
notes[0] = 15
# notes_validee[0] = 15 # erreur
n =  notes_validee.__add__((15,)) # (15, 16, 14, 15)

print("Mes notes sont", notes)
print("Mes notes validées sont", notes_validee)
print("Mes notes validées sont", n)

# Les conditions
#Recuperation de l'age de l'utilisateur
# definition du casting : conversion d'une variable en un autre type
# En C int nombre=5 nombre/2 = 2 (double)nombre/2 = 2.5 ==> 5.0/2 = 2.5
age = int(input("Quel est votre age?"))

if age >= 18:
    print("Je suis majeur")
else:
    print("Je suis mineur")

# operateur not
if not age >= 18:  # !(age >= 18)
    print("Je suis mineur")

# operateur is not
if age is not 18:
    print("Je ne suis pas majeur")


# Les boucles






