# Given: DNA string of length s at most 1000 bp. 
# Returns: reverse complement of s, reverse_complement 
# Every C <> G  and T <> A 
#Initializes reverse_complement string 
reverse_complement=""

#Asks user to input DNA strand sequence and places it in variable s
s = input ("Please enter DNA strand sequence of < 1000 bp")

#Loops until the length of string < 1000 
while len(s)>1000:
    s=input("Please enter a length of DNA < 1000 bp")

#Reverse is the reverse of string s 
reverse = s [::-1] 

#For every element in the reverse strand converts to the complement nt. 
for element in reverse:
    if element == "C":
        reverse_complement=reverse_complement+"G"
    elif element == "G":
        reverse_complement=reverse_complement+"C"
    elif element == "T":
        reverse_complement=reverse_complement+"A"
    elif element == "A":
        reverse_complement=reverse_complement+"T"
    else: 
        print("Base pair"+element+"does not exist")
        exit 
GTACTGCTGCACAAGTTGCATCGATGCGGTACACATAGACATTCCATCCTCTCGTAAGGCTAGCCTGGCTAAGCTCAGGCCACGACCAAGATGCCAGCTCTCCCGATAATGAGCTACCTATGCCCAGAATGGTCCAGCAGGCGAACAGTGTAGACGGCTAGGAGTCTTGAAGCCAGTGTTATGAGAATCGATGGCTACGAGCATGCCCCTCCCGGCGTAATGTACGGGGTCTCAGCTCAAGACGGCTACGACAGAGTGATCAGAAGTAGGAGAACTGTTCGTATAACAACAACTTGAATGTGTGTCGCGAACGAGGCTTCGTAATTCACTTAGATCGTCGGTACGTCAAGATTGACCGTCACTGTCCCCGGTACGTTAGTACGAATCTGACAGGGAGCATATTCGTTAGCACTGAAGCTATCGGATTATCAAGATGTCCGAGTATGGCACCGCGGGCCCAGTATACGAGGTGTGACATCTGTAGACAAAGACTCGAACATCCATACGAGGTATCACACAATGCCCCTGGAGTCTCTCCCTGCCCCAAGACCAACAAAGCATTGACAGCTAGTCATTGAGACTTTATCCAGGAGATTGCTCCATTCACCACCTCTCCACCCTAATGAGGGCAGACTTTGTCCAGAGACTAACGCCAATTAAATGCTCAATCCGTCTCTTGAAAATCAGCCACAAAGACTTATATGTGATACCAGTACGGGACCTTAGAGGTGTGTATCGCTAGACGATTCTCACGGTCAAAGGACCGCGCTTTCACAGTCTGCTCCGGCTCGCGACTATCTACGCGTTCGAAACCTTGTTTCCTGAGCTAGCCATATAAAGGTTTTCGCCCATGTAGGGACTATAGTAGGTTCGTCCTCTGTACTGCCTACAGGATTTTGCCTCCCTGAATCGTTGCCGGTCGAAAAAAGGCACAACAGGCGTGTCATCTTGATGTGATCGAGAAGCTGCTACGAAAG

print(reverse_complement)



