
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def inorder(self):
		if self.root:
			return self._inorder(self.root,[])
		else:
			return None

	def _inorder(self,node,S=[]):
		if node.left:
			self._inorder(node.left,S)
		S.append(node.value)
		if node.right:
			self._inorder(node.right,S)
		return S