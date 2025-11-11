class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # Altura para balanceamento AVL
        self.dup = 1     # Contagem de duplicatas deste valor
        self.size = 1    # Total de nós nesta subárvore (incluindo dups)

#  Classe da Solução com a Lógica AVL 
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        self.root = None
        self.result = [0] * n
        
        # Iteramos de TRÁS para FRENTE
        for i in range(n - 1, -1, -1):
            self.root = self.insert(self.root, nums[i], i, 0)
            
        return self.result

    #  Funções Auxiliares da AVL 
    
    def getHeight(self, node):
        return node.height if node else 0

    def getSize(self, node):
        return node.size if node else 0

    # Atualiza altura E size de um nó (chamado após inserções/rotações)
    def updateNode(self, node):
        if not node:
            return
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        node.size = node.dup + self.getSize(node.left) + self.getSize(node.right)

    def getBalance(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right) if node else 0

    #  Rotações AVL 
    
    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        
        # Rotação
        x.right = y
        y.left = T2
        
        # Atualiza nós (IMPORTANTE: y primeiro, pois é o filho)
        self.updateNode(y)
        self.updateNode(x)
        
        return x

    def leftRotate(self, x):
        y = x.right
        T1 = y.left

        # Rotação
        y.left = x
        x.right = T1

        # Atualiza nós (IMPORTANTE: x primeiro, pois é o filho)
        self.updateNode(x)
        self.updateNode(y)
        
        return y

    #  Função Principal de Inserção e Contagem  
    
    def insert(self, node, val, index, smaller_count_so_far):
        
        #  Inserção normal de BST
        if not node:
            self.result[index] = smaller_count_so_far
            return Node(val)

        if val == node.val:
            node.dup += 1
            # Encontramos o valor. Todos na subárvore esquerda são menores.
            self.result[index] = smaller_count_so_far + self.getSize(node.left)
        
        elif val < node.val:
            # Indo para a esquerda. O smaller_count não muda.
            node.left = self.insert(node.left, val, index, smaller_count_so_far)
        
        else: # val > node.val
            # Indo para a direita.
            # TODOS na subárvore esquerda (getSize(node.left)) 
            # E TODAS as duplicatas (node.dup) são menores.
            new_smaller_count = smaller_count_so_far + self.getSize(node.left) + node.dup
            node.right = self.insert(node.right, val, index, new_smaller_count)

        #  Atualizar altura e size do nó atual (NA SUBIDA)
        #    (A exceção é o if val == node.val, que não faz chamada recursiva)
        self.updateNode(node)

        #  Obter o fator de balanceamento
        balance = self.getBalance(node)

        #  Rebalancear se necessário (4 casos)

        # Caso Left-Left (LL)
        if balance > 1 and val < node.left.val:
            return self.rightRotate(node)

        # Caso Right-Right (RR)
        if balance < -1 and val > node.right.val:
            return self.leftRotate(node)

        # Caso Left-Right (LR)
        if balance > 1 and val > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Caso Right-Left (RL)
        if balance < -1 and val < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        # Retorna o nó (potencialmente) novo
        return node