from gerbiletics_source import *

def test_gene_status():
	gene = Gene('A.a', 'a')
	assert gene.name == 'A.a'
	assert gene.type == 'a'
	assert gene.one == 'A'
	assert gene.two == 'a'
	
	wrong_type = Gene('a.-', 'A')
	assert wrong_type.name == 'a.-'
	assert wrong_type.type == 'a'
	assert wrong_type.one == 'a'
	assert wrong_type.two == '-'
	
def test_gene_behavior():
	gene1 = Gene('A.a', 'a')
	gene2 = Gene('a.A', 'A')
	gene3 = Gene('C.C', 'c')
	gene4 = Gene('ch.ch', 'c')
	gene5 = Gene('chm.ch', 'c')
	gene6 = Gene('C.ch', 'c')

	assert gene2.name == 'A.a'
	assert gene2.one == 'A'
	assert gene2.two == 'a'
	
	gene1.letter_position_correction()
	assert gene1.name == 'A.a'
	assert gene1.one == 'A'
	assert gene1.two == 'a'
	
	breed = gene1.gene_combinations(gene2)
	assert breed['A.A'] == 25.0
	assert breed['A.a'] == 50.0
	assert breed['a.a'] == 25.0
	
	breed2 = gene3.gene_combinations(gene3)
	assert breed2['C.C'] == 100.0

	breed3 = gene6.gene_combinations(gene5)
	assert breed3['C.ch'] == 25.0
	assert breed3['C.chm'] == 25.0
	assert breed3['ch.chm'] == 25.0
	assert breed3['ch.ch'] == 25.0

	breed4 = gene4.gene_combinations(gene5)
	assert breed4['ch.chm'] == 50.0
	assert breed4['ch.ch'] == 50.0

def test_genotype_status():
	mama = Genotype('A.a,C.chm,D.d,ef.ef,G.g,P.P')
	assert mama.name == 'A.a,C.chm,D.d,ef.ef,G.g,P.P'

	a,c,d,e,g,p = mama.name.split(',')
	names = [a,c,d,e,g,p]

	for i in range(6):
		assert mama.genes[i].name == names[i]


def test_genotype_to_phenotype():
	mama = Genotype('A.a,C.chm,D.d,ef.ef,G.g,P.P')
	papa = Genotype('a.a,C.C,D.d,E.e,G.g,P.p')

	assert mama.genotype_to_phenotype() == ['Schimmel']
	assert papa.genotype_to_phenotype() == ['Black']
	

def test_genotype_combination():
	mama = Genotype('A.a,C.chm,D.D,e.e,G.g,P.P')
	papa = Genotype('a.a,C.C,D.D,E.E,g.g,P.p')
	dominant = Genotype('A.A,C.C,D.D,E.E,G.G,P.P')
	recesive = Genotype('a.a,chm.chm,d.d,e.e,g.g,p.p')

	p1 = dominant.genotype_combination(dominant)
	p2 = recesive.genotype_combination(dominant)
	p3 = mama.genotype_combination(papa)
	p4 = papa.genotype_combination(mama)

	assert len(p1) == 1
	assert p1[0][2] == 100.0
	assert p1[0][1] == ['Agouti']
	o1 = Offspring(p1[0])
	assert o1.genotype == 'AA CC DD EE GG PP'

	assert len(p2) == 1
	assert p2[0][2] == 100.0
	assert p2[0][1] == ['Agouti']
	o2 = Offspring(p2[0])
	assert o2.genotype == 'Aa Cchm Dd Ee Gg Pp'
	
	assert len(p3) == 16
	
	for i in range(len(p3) -1):
		assert p3[i][2] == p3[i+1][2]
	
	assert only_phenotypes(p3)["['Agouti']"] == 25.0
	assert only_phenotypes(p3)["['Grey Agouti']"] == 25.0
	assert only_phenotypes(p3)["['Black']"] == 25.0
	assert only_phenotypes(p3)["['Slate']"] == 25.0
	
	assert p3 == p4
	


