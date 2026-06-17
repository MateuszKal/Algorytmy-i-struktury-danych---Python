import sys
import time, random

class Node: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_AVL(num):
    if not num:
        return None
    num.sort()
    mediana = len(num) // 2 
    root = Node(num[mediana])
    root.left = create_AVL(num[:mediana])
    root.right = create_AVL(num[mediana + 1:])
    return root
    
def create_BST(nums):
    root = Node(nums[0])
    for num in nums[1:]:
        insert_BST(root, num)
    return root

def insert_BST(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert_BST(root.left, val)
    else:
        root.right = insert_BST(root.right, val)
    return root

def get_inorder(root, values):
    if root:
        get_inorder(root.left, values)
        values.append(str(root.val))
        get_inorder(root.right, values)

def print_inorder(root):
    values = []
    get_inorder(root, values)
    print("In-order: ", end="")
    print(", ".join(values))

def get_preorder(root, values):
    if root:
        values.append(str(root.val))
        get_preorder(root.left, values)
        get_preorder(root.right, values)

def print_preorder(root):
    values = []
    get_preorder(root, values)
    print("Pre-order: ", end="")
    print(", ".join(values))
    
def get_postorder(root, values):
    if root:
        get_postorder(root.left, values)
        get_postorder(root.right, values)
        values.append(str(root.val))

def print_postorder(root):
    values = []
    get_postorder(root, values)
    print("Post-order: ", end="")
    print(", ".join(values))

def find_max(node):
    if not node:
        return None
    if not node.right:
        return node.val
    return find_max(node.right)

def find_min(node):
    if not node:
        return None
    if not node.left:
        return node.val
    return find_min(node.left)

def postorder_delete(root, deleted=[]):
    if root is None:
        return None
    postorder_delete(root.left, deleted)
    postorder_delete(root.right, deleted)
    deleted.append(root.val)
    del root

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

def left_rotation(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    return new_root

def right_rotation(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root

def rebalance(root):
    if root is None:
        return None
    left_height = height(root.left)
    right_height = height(root.right)

    if left_height - right_height > 1:
        if height(root.left.left) >= height(root.left.right):
            root = right_rotation(root)
        else:
            root.left = left_rotation(root.left)
            root = right_rotation(root)
    elif right_height - left_height > 1:
        if height(root.right.right) >= height(root.right.left):
            root = left_rotation(root)
        else:
            root.right = right_rotation(root.right)
            root = left_rotation(root)

    return root

def remove(root, values):
    if root is None:
        return root
    
    if not isinstance(values, list):
        values = [values]
    
    for val in values:
        root = remove_single(root, val)
    
    return root

def remove_single(root, val):
    if root is None:
        return root
    
    if val < root.val:
        root.left = remove_single(root.left, val)
    elif val > root.val:
        root.right = remove_single(root.right, val)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = find_min_node(root.right)
        root.val = temp.val
        root.right = remove_single(root.right, temp.val)

    root = rebalance(root)
    return root

def find_min_node(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def menu(root):
    n = ""
    try:
        while(n != "Exit"):
            print("action> ", end="")
            n = input()
            if (n == "Help"):
                print("Help\t\tShow this message")
                print("FindMinMax\tFind min and max elements of the tree")
                print("Print\t\tPrint the tree usin In-order, Pre-order, Post-order")
                print("Remove\t\tRemove elements of the tree")
                print("Delete\t\tDelete whole tree")
                print("Rebalance\tRebalance the tree")
                print("Exit\t\tExits the program (same as ctrl+D)")
                
            elif (n == "Print"):
                print_inorder(root)
                print_postorder(root)
                print_preorder(root)

            elif (n == "FindMinMax"):
                print("Min:", find_min(root))
                print("Max:", find_max(root))

            elif (n == "Delete"):
                deleted_nodes = []
                postorder_delete(root, deleted_nodes)
                print("Deleting: ", end="")
                print(" ".join(map(str, deleted_nodes)))
                root = None
                print("Tree succesfully removed")

            elif (n == "Rebalance"):
                root = rebalance(root)
                print_preorder(root)
                
            elif n == "Remove":
                print("Enter value(s) to remove (separated by spaces): ", end="")
                values = list(map(int, input().split()))
                root = remove(root, values)

    except EOFError:
        print("ctrl + D")
        print("Program exited with status: 0")
        sys.exit(1)

def main():

    if len(sys.argv) < 2 or sys.argv[1] != "--tree":
        print("Usage: python3 tree.py --tree <algorithm_name>")
        sys.exit(1)
    algorithm_name = sys.argv[2]
    
    nodes = int(input("nodes> "))
    if nodes <= 0:
        print("You provided an incorrect node representation.")
        sys.exit(1)

    print("insert> ", end="")
    inserts = input().split()
    inserts = list(map(int, inserts))
    inserts = elements = [random.randrange(1, 5000000) for _ in range(262144)]

    if len(inserts) != nodes:
        print("You specified too few/more nodes.")
        sys.exit(1)

    for insert in inserts:
        if insert <= 0:
            print("You have entered a negative node or node with a value of 0.")
            sys.exit(1)

    if (algorithm_name == "AVL"):
        start_time = time.perf_counter()
        root = create_AVL(inserts)
        print("Sorted: ", end="")
        end_time = time.perf_counter()
        czas_wykonania = end_time - start_time
        for i in range(len(inserts)):
            if i == len(inserts) - 1:
                print(inserts[i], end="")
            else:
                print(inserts[i], end=", ")
        mediana = len(inserts) // 2 
        print("\nMedian:", inserts[mediana])
        print(f"czas wykonania: {czas_wykonania} sekund")
        sys.exit()
    elif (algorithm_name == "BST"):
        root = create_BST(inserts)
        print("Inserting: ", end="")
        for i in range(len(inserts)):
            if i == len(inserts) - 1:
                print(inserts[i], end="")
            else:
                print(inserts[i], end=", ")
        print(" ")

    else:
        print("You entered the wrong algorithm name")
        sys.exit(0)

    menu(root)
    print("Program exited with status: 0")

if __name__ == "__main__":
    main()