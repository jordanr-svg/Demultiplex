#!/usr/bin/env python
import bioinfo
import argparse
import matplotlib.pyplot as plt
import gzip

### arguments for oneline fasta function
def my_args():
    parser = argparse.ArgumentParser(description="fastq file arguements")
    parser.add_argument("-f","--filename", type = str, required = False, help = "Input file name, fastq files to be demultiplexed")
    parser.add_argument("-p","--prefix",type = str, required = False, help ="prefix based on which input file, should be Read_1/2 or Index_1/2")
    return parser.parse_args()
args = my_args()


file = args.filename
prefix = args.prefix

"""Take fastq file and read each phred score line, convert each phred score to 
qscore (using bioinfo.convert_phred function) and sum scores from same read.
Stores qscore sums to list score_list, length of score list should equal number of reads from fastq"""

### defining variables, empty list for phred scores
score_list:list = []

### for read lists
#score_list = bioinfo.init_list(score_list)

### for index lists
i = 0.0
while len(score_list) < 8:
    score_list.append(i)


### opening fastq file and printing lines with quality scores
with gzip.open(file, "rt") as fq:
    i = 0
    for line in fq:
        i+=1
        line = line.strip('\n')
        if i%4 == 0:
            ### read character by character in line
            ### iterating over phred scores to convert to qscore AND
            ### summing qscores at that position
            for pos, letter in enumerate(line):

                score_list[pos] += bioinfo.convert_phred(letter)

num = 0
for score in score_list:
    score_list[num] = score/(i/4)
    num += 1


plt.plot(score_list)
plt.xlabel('# Base Pair')
plt.ylabel('Mean Quality Score')
plt.title(f'Mean Illumina Quality Scores For Bases At Each Index in {prefix}')
plt.savefig(f'{prefix}_dist.png')