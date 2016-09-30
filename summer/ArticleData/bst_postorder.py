
class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.value = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def postorder(self):
		if self.root:
			return self._postorder(self.root,[])
		else:
			return None

	def _postorder(self,node,S=[]):		
		if node.left:
			self._postorder(node.left,S)
		
		if node.right:
			self._postorder(node.right,S)
		
		S.append(node.value)		
		return S