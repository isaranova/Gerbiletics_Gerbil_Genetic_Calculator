import gerbiletics_source

def gene_status_test():
	gene = Gene('A.a', 'a')
	assert gene.name == 'A.a'
	assert gene.type == 'a'
	assert gene.one == 'A'
	assert gene.two == 'a'
	
	wrong_type = Gene('a.-', 'A')
	assert gene.name = 'a.-'
	assert gene.type = 'a'
	assert gene.one = 'a'
	assert gene.two = '-'
	
def gene_behavior_test():
	gene1 = Gene('A.a', 'a')
	gene2 = Gene('a.A', 'A')
	
	assert gene2.name = 'A.a'
	assert gene2.one = 'A'
	assert gene2.two = 'a'
	
	gene1.letter_position_correction()
	assert gene1.name = 'A.a'
	assert gene1.one = 'A'
	assert gene1.two = 'a'
	
	breed = gene1.gene_combinations(gene2)
	assert breed['A.A'] == 25.0
	assert breed['A.a'] == 50.0
	assert breed['a.a'] == 25.0
