from main import recherche, verifie_chaine, remplace, verifie_numero, verifie_email

# Test Exercice 1: Recherche de Mot
mot_test = "Hello"
chaine_test = "Hello, i am Noureddine."
resultat = recherche(mot_test, chaine_test)
print(f"Exercice 1: {resultat}")  

# Test Exercice 2: Vérification de Chiffres
chaine_test = "This string contains 123."
resultat = verifie_chaine(chaine_test)
print(f"Exercice 2: {resultat}")  

# Test Exercice 3: Remplacement d'Espaces
chaine_test = "ISGI is the best."
resultat = remplace(chaine_test)
print(f"Exercice 3: {resultat}")  

# Test Exercice 4: Vérification du Numéro de Téléphone
numero_test = "12-345-6789"
resultat = verifie_numero(numero_test)
print(f"Exercice 4: {resultat}")  

# Test Exercice 5: Validation de l'Adresse E-mail
email_test = "test@example.com"
resultat = verifie_email(email_test)
print(f"Exercice 5: {resultat}")  
