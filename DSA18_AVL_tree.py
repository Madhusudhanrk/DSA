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