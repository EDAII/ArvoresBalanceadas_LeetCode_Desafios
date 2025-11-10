'''
732. Balance a Binary Search Tree: https://leetcode.com/problems/my-calendar-iii/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''

import java.util.Map;
import java.util.TreeMap;

class MyCalendarThree {

    // A solução usa uma TreeMap (Árvore Rubro-Negra). A TreeMap garante que, ao iterarmos, as mudanças sejam processadas em ordem cronológica.
    // Ela armazenará as "mudanças" na contagem de eventos ativos.
    // Chave (Integer): O timestamp (tempo de início ou fim).
    // Valor (Integer): A mudança na contagem (+1 se for um início, -1 se for um fim).
    private Map<Integer, Integer> mudancas;

    public MyCalendarThree() {
        // Aqui instanciamos a árvore balanceada para guardar as mudanças.
        this.mudancas = new TreeMap<>();
    }

    public int book(int startTime, int endTime) {
        
        // Etapa 1: Registrar as Mudanças
        // Registra que no 'startTime', o número de eventos ativos AUMENTA em 1.
        this.mudancas.put(startTime, this.mudancas.getOrDefault(startTime, 0) + 1);
        
        // Registra que no 'endTime', o número de eventos ativos DIMINUI em 1.
        this.mudancas.put(endTime, this.mudancas.getOrDefault(endTime, 0) - 1);

        // Etapa 2: Processar as Mudanças
        int eventosAtivos = 0; // Contador de eventos simultâneos.
        int maxK = 0;          // O máximo de eventos encontrado.
        
        // Iteramos pelos VALORES da nossa TreeMap. Como a árvore é ordenada pela chave (tempo), temos a garantia de que estamos processando as mudanças na ordem correta.
        for (int mudanca : this.mudancas.values()) {
            
            // Aplicamos a mudança (+1 ou -1) ao nosso contador
            eventosAtivos += mudanca;
            
            // Se o número atual de eventos ativos for o maior que já vimos, atualizamos o máximo.
            if (eventosAtivos > maxK) {
                maxK = eventosAtivos;
            }
        }
        
        // Retorna o k-booking máximo
        return maxK;
    }
}