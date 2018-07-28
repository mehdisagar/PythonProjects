class Stack():
	"""implementing stack abstract data type using array"""
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		print(self.stack == [])

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def sizeOfStack(self):
		return len(self.stack)

	def printStack(self):
		for i in range(len(self.stack)):
			print (self.stack[i])



if __name__ == "__main__":

	stack = Stack()
	stack.isEmpty()
	stack.push(10)
	stack.push(100)
	stack.push(1000)
	stack.printStack()
	print("The popped value = ", stack.pop())
	stack.printStack()
	print("The current size of the stack = ", stack.sizeOfStack())

		