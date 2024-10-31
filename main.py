import random
import matplotlib.pyplot as plt
import pandas as pd
import time
import numpy as np

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def selection_sort_time(arr):
    start = time.time()
    selection_sort(arr)
    end = time.time()
    return end - start

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def insertion_sort_time(arr):
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    return end - start

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def bubble_sort_time(arr):
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    return end - start

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        i = j = l = 0
        while i < len(left_half) and j < len(right_half):
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

def merge_sort_time(arr):
    start = time.time()
    merge_sort(arr)
    end = time.time()
    return end - start

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def shell_sort_time(arr):
    start = time.time()
    shell_sort(arr)
    end = time.time()
    return end - start

def shell_sort_hibbard(arr):
    n = len(arr)
    gap = 1

    while gap < n // 2:
        gap = 2 * gap + 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def shell_sort_hibbard_time(arr):
    start = time.time()
    shell_sort_hibbard(arr)
    end = time.time()
    return end - start

def shell_sort_pratt(arr):
    n = len(arr)
    gap = 1

    while gap < n // 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3

def shell_sort_pratt_time(arr):
    start = time.time()
    shell_sort_pratt(arr)
    end = time.time()
    return end - start

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heap_sort_time(arr):
    start = time.time()
    heap_sort(arr)
    end = time.time()
    return end - start

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_time(arr):
    start = time.time()
    quick_sort(arr)
    end = time.time()
    return end - start

def generate_arrays(n):
    best_case = list(range(1, n + 1))

    almost_sorted_case = best_case[:]
    num_swaps = int(0.1 * n)
    for _ in range(num_swaps):
        i, j = random.sample(range(n), 2)
        almost_sorted_case[i], almost_sorted_case[j] = almost_sorted_case[j], almost_sorted_case[i]

    worst_case = list(range(n, 0, -1))

    avg_case = best_case[:]
    random.shuffle(avg_case)

    return best_case, almost_sorted_case, worst_case, avg_case

sorts = {
    "Сортировка выбором": selection_sort_time,
    "Сортировка вставками": insertion_sort_time,
    "Сортировка пузырьком": bubble_sort_time,
    "Сортировка слиянием": merge_sort_time,
    "Сортировка Шелла": shell_sort_time,
    "Сортировка Шелла (последовательность Хиббарда)": shell_sort_hibbard_time,
    "Сортировка Шелла (последовательность Пратта)": shell_sort_pratt_time,
    "Быстрая сортировка": quick_sort_time,
    "Пирамидальная сортировка": heap_sort_time
}

results = []

for sort_name, sort_func in sorts.items():
    print(sort_name)
    sizes = range(1000, 2001, 100)

    best_case_time = []
    almost_sorted_case_time = []
    worst_case_time = []
    avg_case_time = []

    for size in sizes:
        best_case, almost_sorted_case, worst_case, avg_case = generate_arrays(size)

        result_time = sort_func(best_case)
        time_best = result_time
        best_case_time.append(result_time)
        print(f"Отсортированный: {size} элементов, время: {result_time}")

        result_time = sort_func(almost_sorted_case)
        time_almost = result_time
        almost_sorted_case_time.append(result_time)
        print(f"Почти отсортированный случай: {size} элементов, время: {result_time}")

        result_time = sort_func(avg_case)
        time_avg = result_time
        avg_case_time.append(result_time)
        print(f"Случайно отсортированный: {size} элементов, время: {result_time}")

        result_time = sort_func(worst_case)
        time_worst = result_time
        worst_case_time.append(result_time)
        print(f"Обратно отсортированный: {size} элементов, время: {result_time}")

        results.append([
            sort_name, size, time_best, time_almost,
            time_avg, time_worst
        ])

    plt.figure()
    plt.plot(sizes, best_case_time, marker='o', ms='1', color='b', linestyle=' ', label='Лучший случай')
    coeffs_best = np.polyfit(sizes, best_case_time, deg=2)
    best_fit_line = np.polyval(coeffs_best, sizes)
    plt.plot(sizes, best_fit_line, color='b')

    plt.plot(sizes, almost_sorted_case_time, marker='o', ms='1', color='g', linestyle=' ', label='Почти отсортированный случай')
    coeffs_almost = np.polyfit(sizes, almost_sorted_case_time, deg=2)
    almost_fit_line = np.polyval(coeffs_almost, sizes)
    plt.plot(sizes, almost_fit_line, color='g')

    plt.plot(sizes, avg_case_time, marker='o', ms='1', color='r', linestyle=' ', label='Средний случай')
    coeffs_avg = np.polyfit(sizes, avg_case_time, deg=2)
    avg_fit_line = np.polyval(coeffs_avg, sizes)
    plt.plot(sizes, avg_fit_line, color='r')

    plt.plot(sizes, worst_case_time, marker='o', ms='1', color='m', linestyle=' ', label='Худший случай')
    coeffs_worst = np.polyfit(sizes, worst_case_time, deg=2)
    worst_fit_line = np.polyval(coeffs_worst, sizes)
    plt.plot(sizes, worst_fit_line, color='m')
    plt.title(sort_name)
    plt.xlabel('Размер массива')
    plt.ylabel('Время работы')
    plt.legend()
    plt.show()

df = pd.DataFrame(results, columns=[
    "Название сортировки", "Количество элементов",
    "Отсортированный массив", "Почти отсортированный массив",
    "Случайный массив", "Обратно отсортированный массив"
])

df.to_excel("sorting_results.xlsx", index=False)
print("Результаты сохранены в sorting_results.xlsx")
