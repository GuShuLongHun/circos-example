#!/usr/bin/python

from Bio import SeqIO

record = SeqIO.parse("EU078592.gbk", "genbank").next()
name = "DE3"
with open('EU078592.genes.list.txt', 'w') as f:
    for feature in record.features:
        if feature.type == 'CDS':
            d = feature.qualifiers
            if 'gene' in d:
                gene = d['gene'][0]
            else:
                gene = d['locus_tag'][0]
            if 'product' in d:
                product = d['product'][0]
            elif 'note' in d:
                product = d['note'][0]
            else:
                product = ''
            location = feature.location
            strand, start, end =  location.strand, location.start, location.end

            if strand == -1:
                start, end = end, start
            f.write("{}\t{}\t{}\t{}-{}\n".format(name, start, end, gene, product))


record = SeqIO.parse("J02459.gbk", "genbank").next()
name = "lambda"
with open('J02459.genes.list.txt', 'w') as f:
    for feature in record.features:
        if feature.type == 'CDS':
            d = feature.qualifiers
            if 'product' in d:
                gene = d['product'][0]
            else:
                raise Exception("error, {}".format(d))
            location = feature.location
            strand, start, end =  location.strand, location.start, location.end

            if strand == -1:
                start, end = end, start
            f.write("{}\t{}\t{}\t{}\n".format(name, start, end, gene))
