class Queue():
	"""The implementation of Queue abstarct data type using array"""
	def __init__(self):
		self.queue = []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def isEmpty(self):
		return self.queue == []

	def sizeQ(self):
		return len(self.queue)

	def printQ(self):
		for i in range(len(self.queue)):
			print self.queue[i]




if __name__ == "__main__":

	queue = Queue()

	for i in range(10):
		queue.enqueue(i)

	print("The dequeued valud : ", queue.dequeue())
	queue.printQ()

