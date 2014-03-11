dic = {
	'marco': 'desk 1',
	'giulio': 'desk 2',
	'mike': 'room 3'
}

def dict_values_ascending(dictionary):
	values = dictionary.values()
	values.sort()
	return values

print dict_values_ascending(dic)