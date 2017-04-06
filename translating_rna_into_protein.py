import sys

file_path = sys.argv[1]
rna_string = ''
protein_string = ''

codon_dict = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    			"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    			"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    			"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    			"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    			"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    			"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    			"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    			"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    			"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    			"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    			"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    			"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    			"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    			"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    			"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

with open(file_path, 'r') as f:
	rna_string = f.readline()

#split into codons
rna_string = [rna_string[i:i+3] for i in range(0,len(rna_string), 3)]
for codon in rna_string:
	if codon_dict[codon] == 'STOP':
		break
	else:
		protein_string += codon_dict[codon]

print protein_string