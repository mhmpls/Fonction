#Activité 1: Ecriture d'un fichier
"""
fichier = open ("monFichierLatin9.txt", mode="w", encoding="latin9")
fichier.write("Ce pull est très cher, il coute 100 €.")
fichier.close()
"""

#Activité 1: Lecture d'un fichier
"""
fichier = open ("monFichierLatin9.txt", mode="r", encoding="utf8")
contenu= fichier.read()
print(contenu)
fichier.close()
"""

#Activité 2: Un programme Python pour convertir en majuscule

#2:
"""
lettre_min = str(input("Entrez un caractère minuscule : "))
code_min = ord(lettre_min)
code_maj = code_min - 32
lettre_maj = chr(code_maj)
print(lettre_maj)
"""
#3:
"""
lettre_min = str(input("Entrez un caractère minuscule : "))
def maj2min():
    global code_min, code_maj, lettre_maj
    code_min = ord(lettre_min)
    code_maj = code_min - 32
    lettre_maj = chr(code_maj)
    return lettre_maj

print(maj2min())
"""

#4: Au lieu de faire -32 il faut faire +32













