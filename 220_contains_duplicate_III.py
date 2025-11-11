from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        
        # Se k=0, a distância abs(i-j) <= k nunca será satisfeita por i != j.
        # Se t < 0, a distância abs(nums[i] - nums[j]) <= t nunca será satisfeita.
        if k <= 0 or t < 0:
            return False

        # Esta é a "Red-Black Tree" simulada, que manterá a janela.
        window = SortedList()

        for i, num in enumerate(nums):
            # Manter a janela deslizante de tamanho k
            # Se a janela está cheia, remove o elemento mais antigo.
            if i > k:
                window.remove(nums[i - k - 1])

            # Verificar a condição de valor 't'
            # Precisa ver se existe algum 'x' na 'window' tal que: abs(num - x) <= t  
            # O que é o mesmo que:  -t <= num - x <= t
            # O que é o mesmo que:  num - t <= x <= num + t
            
            # Nós podemos eficientemente (em O(log k)) encontrar o ponto de inserção  para o valor mais baixo (num - t).
            pos = window.bisect_left(num - t)

            # Verificar se o candidato encontrado está dentro do limite
            # Se 'pos' não é o fim da lista (window[pos] existe)
            # E se esse valor (window[pos]) é menor ou igual ao limite superior (num + t)
            # Então encontramos um 'x' que satisfaz a condição.
            if pos < len(window) and window[pos] <= num + t:
                return True

            # Adicionar o número atual à janela
            window.add(num)

        # Se terminar o loop sem encontrar, não há duplicatas.
        return False