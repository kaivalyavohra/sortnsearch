from random import randint
#gen random number array
def gen(size,minimum,maximum):
	arr = []
	for i in range(size):
		arr.append(randint(minimum,maximum))
	return(arr)
