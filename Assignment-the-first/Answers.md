# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here: /projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/Assignment-the-first/part1.py


| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | read1 | 363,246,735 | Phred-33 |
| 1294_S1_L008_R2_001.fastq.gz | index1 | 363,246,735 | Phred-33 |
| 1294_S1_L008_R3_001.fastq.gz | index2 | 363,246,735 | Phred-33 |
| 1294_S1_L008_R4_001.fastq.gz | read2 | 363,246,735 | Phred-33 |

2. Per-base NT distribution

    1. ![Index 1 Mean Quality Scores Per base](/projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/Assignment-the-first/Index_1_dist.png)
    2. ![Index 2 Mean Quality Scores Per Base](/projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/Assignment-the-first/Index_2_dist.png)
    3. ![Read 1 Mean Quality Scores Per Base](/projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/Assignment-the-first/Read_1_dist.png)
    4. ![Read 2 Mean Quality Scores Per Base](/projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/Assignment-the-first/Read_2_dist.png)
    
## Part 2
1. Define the problem:  We have Illumina sequencing data for multiple projects/samples/labs on one run. In order to identify samples barcodes were added to both ends of the sequences. Barcodes at both ends helps determine if index hopping occured where during sequence amplification the barcodes from a different sample ended up in the sequence. This code will go through the sequence of each read and the corresponding barcode reads to identify who the sample belongs too and if the indexes were hopped.

2. Describe output: Since we have 24 barcodes we expect 48 read files, 24 forward read and 24 reverse and count how many reads for each barcode. We will also make two index hopped files for forwaard and reverse reads, and two unknown files for forward and reverse reads.

3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).

INPUT TEST FILES:
/projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ

EXPECTED OUTPUT FILES:
/projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/TEST-output_FASTQ

4. Pseudocode: /projects/bgmp/jordanro/bioinfo/Bi622/Demultiplex/Assignment-the-first/Pseudocode.md
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement

  
rev_compliment:(seq: str) -> str:
  ''' Takes string of sequence, reverse sequence and turns A to T, T to A, G to C, C to G, and N to N '''
  return rev_str

  IN: "NCTTGCAA"
  OUT: "TTGCAAGN"