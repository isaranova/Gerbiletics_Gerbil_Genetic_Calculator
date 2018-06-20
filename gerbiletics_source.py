gene_types = {
    'a': ['A', 'a'],
    'c': ['C', 'ch', 'chm'],
	'd': ['D', 'd'],
    'e': ['E', 'e', 'ef'],
    'g': ['G', 'g'],
    'p': ['P', 'p']
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

    return i_number / number * 100


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
            if self.two == gene_types[self.type][2] and self.one == gene_types[self.type][1]:
                self.one, self.two = swap_string(self.one, self.two)

    def gene_combinations(self, gen2):
        combinations = dict()
        genotypes = list()

        gen1 = [self.one, self.two]
        gen2 = [gen2.one, gen2.two]

        for i in gen1:
            for y in gen2:
                if (gen1 or gen2) == '-':
                    gen = list()
                    for letter in gene_types[self.type]:
                        g = Gene(gen1+'.'+gen2, self.type)
                        g.name.replace('-', letter)
                        g.letter_position_correction()
                        gen.append(g)

                gen = Gene(gen1+'.'+gen2, self.type)
                gen.letter_position_correction()
                genotypes.append(gen)

        for g in genotypes:
            if g not in combinations:
                combinations[g] = probability(genotypes, g)

		return combinations
