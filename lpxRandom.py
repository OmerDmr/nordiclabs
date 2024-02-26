import random
import string


def get_random_string(length):

	i = 0
	
	randomCodes = []
	
	letters = string.ascii_uppercase
	digits = string.digits
	result_str = ''.join(random.choice(letters + digits) for i in range(length))
	code = 'LPX' + '-' + result_str
	randomCodes.append(code)
	
	f = open("codes.txt", "a")
	while i<10000:
		# choose from all lowercase letter
		result_str = ''.join(random.choice(letters + digits) for i in range(length))
		code = 'NRD' + '-' + result_str
		
		k = 0
		while k < len(randomCodes) and code != randomCodes[k]:
			k = k+1
		
		if code != randomCodes[k-1]:
			randomCodes.append(code)
			f.write(code)
			f.write('\n')
			print("Code:", length, "is:", code)	
			i= i+1
	f.close()
		
	
get_random_string(8)
