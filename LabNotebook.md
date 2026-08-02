# Demultiplexing Bi622

## Assignment the First: Part 1

### 07/28/26
Initial data exploration bash commands

To get read count for all of the files:

$  zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz | wc -l

returned: 1452986940 -> divided by 4

Then I piped zcat of file to head to look at phred scores, I believe it is phred-33 since the lowest score I saw would be "#" which is not in phred-64

### 08/01/26

Repurposed populate_list function from Bi621 PS4 but will need to do sbatch scripts to run over such large files