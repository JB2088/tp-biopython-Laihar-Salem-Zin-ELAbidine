# Cellule 7 : Lecture du fichier FASTA
from Bio import SeqIO
print("=== Séquences du fichier ===")
for record in SeqIO.parse("echantillons.fasta", "fasta"):
    print("ID :", record.id)
    print("Description :", record.description)
    print("Longueur :", len(record.seq), "pb")
    print("---")