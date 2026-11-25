# Cellule 5 : Calcul du GC
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
def gc_content(sequence):

    seq_str = str(sequence).upper()
    nb_gc = seq_str.count("G") + seq_str.count("C")
    return 100 * nb_gc / len(seq_str)
dna = Seq("ATGGCCATTGTAATGGGCCGC")
print("Séquence :", dna)
print("Contenu en GC :", round(gc_content(dna), 2), "%")
# Vérification avec la fonction intégrée de Biopython
print("Avec gc_fraction :", round(gc_fraction(dna) * 100, 2), "%")