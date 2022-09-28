#AVL TREES or Balanced Binary Trees
#----------------------------------

#AVL Trees is just a Binary search tree But it is used to balance the tree.
#Both sides left and right evenly got nodes or 1 node extra not more than like that.
#AVL y introduced because tree time complexity based on the tree height tree DS used for log(N) but the regular BST takes more height AVL introduced.
#In AVL Trees Balance is calculated using Height of the tree.

#How to calculate Tree height?
#Based on stages a node has 1 or 2 leaf nodes then it is stage 1, then leaf nodes having 1 or 2 nodes then it is 2nd stage to root node and 1st stage to child node it like chine link concept this is how to calculate height.

#NOTE: balance factor =  height of left - height of right => -1 , 0 , 1 or not balanced.

#How to calculate Tree is Balanced or Not
#If tree one side height is high compare to other side this it is imbalanced tree.

#How to balance it?
#Just make left or right tree nodes should become allign and which side side to length take middle from that length and move to root above that node all nodes need to be moved to other side to balance the tree.

#To balance LL,RR,LR,RL Rotation methods or used how it works i Know.

#LL - left left rotation is single rotation on left side to right side rotation.(rotation to left)

#RR -  also same but (rotation to right)

#LR - is used for first Left side rotation then Right side rotation (double rotation)

#RL -  is opposite to LR.


#------------------------------------------------------------------------

# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode():
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the
# Insert operation
class AVL_Tree():

	# Recursive function to insert key in
	# subtree rooted with node and returns
	# new root of subtree.
	def insert(self, root, key):
	
		# Step 1 - Perform normal BST
		if root is None:
			return TreeNode(key)
		elif key < root.key:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and key < root.left.key:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and key > root.right.key:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and key > root.left.key:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and key < root.right.key:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def leftRotate(self, z):

		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):

		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def InOrder(self, root):

		if not root:
			return

		self.InOrder(root.left)
		print("{0} ".format(root.key), end="")
		self.InOrder(root.right)


# Driver program to test above function
myTree = AVL_Tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

"""The constructed AVL Tree would be
			30
		/ \
		20 40
		/ \	 \
	10 25 50"""

# InOrder Traversal
print("InOrder traversal of the",
	"constructed AVL tree is")
myTree.InOrder(root)
print()

# This code is contributed by Ajitesh Pathak
