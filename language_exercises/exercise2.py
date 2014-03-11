dict_1 = {
	'marco': 'desk 1',
	'giulio': 'desk 2',
	'mike': 'room 3'
}

dict_2 = {
	'zubat': 'grotta',
	'rattata': 'erba',
	'magikarp': 'acqua'
}

def add_dict(dict_1, dict_2):
	dict_3 = {}
	for x in dict_1: 
		dict_3[x] = dict_1[x]
	for x in dict_2:
		dict_3[x] = dict_2[x]
	return dict_3

print add_dict(dict_1, dict_2)