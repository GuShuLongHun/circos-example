lastdb lambda NC_001416.fna
lastal lambda EU078592.fa > DE3_aligned_to_lambda.maf
# manually edit DE3_aligned_to_lambda.maf to get links.txt
python gbk2genes.py   # will generate DE3.genes.list.txt, lambda.genes.list.txt
circos -conf phage.conf -debug_group textplace | grep not_placed
