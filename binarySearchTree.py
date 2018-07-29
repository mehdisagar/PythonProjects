class Node(object):
	"""class for Node in the tree"""
	def __init__(self, data):
		
		self.data = data
		self.leftChild = None
		self.rightChild = None

class BinarySearchTree(object):
	def __init__(self, root = None):
		self.root = root

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(data, self.root)

	def insertNode(self, data, node):
		
		if data < node.data:

			if node.leftChild is None:
				node.leftChild = Node(data)
			else:
				self.insertNode(data, node.leftChild)
		else:
			if node.rightChild is None:
				node.rightChild = Node(data)
			else:
				self.insertNode(data, node.rightChild)

	def traversTree(self):
		if self.root is not None:
			self.traverseInOrder(self.root)

	def traverseInOrder(self, node):
		if node.leftChild:
			self.traverseInOrder(node.leftChild)

		print(node.data)

		if node.rightChild:
			self.traverseInOrder(node.rightChild)

	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)

	def removeNode(self, data, node):
		if node is None:
			return node

		if data < node.data:
			node.leftChild = self.removeNode(data, node.leftChild)
		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild)
		else:
			if not node.leftChild and not node.rightChild:
				del node
				return None
			elif not node.leftChild:
				tempNode = node.rightChild
				del node
				return tempNode
			elif not node.rightChild:
				tempNode = node.leftChild
				del node
				return tempNode

			print("Removing node with two childern!")

			tempNode = self.getGreatestLeftNode(node.leftChild)
			node.data = tempNode.data
			node.leftChild = self.removeNode(tempNode.data, node.leftChild)
		return node
	def getGreatestLeftNode(self, node):
		if node.rightChild:
			return self.getGreatestLeftNode(node.rightChild)
		return node


if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.insert(10)
	bst.insert(3)
	bst.insert(-1)
	bst.insert(5)
	bst.insert(12)
	bst.traversTree()

	bst.remove(3)
	
	bst.traversTree()


		
		

		