#!/usr/bin/env python

# Author: <Jordan Rodgers> <jordanro@uoregon.edu>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.5"   #Bi622 for demultiplexing
# Read way more about versioning here
# # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = ["A","T","C","G"]
RNA_bases = ["A", "U","C","G"]

def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''

    i = 0
    while len(lst) < 101:
        lst.append(value)

    return lst

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''

    return ord(letter) - 33

def qual_score(phred_score: str) -> float:
    """calculates average q score from phred score
    uses convert_phred to get q score for each base then averages"""

    x = 0
    q_sum = 0

    for pos in phred_score:
        x += 1
        pos = convert_phred(pos)
        q_sum += pos
    print(x)
    return q_sum/len(phred_score)

    pass

def validate_base_seq(seq: str, RNAflag:bool):
    '''This function takes a sequence string, and RNAflag (True or False). Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    seq = seq.upper()
    return len(seq) == seq.count("A") + seq.count("U" if RNAflag else "T") + seq.count("C") + seq.count("G")

    pass

def gc_content(DNA: str):
    '''Returns GC content of a DNA sequence as a decimal between 0 and 1.'''
    DNA = DNA.upper()
    Gs = DNA.count("G")
    Cs = DNA.count("C")
    return (Gs + Cs) / len(DNA)

    pass

def calc_median(lst: list):
    '''Given a sorted list, returns the median value of the list'''
    x = len(lst)
    middle = x//2

    if x%2 == 0:
        return (lst[middle] + lst[middle-1])/2
    elif x%2 == 1:
        return lst[middle]
    else:
        print(f'something is wrong')

    pass

def oneline_fasta(file1,file2):
    '''Takes in fasta file and makes every sequence one line instead of multiple'''
    #print(f"reading from {file1} and writing to {file2}")
    with open(file1, "r") as filein: ### open read in file
        with open(file2, "w") as fileout: ### open file to write out
            seq_str:str = "" ### intialize empy string for sequence
            for line in filein: ### loop through each line
                if not line.startswith(">"): ### if line is not a header
                    #print(f"seq:\t{line}")
                    seq_str += line.strip() ### add sequence to string
                else:
                    #print(f"should be a header:\t{line}")
                    if seq_str != "": ### if string is empty (first header in file)
                        fileout.write(f"{seq_str}\n") ### write every header with newline character in front
                        seq_str = "" ### clearing string to use for next read
                    fileout.write(line) ### write header to output file as is
            fileout.write(seq_str)   ### writing out final string

    pass

def rev_comp(rev_barcode:str)->str:
    ''' takes a DNA barcode string from reverse barcode and makes it a list of characters, reverses the list, and changes to complementary DNA string'''
    DNA_comp:dict = {"A":"T", "T": "A", "C":"G", "G":"C", "N":"N"}
    #RNA_comp:dict = {"A":"U", "U": "A", "C":"G", "G":"C", "N":"N"}


    revBarcode:list = rev_barcode.split() ### making string a list
    barcode_lst:list = revBarcode[::-1] ### reversing rev barcode to get the complementary foward base list

    barcode:list = [] ### initializing empty list for new barcode

    for i in barcode_lst:
        barcode.append = DNA_comp[i]

    fin_barcode:str = "".join(barcode)

    return fin_barcode


if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    # These tests are run when you execute this file directly (instead of importing it)
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")
    ### validate base seq asserts
    assert validate_base_seq("AATAGAT") == True, "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
    print("Passed DNA and RNA tests")
    ### gc content asserts
    assert gc_content("GCGCGC") == 1
    assert gc_content("AATTATA") == 0
    assert gc_content("GCATCGAT") == 0.5
    print("correctly calculated GC content")
    ### quality score asserts
    assert qual_score("I","I","C","D") == 37.25, "Quality score not working"
    assert qual_score("I","I") == 40.0, "Quality score really not working"
    ### calc median asserts
    assert calc_median([1,1,1,3,4,5,6,9]) == 3.5, "Calc median does not work for even list"
    assert calc_median([1,3,4,5,6]) == 4, "Calc median does not work for odd list"
    ### rev_comp asserts
    assert rev_comp("GCATCGNT") == ["ANCGATGC"], "rev_comp does not return reverse compliment"
    assert rev_comp("NATGCCGN") == ["NCGGCATN"], "rev_comp does not return reverse compliment"
    assert rev_comp("AAACTGCA") == ["TGCAGTTT"], "rev_comp does not return reverse compliment"