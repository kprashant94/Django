
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def delete(self,key):
		self._delete(self._search(self.root,key))

	def _delete(self,node):
		if node:
			if node.left == None and node.right == None:
				if node.parent:
					if node == node.parent.left:
						node.parent.left = None
					else:
						node.parent.right = None
				else:
					self.root = None
			
			elif node.left == None:
				if node.parent:
					if node == node.parent.left:
						node.parent.left = node.right
					else:
						node.parent.right = node.right
				else:
					self.root = self.root.right
					self.root.parent = None

			elif node.right == None:
				if node.parent:
					if node == node.parent.left:
						node.parent.left = node.left
					else:
						node.parent.right = node.left
				else:
					self.root = self.root.left
					self.root.parent = None

			else:
				temp = self._successor(node)
				node.value = temp.value
				self._delete(temp)

	def successor(self,key):
		temp = self._successor(self._search(self.root,key))
		if temp:
			return temp.value
		else:
			return None

	def _successor(self,node):
		if node:
			if node.right:
				return self._min(node.right)
			elif node == node.parent.left:
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