#!/usr/bin/python

# note! - gbk files downloaded with efetch are different with those downloaded from ftp, and gbk files from ftp site are well annotated.

from Bio import SeqIO

# record = SeqIO.parse("DE3_EU078592.gb", "genbank").next()
# name = "DE3"
# with open('DE3.genes.list.txt', 'w') as f:
#     for feature in record.features:
#         if feature.type == 'gene':
#             d = feature.qualifiers
#             if 'gene' in d:
#                 gene = d['gene'][0]
#             else:
#                 gene = d['locus_tag'][0]
# 
#             location = feature.location.parts
#             for part in location:
#                 strand, start, end = part.strand, part.start, part.end
# 
#                 if strand == -1:
#                     start, end = end, start
#                 f.write("{}\t{}\t{}\t{}\n".format(name, start, end, gene).replace(' ', '_'))


def gbk2genelist(gbk_file, out_file, name):
    record = SeqIO.parse(gbk_file, "genbank").next()
    with open(out_file, 'w') as f:
        for feature in record.features:
            if feature.type == 'gene':
                d = feature.qualifiers
                if 'gene' in d:
                    gene = d['gene'][0]
                else:
                    gene = d['locus_tag'][0]

                location = feature.location.parts
                for part in location:
                    strand, start, end = part.strand, part.start, part.end

                    if strand == -1:
                        start, end = end, start
                    f.write("{}\t{}\t{}\t{}\n".format(name, start, end, gene).replace(' ', '_'))

gbk_file = "DE3_EU078592.gb"
name     = "DE3"
out_file = "DE3.genes.list.txt"
gbk2genelist(gbk_file, out_file, name)

gbk_file = "NC_001416.gbk"
name     = "lambda"
out_file = "lambda.genes.list.txt"
gbk2genelist(gbk_file, out_file, name)
