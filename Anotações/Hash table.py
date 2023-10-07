class Solution:
# self: O primeiro parâmetro é sempre uma referência à instância da classe (o objeto) e é usado implicitamente em métodos de instância em Python.
# nums: Uma lista de números inteiros que representam os números de entrada nos quais você deseja encontrar dois números que somam ao target.
# target: Um número inteiro que representa o valor alvo que você deseja alcançar somando dois números da lista.
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Aqui, criamos um dicionário vazio chamado numMap. Este dicionário será usado para armazenar 
        # os números da lista e seus índices à medida que iteramos pela lista.
        numMap = {}
        # Calculamos o comprimento da lista nums e armazenamos em n. Isso será usado para controlar a iteração pelos elementos da lista.
        n = len(nums)

        for i in range(n):
            # Iniciamos um loop for que irá iterar pelos índices da lista nums
            complement = target - nums[i]
            # Calculamos a diferença entre o target e o número atual em nums[i] e armazenamos em complement.
            # O complement é o número que precisamos encontrar na lista para que a soma dos dois números seja igual ao target.
            if complement in numMap:
                # Verificamos se o complement já existe no dicionário numMap. Se existir, significa que encontramos dois números cuja soma é igual ao target,
                # e estamos prontos para retornar os índices desses números.
                return [numMap[complement], i]
            # Se encontrarmos o complement no dicionário, retornamos uma lista contendo os índices desses dois números. 
            # numMap[complement] retorna o índice do primeiro número, e i retorna o índice do segundo número.
            numMap [nums[i]] = i
            # Se não encontrarmos o complement, adicionamos o número atual (nums[i]) como chave no dicionário numMap, 
            # com o valor sendo o índice desse número na lista. Isso nos permite procurar o complemento do número atual em iterações futuras.

        return[]
    # Se o loop terminar sem encontrar uma solução, retornamos uma lista vazia [] para indicar que não foi possível encontrar dois números que somam ao target.