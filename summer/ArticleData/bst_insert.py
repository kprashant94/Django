
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self,key):
		if self.root:
			self._insert(self.root,key)
		else:
			self.root = Node(key)

	def _insert(self,node,key):
		if key > node.value:
			if node.right:
				self._insert(node.right,key)
			else:
				node.right = Node(key,None,None,node)

		else:
			if node.left:
				self._insert(node.left,key)
			else:
				node.left = Node(key,None,None,node)