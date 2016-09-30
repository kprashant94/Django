
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def min(self):
		temp = self._min(self.root)
		if temp:
			return temp.value
		else:
			return None

	def _min(self,node):
		if node:
			if node.left:
				return self._min(node.left)
			else:
				return node
		else:
			return None