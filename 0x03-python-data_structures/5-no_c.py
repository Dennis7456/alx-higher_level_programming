def no_c(my_string):
	string_list = list(my_string)
	index_to_replace = 0
	for i in string_list:
		if i == 'c' or i == 'C':
			string_list[index_to_replace] = ""
		index_to_replace += 1
	return "".join(string_list)
