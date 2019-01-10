# this program translates a DNA sequence to amino acid sequence
# so far only standard code
# it gives 5 to 3 prime amino acid sequence in 3 frames
# it also give 3 to 5 prime aa sequence in 3 frames

# dictionary relating codon to amino acid
codons = {'TTT': 'Phe', 'TTC': 'Phe', 'TTA': 'Phe', 'TTG': 'Phe',
          'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
          'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile',
          'ATG': 'Met',
          'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val',
          'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser',
          'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
          'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
          'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
          'TAT': 'Tyr', 'TAC': 'Tyr',
          'TAA': 'XXX', 'TAG': 'XXX',
          'CAT': 'His', 'CAC': 'His',
          'CAA': 'Gin', 'CAG': 'Gin',
          'AAT': 'Asn', 'AAC': 'Asn',
          'AAA': 'Lys', 'AAG': 'Lys',
          'GAT': 'Asp', 'GAC': 'Asp',
          'GAA': 'Glu', 'GAG': 'Glu',
          'TGT': 'Cys', 'TGC': 'Cys',
          'TGA': 'XXX',
          'TGG': 'Trp',
          'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
          'AGT': 'Ser', 'AGC': 'Ser',
          'AGA': 'Arg', 'AGG': 'Arg',
          'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'}

# input string 5' to 3'
dna_string = input('Enter DNA sequence:')

# reverse the string for checking 3' to 5'
dna_string_reverse = dna_string[::-1]

# empty list to hold reverse complement sequence
reverse_comp = []

# create reverse complement list
for i in dna_string_reverse:
    if i == 'A':
        reverse_comp.append('T')
    if i == 'T':
        reverse_comp.append('A')
    if i == 'G':
        reverse_comp.append('C')
    if i == 'C':
        reverse_comp.append('G')

# create string from reverse_comp list
reverse_dna = ''
for x in reverse_comp:
    reverse_dna += x

# this function handles reading frame 1
def dna_splitter1(dna):
    '''
    Doctype
    splits the sequence into codons 1st pos
    '''
    codon = ([dna[i:i+3] for i in range(0, len(dna), 3)])
    return codon

# this function handles reading frame 2
def dna_splitter2(dna):
    '''
    Doctype
    splits the sequence into codons 2nd pos
    '''
    codon = ([dna[i:i+3] for i in range(1, len(dna), 3)])
    return codon

# this function handles reading frame 3
def dna_splitter3(dna):
    '''
    Doctype
    splits the sequence into codons 3rd pos
    '''
    codon = ([dna[i:i+3] for i in range(2, len(dna), 3)])
    return codon


# handling 5'3' sequences

# call function and pass 5'3' dna string Frame 1
output1 = dna_splitter1(dna_string)

# empty list to hold the new amino acid string
list_aminos1 = []

# for loop to match codon to amino acid in dictionary
# appends the dictionary values to new list
for x in output1:
    if x in codons:
        list_aminos1.append(codons[x])

# print out the results of reading frame 1
print("5'3' Reading Frame 1:")
print(list_aminos1)

# call function and pass 5'3' dna string Frame 2
output2 = dna_splitter2(dna_string)

# empty list to hold the new amino acid string
list_aminos2 = []

# for loop to match codon to amino acid in dictionary
# appends the dictionary values to new list
for x in output2:
    if x in codons:
        list_aminos2.append(codons[x])

# print out the results of reading frame 2
print("5'3' Reading Frame 2:")
print(list_aminos2)

# call function and pass 5'3' dna string Frame 3
output3 = dna_splitter3(dna_string)

# empty list to hold the new amino acid string
list_aminos3 = []

# for loop to match codon to amino acid in dictionary
# appends the dictionary values to new list
for x in output3:
    if x in codons:
        list_aminos3.append(codons[x])

# print out the results of reading frame 3
print("5'3' Reading Frame 3:")
print(list_aminos3)


# handling 3'5' sequences

# call function and pass 3'5' dna string Frame 1
output4 = dna_splitter1(reverse_dna)

# empty list to hold the new amino acid string
list_aminos4 = []

# for loop to match codon to amino acid in dictionary
# appends the dictionary values to new list
for x in output4:
    if x in codons:
        list_aminos4.append(codons[x])

# print out the results of reading frame 1
print("3'5' Reading Frame 1:")
print(list_aminos4)

# call function and pass 3'5' dna string Frame 2
output5 = dna_splitter2(reverse_dna)

# empty list to hold the new amino acid string
list_aminos5 = []

# for loop to match codon to amino acid in dictionary
# appends the dictionary values to new list
for x in output5:
    if x in codons:
        list_aminos5.append(codons[x])

# print out the results of reading frame 2
print("3'5' Reading Frame 2:")
print(list_aminos5)

# call function and pass 3'5' dna string Frame 3
output6 = dna_splitter3(reverse_dna)

# empty list to hold the new amino acid string
list_aminos6 = []

# for loop to match codon to amino acid in dictionary
# appends the dictionary values to new list
for x in output6:
    if x in codons:
        list_aminos6.append(codons[x])

# print out the results of reading frame 3
print("3'5' Reading Frame 3:")
print(list_aminos6)