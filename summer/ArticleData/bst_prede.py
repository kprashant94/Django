
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def predecessor(self,key):
		temp = self._predecessor(self._search(self.root,key))
		if temp:
			return temp.value
		else:
			return None

	def _predecessor(self,node):
		if node:
			if node.left:
				return self._max(node.left)
			elif node == node.parent.right:
				return node.parent
			else:
				return None

		else:
			return None

	def search(self,key):
		temp = self._search(self.root,key)
		if temp:
			return temp.value
		else:
			return None

	def _search(self,node,key):
		if node:
			if key == node.value:
				return node
			elif (key > node.value):
				return self._search(node.right,key)
			else:
				return self._search(node.left,key)
		else:
			return None

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