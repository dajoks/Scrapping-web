import requests  # pour envoyer des requêtes HTTP
from bs4 import BeautifulSoup  # pour parser le HTML et extraire des informations

# URL de la page à scraper
url = "https://www.annuaire-mairie.fr/departement-somme.html"

# Envoi d'une requête GET à l'URL
response = requests.get(url)

# Vérifie si la requête a réussi (status code 200)
response.raise_for_status()  # ATTENTION : il manque les parenthèses pour l'exécuter

# Affiche l'objet response pour voir si la requête a fonctionné
print(response)

# Parser le contenu HTML de la page avec BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Liste pour stocker tous les liens des villes
links = []

# URL de base pour compléter les liens relatifs
base_url = "https://www.annuaire-mairie.fr"

# Parcours de toutes les balises <td> de la page
for td in soup.find_all('td'):
    # Cherche une balise <a> avec un attribut href dans chaque <td>
    tag = td.find('a', href=True)
    if tag:
        # Ajoute le lien complet (base_url + href) à la liste
        links.append(base_url + tag['href'])

        # Écrit tous les liens trouvés dans un fichier texte
        with open('villeliste.txt', 'w', encoding='utf-8') as file:
            for link in links:
                file.write(link + "\n")
