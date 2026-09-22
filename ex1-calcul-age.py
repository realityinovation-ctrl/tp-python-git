nom = input("Quel est votre nom ? ")
annee_naissance = int(input("Quelle est votre année de naissance ? "))
annee_actuelle = 2026

age = annee_actuelle - annee_naissance
print(f"Bonjour {nom}, vous avez (ou aurez) {age} ans cette année.")