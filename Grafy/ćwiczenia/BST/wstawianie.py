class BSTNode:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def wstawianie(root,key):
    while root != None:
        if root.key == key:
            return None
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    new = BSTNode(key)
    if root.key < key:
        root.right = new
        new.parent = new
    else:
        root.left = new
        new.parent = new

def min_max(root):
    while root.left is not None:
        root = root.left
    return root.key

def find(root,key):
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None

def usuwanie(root,key):
    head = find(root,key)
    if head is not None:
        if root.right == None and root.left == None:
            root = root.parent
            root.next = None
        elif root.right == None or root.left == None:
            if root.right is None:
                root = root.parent
                if root.left.key == key:
                    root = root.left.left
                else:
                    root = root.right.left
            else:
                root = root.parent
                if root.left.key == key:
                    root = root.left.left
                else:
                    root = root.right.left
        else:


