import random
import matplotlib.pyplot as plt
import pandas as pd

def selection_sort(arr):
    n = len(arr)
    k = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            k += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return k

def insertion_sort(arr):
    n = len(arr)
    k = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            k += 1
        arr[j + 1] = key
        k += 1
    return k

def bubble_sort(arr):
    n = len(arr)
    k = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            k += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return k

def merge_sort(arr, k=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        k = merge_sort(left_half, k)
        k = merge_sort(right_half, k)

        i = j = l = 0
        while i < len(left_half) and j < len(right_half):
            k += 1
            if left_half[i] < right_half[j]:
                arr[l] = left_half[i]
                i += 1
            else:
                arr[l] = right_half[j]
                j += 1
            l += 1

        while i < len(left_half):
            arr[l] = left_half[i]
            i += 1
            l += 1

        while j < len(right_half):
            arr[l] = right_half[j]
            j += 1
            l += 1

    return k

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    k = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                k += 1
            arr[j] = temp
            k += 1
        gap //= 2

    return k

def quick_sort(arr, k=0):
    if len(arr) <= 1:
        return arr, k

    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        k += 1
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    sorted_left, k = quick_sort(left, k)
    sorted_right, k = quick_sort(right, k)

    return sorted_left + middle + sorted_right, k

def heap_sort(arr):
    n = len(arr)
    k = 0

    for i in range(n // 2 - 1, -1, -1):
        k = heapify(arr, n, i, k)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        k = heapify(arr, i, 0, k)

    return k

def heapify(arr, n, i, k):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        k += 1
        k = heapify(arr, n, largest, k)

    return k

def quick_sort(arr, k=0):
    if len(arr) <= 1:
        return arr, k

    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        k += 1
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    sorted_left, k = quick_sort(left, k)
    sorted_right, k = quick_sort(right, k)

    return sorted_left + middle + sorted_right, k

def quick_sort_wrapper(arr):
    _, iterations = quick_sort(arr)
    return iterations

def generate_arrays(n):
    best_case = list(range(1, n + 1))

    almost_sorted_case = best_case[:]
    num_swaps = int(0.1 * n)
    for _ in range(num_swaps):
        i, j = random.sample(range(n), 2)
        almost_sorted_case[i], almost_sorted_case[j] = almost_sorted_case[j], almost_sorted_case[i]

    worst_case = list(range(n, 0, -1))

    # Случайный массив (средний случай)
    avg_case = best_case[:]
    random.shuffle(avg_case)

    return best_case, almost_sorted_case, worst_case, avg_case

sorts = {
    "Сортировка выбором": selection_sort,
    "Сортировка вставками": insertion_sort,
    "Сортировка пузырьком": bubble_sort,
    "Сортировка слиянием": merge_sort,
    "Сортировка Шелла": shell_sort,
    "Быстрая сортировка": quick_sort_wrapper,
    "Пирамидальная сортировка": heap_sort
}

results = []

for sort_name, sort_func in sorts.items():
    print(sort_name)
    sizes = range(1000, 10001, 500)

    best_case_iterations = []
    almost_sorted_case_iterations = []
    worst_case_iterations = []
    avg_case_iterations = []

    for size in sizes:
        best_case, almost_sorted_case, worst_case, avg_case = generate_arrays(size)

        iterations = sort_func(best_case)
        iterations_best = iterations
        best_case_iterations.append(iterations)
        print(f"Отсортированный: {size} элементов, итераций: {iterations}")

        iterations = sort_func(almost_sorted_case)
        iterations_almost = iterations
        almost_sorted_case_iterations.append(iterations)
        print(f"Почти отсортированный случай: {size} элементов, итераций: {iterations}")

        iterations = sort_func(avg_case)
        iterations_avg = iterations
        avg_case_iterations.append(iterations)
        print(f"Случайно отсортированный: {size} элементов, итераций: {iterations}")

        iterations = sort_func(worst_case)
        iterations_worst = iterations
        worst_case_iterations.append(iterations)
        print(f"Обратно отсортированный: {size} элементов, итераций: {iterations}")

        results.append([
            sort_name, size, iterations_best, iterations_almost,
            iterations_avg, iterations_worst
        ])

    plt.figure()
    plt.plot(sizes, best_case_iterations, linestyle='-', color='b', label='Лучший случай')
    plt.plot(sizes, almost_sorted_case_iterations, linestyle='-', color='g', label='Почти отсортированный случай')
    plt.plot(sizes, avg_case_iterations, linestyle='-', color='r', label='Средний случай')
    plt.plot(sizes, worst_case_iterations, linestyle='-', color='m', label='Худший случай')
    plt.title(sort_name)
    plt.xlabel('Размер массива')
    plt.ylabel('Количество итераций')
    plt.legend()
    plt.show()

df = pd.DataFrame(results, columns=[
    "Название сортировки", "Количество элементов",
    "Отсортированный массив", "Почти отсортированный массив",
    "Случайный массив", "Обратно отсортированный массив"
])

df.to_excel("sorting_results.xlsx", index=False)
print("Результаты сохранены в sorting_results.xlsx")