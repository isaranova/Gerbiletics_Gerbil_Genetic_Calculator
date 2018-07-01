genotype_phenotype = {
	'Agouti': 'A.-,C.-,D.-,E.-,G.-,P.-',
	'Argente Golden': 'A.-,C.C,D.-,E.-,G.-,p.p',
	'Argente Cream': 'A.-,C.ch,D.-,E.-,G.-,p.p',
	'Grey Agouti': 'A.-,C.-,D.-,E.-,g.g,P.-',
	'Ivory Cream': 'A.-,C.C,D.-,E.-,g.g,p.p',
	'Dark Eyed Honey': 'A.-,C.-,D.-,e.e,G.-,P.-',
	'Red Eyed Honey': 'A.-,C.C,D.-,e.e,G.-,p.p',
	'Polar Fox ': 'A.-,C.-,D.-,e.e,g.g,P.-',
	'Red Eyed Polar Fox': 'A.-,C.-,D.-,e.e,g.g,p.p',
	'Black': 'a.a,C.-,D.-,E.-,G.-,P.-',
	'Blue': 'a.a,C.-,d.d,E.-,G.-,P.-',
	'Slate': 'a.a,C.-,D.-,E.-,g.g,P.-',
	'Lilac': 'a.a,C.C,D.-,E.-,G.-,p.p',
	'Dove': 'a.a,C.ch,D.-,E.-,G.-,p.p',
	'Ruby Eyed White': 'a.a,C.-,D.-,E.-,g.g,p.p',
	'Nutmeg': 'a.a,C.-,D.-,e.e,G.-,P.-',
	'Argente Nutmeg': 'a.a,C.C,D.-,e.e,G.-,p.p',
	'Pale Argente Nutmeg': 'a.a,C.ch,D.-,e.e,G.-,p.p',
	'Silver Nutmeg': 'a.a,C.-,D.-,e.e,g.g,P.-',
	'Schimmel': '-.-,C.-,D.-,ef.ef,G.-,P.-',
	'Red Eyed Schimmel  ': '-.-,C.-,D.-,ef.ef,G.-,p.p',
	'Topas': 'A.-,C.chm,D.-,E.-,G.-,p.p',
	'Colourpoint Grey Agouti': 'A.-,chm.chm,D.-,E.-,g.g,P.-',
	'Burmese': 'a.a,chm.chm,D.-,E.-,G.-,P.-',
	'Siamese': 'a.a,chm.ch,D.-,E.-,G.-,P.',
	'Sapphire': 'a.a,C.chm,D.-,E.-,G.-,p.p',
	'Colourpoint Nutmeg': 'a.a,chm.chm,D.-,e.e,G.-,P.-',
	'Colourpoint Silver Nutmeg': 'a.a,chm.chm,D.-,e.e,g.g,P.-',
	'Dark Tailed White': '-.-,ch.ch,D.-,-.-,-.-,P.-',
	'Pink Eyed White': '-.-,ch.ch,D.-,-.-,-.-,p.p',
}

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

gene_order = {
    0: 'a',
    1: 'c',
    2: 'd',
    3: 'e',
    4: 'g',
    5: 'p'
}
