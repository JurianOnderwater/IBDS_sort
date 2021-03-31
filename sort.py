genes_upregulated = open("/Users/jurianonderwater/Documents/Bioinformatics/IBDS/genes_upregulated.txt", 'r')
genes_upregulated = genes_upregulated.read()
genes_upregulated = genes_upregulated.split('\n')
genes_upregulated = [x.split('\t') for x in genes_upregulated]

up_25up = [x[0] for x in genes_upregulated if float(x[1]) > 25]
up_2499to10 = [x[0] for x in genes_upregulated if (float(x[1]) < 24.99 and float(x[1]) > 10)]
up_999to5 = [x[0] for x in genes_upregulated if (float(x[1]) < 9.99 and float(x[1]) > 5)]
up_499to25 = [x[0] for x in genes_upregulated if (float(x[1]) < 4.99 and float(x[1]) > 2.5)]
up_249to15 = [x[0] for x in genes_upregulated if (float(x[1]) < 2.49 and float(x[1]) > 1.5)]




genes_downregulated = open("/Users/jurianonderwater/Documents/Bioinformatics/IBDS/genes_downregulated.txt", 'r')
genes_downregulated = genes_downregulated.read()
genes_downregulated = genes_downregulated.split('\n')
genes_downregulated = [x.split('\t') for x in genes_downregulated]

down_066to04 = [x[0] for x in genes_downregulated if (float(x[1]) < 0.66 and float(x[1]) > 0.4)]
down_039to02 = [x[0] for x in genes_downregulated if (float(x[1]) < 0.39 and float(x[1]) > 0.2)]
down_019to01 = [x[0] for x in genes_downregulated if (float(x[1]) < 0.19 and float(x[1]) > 0.1)]
down_009down = [x[0] for x in genes_downregulated if float(x[1]) < 0.09 ]

for gene in down_009down:
    print(gene + ',')