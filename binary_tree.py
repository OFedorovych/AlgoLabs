class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        else:
            return True

    def find_item(self, value):
        found_node = self._search(self.root, value)
        return found_node

    def _search(self, noda_to_check, value):
        #no more nodes, our parent is a leaf
        #we found: searched  value is equal to the node
        if ((noda_to_check == None) or (noda_to_check.value == value)):
            return noda_to_check
        
        if value > noda_to_check.value:
            # go right
            return self._search(noda_to_check.right, value)
        else:
            # go left
            return self._search(noda_to_check.left, value)



    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        self._insert(self.root, value)

    def _insert(self, current_node, value):
        #go to right
        if value > current_node.value:
            #add right leaf if absent
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            #search for a proper position in right branch
            return self._insert(current_node.right, value)
            
        else:
            #add left leaf if absent
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            return self._insert(current_node.left, value)



    def delete(self, value):
        if self.root is None:
            return self.root

        self._delete(self.root, value)

    def min_val_node(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def _delete(self, current_node, value):
        if value > current_node.value:
            current_node.right = self._delete(current_node.right, value)
        elif(value < current_node.value):
            current_node.left = self._delete(current_node.left, value)
        #if value is same as current node value, than this is the node to be deleted
        else:
            #node with only one or no child
            if current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            elif(current_node.left is None):
                temp = current_node.right
                current_node = None
                return temp
            #node with two children
            temp = self.min_val_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete(current_node.right, temp.value)
        
        return current_node

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, current_node):
        if current_node is not None and ((current_node.left != None) or (current_node.right != None)) :
            print ("\nNode : " + str(current_node.value))
            if current_node.left is not None:
                print ("Left child of Node "+ str(current_node.value) + ": " + str(current_node.left.value))
            else:
                print("Node " + str(current_node.value) + " has no left child")
            if current_node.right is not None:
                print ("Right child of Node "+ str(current_node.value) + ": " + str(current_node.right.value))
            else:
                print("Node " + str(current_node.value) + " has no right child")
            self._inorder(current_node.left)
            self._inorder(current_node.right)

    
class Node:

    def __init__(self, value, parent = None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value

def main():
    tree = Tree()
    tree.insert(15)
    tree.insert(6)
    tree.insert(7)
    tree.insert(4)
    tree.insert(5)
    tree.insert(23)
    tree.insert(71)
    tree.insert(50)

    print("\nBinary tree before deleting a node:")
    tree.inorder()

    tree.delete(15)
    print("\n\nBinary tree after deleting a node:")
    tree.inorder()

    print("\nFound item: " + str(tree.find_item(71).value))

    print("\nIs element 7 inside the binary tree? - " + str(tree.search(7)))
    print("\nIs element 115 inside the binary tree? - " + str(tree.search(115)))
    print("\nIs element 80 inside the binary tree? - " + str(tree.search(80)))
    print("\nIs element 23 inside the binary tree? - " + str(tree.search(23)))


if __name__ == "__main__":
    main()