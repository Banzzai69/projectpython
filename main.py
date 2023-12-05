from functions import *

# Nom de fichier à charger
FileName = "FIFA_World_Cup/FIFA-2022.txt";

# Charge un fichier en lecture
file = open(FileName, "r")

# Charge les données à partir d'un fichier
data = load_data(FileName);
