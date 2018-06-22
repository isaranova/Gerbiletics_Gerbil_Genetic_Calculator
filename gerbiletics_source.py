gene_types = {
    'a': ['A', 'a'],
    'c': ['C', 'ch', 'chm'],
	'd': ['D', 'd'],
    'e': ['E', 'e', 'ef'],
    'g': ['G', 'g'],
    'p': ['P', 'p']
}

gene_possibilities = {
    'a': ['A.A', 'A.a', 'a.a'],
    'c': ['C.C', 'C.ch', 'C.chm', 'ch.ch', 'chm.ch', 'chm.chm'],
    'd': ['D.D', 'D.d', 'd.d'],
    'e': ['E.E', 'E.e', 'E.ef', 'e.e', 'e.ef', 'ef.ef'],
    'g': ['G.G', 'G.g', 'g.g'],
    'p': ['P.P', 'P.p', 'p.p'],
}

def swap_string(string1, string2):
    temp = string1
    string1 = string2
    string2 = temp
    return string1, string2

def probability(struct, item):
    number = len(struct)
    i_number = struct.count(item)

    if i_number == 0:
        return 0

    probability = i_number / number * 100
    return probability

def letter_possibilities(type, gene):
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

class Gene:
    def __init__(self, name, type):
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

gene = Gene('a.A', 'A')
gen2 = Gene('a.a', 'a')
funky = Gene('A.-', 'a')
c = Gene('C.ch', 'c')
c2 = Gene('ch.chm', 'c')
combo = gene.gene_combinations(gen2)
combo2 = gene.gene_combinations(funky)
combo3 = c.gene_combinations(c2)
print(combo, combo2, combo3)
