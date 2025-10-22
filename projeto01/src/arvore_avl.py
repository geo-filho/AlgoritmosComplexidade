from arvore_binaria import Node, BST

class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

class AVLTree(BST):
    """
    Árvore AVL (BST balanceada)
    Complexidade:
        Inserção, remoção e busca: O(log n)
    """
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # chave duplicada

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)

        # Rotação esquerda-direita
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        # Rotação direita-esquerda
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        # Rotação esquerda-direita
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # Rotação direita-esquerda
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y
