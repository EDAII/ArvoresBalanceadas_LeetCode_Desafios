'''
1382. Balance a Binary Search Tree: https://leetcode.com/problems/balance-a-binary-search-tree/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''

import java.util.ArrayList;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    
    // Usamos uma lista para armazenar os valores da árvore em ordem crescente.
    private List<Integer> sortedNodes = new ArrayList<>();

    // Função principal que recebe a raiz da árvore desbalanceada e retorna a raiz da nova árvore balanceada.
    public TreeNode balanceBST(TreeNode root) {
        
        // Etapa 1: Percorrer a árvore original e armazenar os valores em ordem crescente na lista 'sortedNodes'.
        inOrderTraversal(root);
        
        // Etapa 2: Construir e retornar a nova árvore balanceada a partir da lista ordenada.
        return buildBalancedTree(0, sortedNodes.size() - 1);
    }
    
    // Percorre a árvore em-ordem (esquerda, raiz, direita) e adiciona os valores dos nós na lista 'sortedNodes'. Ao final, a lista conterá todos os valores em ordem crescente.
    private void inOrderTraversal(TreeNode node) {
        // Caso base: se o nó é nulo, não há nada a fazer.
        if (node == null) {
            return;
        }
        
        // Visita recursivamente a subárvore esquerda.
        inOrderTraversal(node.left);
        
        // Adiciona o valor do nó atual (raiz da subárvore).
        sortedNodes.add(node.val);
        
        // Visita recursivamente a subárvore direita.
        inOrderTraversal(node.right);
    }
    
    // Constrói recursivamente uma árvore balanceada a partir dos elementos da lista 'sortedNodes' dentro do range [start, end].
    private TreeNode buildBalancedTree(int start, int end) {
        // Caso base: Se o índice inicial ultrapassar o final, significa que este ramo da árvore terminou.
        if (start > end) {
            return null;
        }
        
        // Agora vamos encontrar o elemento do meio do range atual. Esta será a raiz da (sub)árvore.
        int mid = (start + end) / 2;
        
        // Criamos o nó raiz com o valor do meio.
        TreeNode root = new TreeNode(sortedNodes.get(mid));
        
        // Construimos recursivamente a subárvore esquerda. Ela será formada pelos elementos à esquerda do meio (start até mid - 1)
        root.left = buildBalancedTree(start, mid - 1);
        
        // Construimos recursivamente a subárvore direita. Ela será formada pelos elementos à direita do meio (mid + 1 até end)
        root.right = buildBalancedTree(mid + 1, end);
        
        // Retornar a raiz da (sub)árvore criada
        return root;
    }
}