# Cellule 3 : Opérations biologiques
from Bio.Seq import Seq
dna = Seq("ATGGCCATTGTAATGGGCCGC")
print("Séquence originale :", dna)
print("Complément :", dna.complement())
print("Complément inverse :", dna.reverse_complement())
print("Transcription en ARNm :", dna.transcribe())