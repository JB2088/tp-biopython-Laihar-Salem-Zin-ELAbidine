# Cellule 8 : Filtrer les séquences de plus de 80 pb
from Bio import SeqIO

sequences_longues = []
for record in SeqIO.parse("echantillons.fasta", "fasta"):
    if len(record.seq) > 80:
        sequences_longues.append(record)
print("Séquences > 80 pb :")
for record in sequences_longues:
    print(f" {record.id} : {len(record.seq)} pb")

# Export du résultat
SeqIO.write(sequences_longues, "sequences_longues.fasta", "fasta")
print("\nFichier sequences_longues.fasta écrit.")