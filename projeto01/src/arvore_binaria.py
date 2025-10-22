class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """
    Árvore Binária de Busca (BST)
    Inserção, busca e remoção.
    Complexidade:
        Busca/Inserção/Remoção: O(h), onde h é a altura da árvore
        Percursos (inorder, preorder, postorder): O(n)
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key)
        return node

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

    def inorder(self):
        res = []
        self._inorder_rec(self.root, res)
        return res

    def _inorder_rec(self, node, res):
        if node:
            self._inorder_rec(node.left, res)
            res.append(node.key)
            self._inorder_rec(node.right, res)

    def preorder(self):
        res = []
        self._preorder_rec(self.root, res)
        return res

    def _preorder_rec(self, node, res):
        if node:
            res.append(node.key)
            self._preorder_rec(node.left, res)
            self._preorder_rec(node.right, res)

    def postorder(self):
        res = []
        self._postorder_rec(self.root, res)
        return res

    def _postorder_rec(self, node, res):
        if node:
            self._postorder_rec(node.left, res)
            self._postorder_rec(node.right, res)
            res.append(node.key)
