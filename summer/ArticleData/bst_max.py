
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def max(self):
		temp = self._max(self.root)
		if temp:
			return temp.value
		else:
			return None

	def _max(self,node):
		if node:
			if node.right:
				return self._max(node.right)
			else:
				return node
		else:
			return None