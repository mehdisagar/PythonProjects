class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextNode = None


class LindkedList(object):
	def __init__(self, head = None):
		self.head = head
		self.size = 0

	def insertAtHead(self, data):
		newNode = Node(data)

		self.size += 1
		if self.head is not None:
			newNode.nextNode = self.head
			self.head = newNode
		else:
			self.head = newNode

	def insertAtEnd(self, data):
		newNode = Node(data)
		self.size += 1

		temp = self.head
		while temp.nextNode is not None:
			temp = temp.nextNode

		temp.nextNode = newNode
		newNode.nextNode = None

	def insertAtLocation(self, data, pose):
		if self.size < pose:
			print "Counting starts from 1.\nThe index is out of bound for the current list"
		elif self.head is None:
			self.insertAtHead(data)
		else:
			self.size += 1
			newNode = Node(data)

			counter = 1
			curNode = self.head
			preNode = None

			while counter != pose:
				curNode = curNode.nextNode
				preNode = curNode
				counter += 1
			newNode.nextNode = curNode.nextNode
			preNode.nextNode = newNode

	def deleteNode(self, data):
		if self.head is None:
			return
		self.size -= 1
		curNode = self.head
		preNode = None
		
		while curNode.data != data:
			preNode = curNode
			curNode = curNode.nextNode
			

		# deleting the head node
		if preNode is None:
			self.head = curNode.nextNode

		else:
			preNode.nextNode = curNode.nextNode

	def printList(self):
		if self.head is None:
			print "The list is empty!"

		temp = self.head
		while temp is not None:
			print ("%d" % temp.data)
			temp = temp.nextNode


if __name__ == "__main__":

	L = LindkedList()
	L.printList()
	L.insertAtHead(1)
	L.insertAtEnd(10)
	L.insertAtLocation(100,2)
	
	L.printList()

	
	
	print("The size of the list = %d" % L.size)

