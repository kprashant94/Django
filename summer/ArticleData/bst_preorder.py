
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def preorder(self):
		if self.root:
			return self._preorder(self.root,[])
		else:
			return None

	def _preorder(self,node,S=[]):
		S.append(node.value)		
		if node.left:
			self._preorder(node.left,S)
		
		if node.right:
			self._preorder(node.right,S)
		
		return S