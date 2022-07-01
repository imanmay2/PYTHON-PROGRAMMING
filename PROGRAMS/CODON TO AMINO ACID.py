codons=["AAA","AAG","AAC","AAU","GAA","GAG","GAC","GAU","CAA","CAG","CAC","CAU","UAA","UAG","UAC","UAU","AGA","AGG","AGC","AGU","GGA","GGG","GGC","GGU","CGA","CGG","CGC","CGU","UGA","UGG","UGC","UGU","ACA","ACG","ACC","ACU","GCA","GCG","GCC","GCU","CCA","CCG","CCC","CCU","UCA","UCG","UCC","UCU","AUA","AUG","AUC","AUU","GUA","GUG","GUC","GUU","CUA","CUG","CUC","CUU","UUA","UUG","UUC","UUU"]
amino=["Lysine","Lysine","Aspergine","Aspergine","Glutamine","Glutamine","Aspergine","Aspergine","Glutamine","Glutamine","Histidine","Histidine","Isoleucine","Isoleucine","Tyrocene","Tyrocene","Arginine","Arginine","Serine","Serine","Glycine","Glycine","Glycine","Glycine","Arginine","Arginine","Arginine","Arginine","Selenocysteine","Tryptophan","Cystine","Cystine","Threonine","Threonine","Threonine","Threonine","Alanine","Alanine","Alanine","Alanine","Proline","Proline","Proline","Proline","Serine","Serine","Serine","Serine","Isoleucine","Methionine","Isoleucine","Isoleucine","Valine","Valine","Valine","Valine","Leucine","Leucine","Leucine","Leucine","Leucine","Leucine","Phenylalamine","Phenylalamine"]
cod=input("ENTER THE CODON TO BE DISPLAYED: ").upper()
if(cod not in codons):
    print("SORRY!! PLZZ ENTER A VALID CODON!!!")
else:
    print(f"AMINO ACID OF {cod} CODON IS: ",amino[codons.index(cod)])
