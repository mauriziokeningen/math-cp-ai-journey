class BinaryNode:
    #A binary node is defined by having three pointers. 2 pointers to the the left or right children (possibly None)
    #and 1 pointer to the parent node (possibly None if it's a root node)
    #O(1) because we are just instantiating one node
    def __init__(A, value, left = None, right = None, parent = None):
        A.value = value
        A.left = left
        A.right = left
        A.parent = parent   

    '''
    The inorder binary tree traversal is the "natural traversal" for a tree since a binary node has left and right children
    The rule are:
    1. Recursively list the nodes of the subtree rooted at the left child of the root
    2. List the root itA
    3. Recursively list the nodes of the subtree rooted at the right child of the root
    '''
    def subtree_inorder(A):
        if A.left:
            yield from A.left.subtree_inorder()
        yield A
        if A.right:
            yield from A.right.subtree_inorder()

    #The first node in an inorder traversal is the deepest left most node. If there is no left subtree the it's the node itA
    #O(h) we have to go down the tree

    def subtree_first(A):
        if A.left:
            return A.left.subtree_first()
        return A
    
    #The last node in an inorder traversal is the deepest right most node. If there is no right subtree then it's the node itA
    #O(h) we have to go down the tree
    def subtree_last(A):
        if A.right:
            return A.right.subtree_last()
        return A
    
    #A sucessor of a node is the next node in the inorder traversal. If our node has a left subtree, then the successor will be
    #the first node in the inorder traversal of that tree.
    #else, it will be the lowest ancestor that has our node as part of its left subtree (we have to walk up the tree until we are not in the right subtree)
    #O(h) because the have to either go directly down or up the tree
    def successor(A):
        if A.right:
            return A.right.subtree_first()
        while A.parent and A == A.parent.right:
            A = A.parent
        return A.parent
    #A predecessor of a node is the previous node in the inorder traversal. If our node has a left subtree the predecessor will be the last node in the inorder traversal
    #of that left subtree. Else, the predecessor is the lowest ancestor such that our node is part of the lowest ancestor's right subtree (walk up the tree until we are not a left subtree)
    ##O(h) because the have to either go directly down or up the tree
    def predecessor(A):
        if A.left:
            return A.left.subtree_last()
        while A.parent and A == A.parent.left:
            A = A.parent
        return A.parent
    
    def add_before(A, B):
        if not A.left:
            A.left = B
            B.parent = A
        else:
            A = A.left.subtree_last()
            A.right = B
            B.parent = A

    def add_after(A, B):
        if not A.right:
            A.right = B
            B.parent = A
        else:
            A = A.right.subtree_first()
            A.left = B
            B.parent = A 

    def subtree_delete(A):
        if A.left or A.right:
            if A.left:
                B = A.predecessor()
            else:
                B = A.successor()
            A.value, B.value = B.value, A.value
            return B.subtree_delete()
        else:
            if A.parent.left == A:
                A.parent.left = None
            else:
                A.parent.right = None
        return A

def build(X):
    A = [x for x in X]
    def build_subtree(A, i, j):
        c = (i+j)//2
        root = BinaryNode(A[c])
        if i < c:
            root.left = build_subtree(A, i, c-1)
            root.left.parent = root
        if c < j:
            root.right = build_subtree(A, c+1, j)
            root.right.parent = root
        return root
    return build_subtree(A, 0, len(A)-1)

[]

    

a = BinaryNode('a')
b = BinaryNode('b')
c = BinaryNode('c')
d = BinaryNode('d')
e = BinaryNode('e')
f = BinaryNode('f')
g = BinaryNode('g')
h = BinaryNode('h')
i = BinaryNode('i')
j = BinaryNode('j')
k = BinaryNode('k')
l = BinaryNode('l')
m = BinaryNode('m')
n = BinaryNode('n')
o = BinaryNode('o')
a.left = b
a.right = c
b.left = d
b.right = e
b.parent = a
c.left = f
c.right = g
c.parent = a
d.left = h
d.right = i
d.parent = b
e.left = j
e.right = k
e.parent = b
f.left = l
f.right = m
f.parent = c
g.left = n
g.right = o
g.parent = c
h.parent = d
i.parent = d
j.parent = e
k.parent = e
l.parent = f
m.parent = f
n.parent = g
o.parent = g


result = []
for node in a.subtree_inorder():
    result.append(node.value)


print(result)
'''
print(a.subtree_first().value)

print(a.subtree_last().value)

print(k.successor().value)

print(j.predecessor().value)

kaka1 = BinaryNode("kaka1")
kaka2 = BinaryNode("kaka2")

a.add_before(kaka1)
a.add_after(kaka2)

result = []
for node in a.subtree_inorder():
    result.append(node.value)
print(result)
'''

a.subtree_delete()

result = []
for node in a.subtree_inorder():
    result.append(node.value)


print(result)

X = [1,2,3,4,5,6,7]
root = build(X)

result = []
for node in root.subtree_inorder():
    result.append(node.value)
print(result)
