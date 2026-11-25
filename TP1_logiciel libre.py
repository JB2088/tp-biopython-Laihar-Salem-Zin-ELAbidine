# Cellule 2 : Premier objet Seq
from Bio.Seq import Seq
# Création d'une séquence d'ADN
dna = Seq("ATGGCCATTGTAATGGGCCGC")
print("Séquence :", dna)
print("Longueur :", len(dna))
print("Premier codon :", dna[0:3])
print("Nombre de G :", dna.count("G"))