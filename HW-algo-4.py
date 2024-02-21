import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Кількість даних для тестування
data_sizes = [1000, 5000, 10000]
for size in data_sizes:
    data = [random.randint(0, 100000) for _ in range(size)]

    # Розрахунок часу для сортування злиттям
    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=10)

    # Розрахунок часу для сортування вставками
    insertion_sort_time = timeit.timeit(
        lambda: insertion_sort(data.copy()), number=10)

    # Розрахунок часу для Timsort
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=10)

    print(f"Розмір даних: {size}")
    print(f"Час для сортування злиттям: {merge_sort_time}")
    print(f"Час для сортування вставками: {insertion_sort_time}")
    print(f"Час для Timsort: {timsort_time}")
    print("\n")
