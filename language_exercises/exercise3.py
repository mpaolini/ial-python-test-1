def count_line_inFile(file_name):
	in_f = open(file_name, "rb")
	i = -1
	for line in in_f:	
		i += 1
	return i

print count_line_inFile("text.txt")