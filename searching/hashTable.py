''' The aim is to build a DS to improve the time complexity
    for accessing the data to O(1). This is what built-in DS
    like dictionaries are providing in Python for example.
'''

class hashTable(object):
	"""docstring for hashTable"""
	def __init__(self, size):
		
		self.size = size
		self.keys = [None] * self.size
		self.values = [None] * self.size

	def put_data(self, key, data):
		
		indx = self.hach_func(key)

		#The while block is for rehashing in case of collisions
		while self.keys[indx] is not None:
			if self.keys[indx] == key:
				self.values[indx] = data
				return

			indx = (indx + 1)% self.size

		self.keys[indx] = key
		self.values[indx] = data

	def hach_func(self, key):
		sum = 0
		for char in range(len(key)):
			sum += ord(key[char])

		return sum%self.size

	def get_data(self, key):

		indx = self.hach_func(key)

		# in case we have done rehashing when inserting to the table
		while self.keys[indx] is not None:
			if self.keys[indx] == key:
				return self.values[indx]

			indx = (indx + 1) % self.size

		return None


if __name__ == "__main__":
	H = hashTable(10)
	H.put_data('Mehdi', 29)
	H.put_data('Sagar', 89)
	#print(H.get_data('mehdi'))
	for i, j in zip(H.keys, H.values):
		if i is not None or j is not None:
			print "The age of {} is {}".format(i, j)

	print H.keys
	print H.values

	