# Cellule 4 : Traduction
from Bio.Seq import Seq
dna = Seq("ATGGCCATTGTAATGGGCCGC")
proteine = dna.translate()
print("Protéine :", proteine)
print("Longueur de la protéine :", len(proteine), "acides aminés")