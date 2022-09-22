def delete_node(self,this_node,key_val):

    if this_node is None:
        return print("root Node is empy")
    if key_val is None:return False

    if key_val < this_node.key:
        this_node.left = self.delete_node(this_node.left,key_val)
    elif key_val > this_node.key:
        this_node.right  = self.delete_node(this_node.right,key_val)
    else:
        if this_node.left is None:
            temp = this_node.right
            this_node.right = None
            return temp
        
        if this_node.right is None:
            temp = this_node.left
            this_node.left = None
            return temp
        
        temp = self.find_inorder_successor(this_node)

        this_node.key = temp.key

        this_node.right = self.delete_node(this_node.right,temp.key)

def successor(this_node):
    temp = this_node
    while temp.left is None:
        temp  = temp.left

    return temp