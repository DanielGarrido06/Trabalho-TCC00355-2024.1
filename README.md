# Trabalho-TCC00355-2024.1

Este script Python é uma demonstração abrangente de vários algoritmos de ordenação, incluindo ordenação por bolha, seleção, inserção, contagem e mesclagem. Também apresenta funções utilitárias para gerar arrays aleatórios e converter nanosegundos para microssegundos de forma legível. A funcionalidade chave está encapsulada na função run_benchmark, que avalia o desempenho de cada algoritmo de ordenação.

# Algoritmos de Ordenação Explicados

## Ordenação por Bolha
Um algoritmo simples baseado em comparação que percorre repetidamente a lista, compara elementos adjacentes e os troca se estiverem na ordem errada. A passagem pela lista é repetida até que a lista esteja ordenada.

## Ordenação por Seleção
Este algoritmo ordena um array ao repetidamente encontrar o elemento mínimo (considerando ordem ascendente) da parte não ordenada e colocá-lo no início. O algoritmo mantém dois subarrays em um dado array: o subarray que já está ordenado e o subarray restante que está desordenado.

## Ordenação por Inserção
Constrói o array ordenado final um item de cada vez. É muito menos eficiente em listas grandes do que algoritmos mais avançados, como quicksort, heapsort ou mergesort. No entanto, a ordenação por inserção oferece várias vantagens, como implementação simples, eficiência para conjuntos de dados pequenos e é mais eficiente na prática do que a maioria dos outros algoritmos quadráticos simples.

## Ordenação por Contagem
Um algoritmo de ordenação de inteiros que opera contando o número de objetos que possuem cada valor de chave distinto. Em seguida, faz alguma aritmética para calcular a posição de cada objeto na sequência de saída. É eficiente se o intervalo dos dados de entrada não for significativamente maior do que o número de objetos a serem ordenados.

## Ordenação por Mesclagem
Um algoritmo de divisão e conquista que divide o array de entrada em duas metades, chama a si mesmo para as duas metades e, em seguida, mescla as duas metades ordenadas. A função de mesclagem é usada para mesclar duas metades. O processo de mesclagem assume que arr[l..m] e arr[m+1..r] estão ordenados e mescla os dois sub-arrays ordenados em um.


# Funções Utilitárias

## nano_para_micro
Converte nanosegundos para microssegundos e formata o resultado para facilitar a leitura, inserindo vírgulas a cada três dígitos.

## gen_arrays
Gera uma lista de arrays com números aleatórios, baseado nos parâmetros fornecidos (número de elementos, valor máximo dos elementos, número de arrays).
Isso permite que cada Algorítimo de ordenação seja testado na mesma bateria de arrays, que recebem cópias do array geral para realizar seus benchmarks.

## run_benchmark
Executa um benchmark de uma função de ordenação específica em todos os arrays gerados, medindo o tempo total de execução e armazenando esse tempo em um dicionário.

# Função Principal
Solicita ao usuário os parâmetros para a geração dos arrays (número de elementos, valor máximo dos elementos, número de arrays), executa os benchmarks para cada algoritmo de ordenação e apresenta os resultados formatados em microsegundos.

# Exemplos de saídas
Tempo total de execução de cada algoritmo de ordenação para a mesma bateria de 10000 arrays de 100 elementos aleatórios, variando de 0 a 1000 :
As unidades de tempo são microsegundos (μs), sempre inteiros, com separação de milhares por vírgulas (,).

Tempo total Bubble sort: 2,687,500 μs

Tempo total Selection sort: 1,203,125 μs

Tempo total Insertion sort: 984,375 μs

Tempo total Counting sort: 906,250 μs

Tempo total Merge sort: 765,625 μs


Tempo total de execução de cada algoritmo de ordenação para a mesma bateria de 10000 arrays de 200 elementos aleatórios, variando de 0 a 500 : 
As unidades de tempo são microsegundos (μs), sempre inteiros, com separação de milhares por vírgulas (,).

Tempo total Bubble sort: 9,156,250 μs

Tempo total Selection sort: 4,359,375 μs

Tempo total Insertion sort: 4,031,250 μs

Tempo total Counting sort: 531,250 μs

Tempo total Merge sort: 1,750,000 μs