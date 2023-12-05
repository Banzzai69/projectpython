## Analyse des Données de la Coupe du Monde de la FIFA

### Contraintes de la Mission

- Toutes les fonctions et structures de données doivent être créées à partir de zéro, en utilisant uniquement les types de données et structures de base du langage, sans recourir à des fonctions ou méthodes avancées du langage.
- Aucune utilisation de fonctions de recherche ou de tri intégrées. Les opérations de recherche, de tri, d'ajout et de suppression doivent être implémentées manuellement.


### Tâches à Réaliser

**Niveau 1 - Opérations de Base**

1. Fonction `charger_donnees(fichier: str) -> list` ok
   - Récupérer les données depuis un fichier.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des lignes du fichier après récupération des données contenus dans le fichier d'entrée.
  
2. Fonction `supprimer_entete(fichier: str) -> list` ok
   - Supprime la première ligne (en-tête) du fichier txt.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des lignes du fichier après suppression de l'en-tête.

3. Fonction `afficher_nom_trois_lettres(str) -> str` ok
   - Affiche un texte en utilisant uniquement les trois premières lettres.
   - Exemple d'entrée : Nom du fichier (.. Espagne, France).
   - Exemple de sortie : mot abrégé (ESP, FRA).

4. Fonction `enregistrer_fichier("donnees, fichier.ext") -> fichier.ext` ok
   - Enregistre les données dans un fichier.
   - Exemple d'entrée : données triées (.. France, Espagne, Argentine).
   - Exemple de sortie : FIFA_1998.txt à jour.

**Niveau 2 - Calculs Statistiques**

1. Fonction `melanger_lignes(donnee) -> list`
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt"). ok 
   - Exemple de sortie : Liste des lignes triées au hasard.

2. Fonction `calculer_points(fichier: str) -> dict` ok
   - Calcule le nombre de points pour chaque équipe en fonction des victoires et des matchs nuls.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Dictionnaire des équipes et de leurs points.

3. Fonction `calculer_difference_buts(fichier: str) -> dict` ok
   - Calcule la différence de buts pour chaque équipe.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Dictionnaire des équipes et de leur différence de buts.

**Niveau 3 - Classement et Qualifications**

1. Fonction `supprimer_colonne(fichier: str, nom_colonne: str) -> list` ok
   - Supprime la colonne spécifiée du fichier txt.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt"), nom de la colonne (ex. "Position").
   - Exemple de sortie : Liste des lignes du fichier après suppression de la colonne.

2. Fonction `trier_par_nom_equipe("donnees") -> list`
   - Trier la liste des équipes par nom.
   - Exemple d'entrée : Nom du fichier (.. France, Espagne, Argentine).
   - Exemple de sortie : la liste des équipes triée par nom abrégé (ARG, ESP, FRA).

3. Fonction `trier_equipes_par_position(donnees) -> list`
   - Trie les équipes par position.
   - Exemple d'entrée : Nom du fichier (ex. "FIFA-1998.txt").
   - Exemple de sortie : Liste des équipes triées par position.

   


### Note

Cette mission permettra de renforcer vos compétences en programmation, en algorithmie et en analyse de données, tout en vous plongeant dans l'excitation d'un des événements sportifs les plus importants au monde. Bonne chance !
