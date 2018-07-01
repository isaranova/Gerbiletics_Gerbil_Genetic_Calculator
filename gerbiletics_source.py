from support_file import genotype_phenotype, gene_order, gene_possibilities, gene_types
import itertools

def swap_string(string1, string2):
    """Function gets two string parameters and swaps their content, returning
    swapped contents as two variables"""
    temp = string1
    string1 = string2
    string2 = temp
    return string1, string2

def probability(struct, item):
    """Function counts probability by the count of item present in the struct,
    parameters are structure with items and item form the structure, returns probability
    of item in the structure in percents"""
    number = len(struct)
    i_number = struct.count(item)

    if i_number == 0:
        return 0

    probability = i_number / number * 100
    return probability

def letter_possibilities(type, gene):
    """Function finds all alleles that complete the missing allele in gene with '-',
    parameters are the type of gene and gene itself, returns list of all possible
    letters"""
    gen1, gen2 = gene.split('.')

    if gen1 == '-' and gen2 == '-':
        return gene_possibilities[type]

    elif gen1 == '-' or gen2 == '-':
        possibilities = list()
        gene = gene.replace('-', '')
        for p in gene_possibilities[type]:
            if gene in p:
                possibilities.extend(p.split('.'))
        return possibilities

    else:
        return [gen1, gen2]

def genotype_probability(genotype, complete_gene_combo):
    """Function counts probability of complete genotype by multiplying the gene probabilities and then
    dividing them by appropriate power of 100, parameters are the genotype and complete gene probabilities for all
    offsprings of the original parents, returns probability of the genotype"""
    probability = 1
    for i in range(len(complete_gene_combo)):
          probability *= complete_gene_combo[i][genotype[i]]

    return probability / (100**5)

def only_phenotypes(list_complete):
    """Function creating dictionary of phenotypes and their probabilities, which are obtained from the complete
    genotype - phenotype - probability list and basically sums the probabilities of each phenotype, parameter is
    the complete list of genotype - phenotype - probability combinations, returns dictionary with phenotype as key
    and its probability as value"""
    only_phenotypes = dict()

    for i in range(len(list_complete)):
        color = str(list_complete[i][1])
        if color not in only_phenotypes:
            only_phenotypes[color] = list_complete[i][2]
        else:
            new_value = only_phenotypes[color] + list_complete[i][2]
            only_phenotypes[color] = new_value

    return only_phenotypes

def print_only_phenotypes(list_complete):
    """Function simply prints the only phenotypes dictionary sorted by its value in descending order, parameter is
    the complete list of genotype - phenotype - probability combinations"""
    dict_only_phenotypes = only_phenotypes(list_complete)
    for p in sorted(dict_only_phenotypes, key=dict_only_phenotypes.get, reverse=True):
        print(p, str(dict_only_phenotypes[p]) + ' %')

class Gene:
    """Class designed for working with gene which consists of dominant or recessive alleles"""
    def __init__(self, name, type):
        """Function initializing the gene structure for easy manipulation in code, setting atributes
        name from first parameter of the function, type from second parameter that is also automatically
        changed to lower alphabetical character, one the first allele, two the second allele and then correcting
        the alleles position accoring to rules of domination in genes"""
        self.name = name
        self.type = type.lower()
        self.one, self.two = self.name.split('.')
        self.letter_position_correction()

    def letter_position_correction(self):
        if self.two == gene_types[self.type][0]:
            self.one, self.two = swap_string(self.one, self.two)

        if self.type == ('e' or 'c'):
            if self.two == gene_types[self.type][1] and self.one == gene_types[self.type][2]:
                self.one, self.two = swap_string(self.one, self.two)

        self.name = self.one + '.' + self.two

    def gene_combinations(self, gen2):
        combinations = dict()
        genotypes = list()

        gen1 = letter_possibilities(self.type, self.name)
        gen2 = letter_possibilities(gen2.type, gen2.name)

        for i in gen1:
            for y in gen2:
                gen = Gene(i+'.'+y, self.type)
                genotypes.append(gen.name)

        for g in genotypes:
            if g not in combinations:
                combinations[g] = probability(genotypes, g)

        return combinations

class Genotype:
    def __init__(self, name):
        self.name = name
        a_gene, c_gene, d_gene, e_gene, g_gene, p_gene = self.name.split(',')
        self.genes = [Gene(a_gene, gene_order[0]),
                      Gene(c_gene, gene_order[1]),
                      Gene(d_gene, gene_order[2]),
                      Gene(e_gene, gene_order[3]),
                      Gene(g_gene, gene_order[4]),
                      Gene(p_gene, gene_order[5])
        ]

    def genotype_to_phenotype(self):
        phenotypes = list()

        for p, g in genotype_phenotype.items():
            g = Genotype(g)
            for i in range(len(self.genes)):
                if g.genes[i].name.replace('-', '') not in self.genes[i].name.replace('-',''):
                    break
                else:
                    if i == len(self.genes) - 1:
                        phenotypes.append(p)

        if phenotypes == []:
            phenotypes.append('Unknown')

        return phenotypes

    def gene_combinations_complete(self, other):
        complete_gene_combo = list()
        for i in range(len(self.genes)):
            combo = self.genes[i].gene_combinations(other.genes[i])
            complete_gene_combo.append(combo)

        return complete_gene_combo


    def genotype_combination(self, other):
        complete_gene_combo = self.gene_combinations_complete(other)
        genotypes = list()

        for i in range(len(complete_gene_combo)):
            gene_combo = list(complete_gene_combo[i].keys())
            genotypes.append(gene_combo)

        genotype_combinations = list(itertools.product(*genotypes))

        genotype_phenotype_probability = list()
        for g in genotype_combinations:
            item = list()
            gg = Genotype(','.join(g))
            item.extend([g, gg.genotype_to_phenotype(), genotype_probability(g, complete_gene_combo)])
            genotype_phenotype_probability.append(item)

        return genotype_phenotype_probability

class Offspring:
    def __init__(self, list_item_offspring):
        self.genotype = ' '.join(list(list_item_offspring[0])).replace('.', '')
        self.phenotype = ', '.join(list_item_offspring[1])
        self.probability = str(list_item_offspring[2]) + ' %'
        self.complete = self.genotype + '\t' + self.phenotype + '\t' + self.probability


gene = Gene('a.A', 'A')
gen2 = Gene('a.a', 'a')
funky = Gene('A.-', 'a')
c = Gene('C.ch', 'c')
c2 = Gene('ch.chm', 'c')
combo = gene.gene_combinations(gen2)
combo2 = gene.gene_combinations(funky)
combo3 = c.gene_combinations(c2)
print(combo, combo2, combo3)

mama = Genotype('A.A,C.C,D.D,e.e,G.g,P.p')
papa = Genotype('a.a,C.C,D.d,E.e,G.g,P.p')
offspring = mama.genotype_combination(papa)

for i in range(len(offspring)):
    babe = Offspring(offspring[i])
    print(babe.complete)

print_only_phenotypes(offspring)
