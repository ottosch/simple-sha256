def print_bits(input):
	"""Print input in groups of 8 bits (binary)"""
	s = ""
	count = 1
	for b in input:
		s += bin(b)[2:].rjust(8, "0")
		if count % 8 == 0:
			s += "\n"
		else:
			s += " "
		count += 1
  
	print(s.strip())
 
def print_hex(input):
	"""Print input in groups of 4 bytes (hexadecimal)"""
	s = ""
	count = 1
	for b in input:
		s += hex(b)[2:].rjust(2, "0")
		if count % 32 == 0:
			s += "\n"
		elif count % 4 == 0:
			s += " "
		count += 1
  
	print(s.strip())
 
def print_words(input):
	"""Print input in groups of 2 words (4 bytes each, binary)"""
	s = ""
	count = 1
	for b in input:
		s += bin(b)[2:].rjust(32, "0")
		if count % 2 == 0:
			s += "\n"
		else:
			s += " "
		count += 1
  
	print(s.strip())
 
def print_words_hex(input):
	"""Print input in groups of 2 words (4 bytes each, hexadecimal)"""
	s = ""
	count = 1
	for b in input:
		s += hex(b)[2:].rjust(8, "0")
		if count % 8 == 0:
			s += "\n"
		else:
			s += " "
		count += 1
  
	print(s.strip())