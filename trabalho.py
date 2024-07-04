import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def counting_sort(arr):
    n = len(arr)
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for i in range(n):
        count[arr[i]] += 1
    k = 0
    for i in range(max_value + 1):
        for _ in range(count[i]):
            arr[k] = i
            k += 1
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def nano_para_micro(num):
    # Divide a entrada em nanosegundos (ns) por 1000, convertendo-a em microsegundos (μs).
    # Também separa a saída em microsegundos em grupos de 3 dígitos, para facilitar a visualização dos resultados.
    num_str = str(int(num/1000))
    result = ""
    for i in range(len(num_str)):
        if i > 0 and (len(num_str) - i) % 3 == 0:
            result += ","
        result += num_str[i]
    return(result)

def gen_array(n, k):
    arr = [random.randint(0, k) for _ in range(n)]
    return arr

def run_benchmark(arr, sort_func, total_times, sort_func_name):
    start = time.process_time_ns()
    sort_func(arr)
    end = time.process_time_ns()
    if sort_func_name not in total_times:
        total_times[sort_func_name] = 0
    total_times[sort_func_name] += (end - start)

def main():
    n = int(input("Insira o número de elementos dos arrays: "))
    k = int(input("Insira o valor máximo dos elementos dos arrays: "))

    total_times = {}

    arr = gen_array(n, k)

    for sort_func in [counting_sort, merge_sort]:
        run_benchmark(arr.copy(), sort_func, total_times, sort_func.__name__)


    print("Tempo total de execução de cada algoritmo de ordenação para o mesmo array de",
        n, "elementos aleatórios, variando de 0 a", k, ":", "\n",
        "As unidades de tempo são microsegundos (μs), sempre inteiros, com separação de milhares por vírgulas (,).")
    for sort_name in total_times:
        print(f"Tempo total {sort_name.replace('_', ' ').capitalize()}:",
              nano_para_micro(total_times[sort_name]), "μs")


if __name__ == "__main__":
    main()
