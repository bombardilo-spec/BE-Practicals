import random
import time

def partition_deterministic(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_deterministic(arr, low, high):
    if low < high:
        pi = partition_deterministic(arr, low, high)
        quick_sort_deterministic(arr, low, pi - 1)
        quick_sort_deterministic(arr, pi + 1, high)


def partition_randomized(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition_deterministic(arr, low, high)


def quick_sort_randomized(arr, low, high):
    if low < high:
        pi = partition_randomized(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)


def analyze_quick_sort(sort_function, arr_size, num_trials=10):
    total_time = 0
    for _ in range(num_trials):
        data = [random.randint(0, arr_size * 10) for _ in range(arr_size)]
        arr_copy = list(data)
        start_time = time.perf_counter_ns()
        sort_function(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.perf_counter_ns()
        total_time += (end_time - start_time)
    avg_time_ms = (total_time / num_trials) / 1_000_000
    return avg_time_ms


if __name__ == "__main__":
    array_sizes = [1000, 5000, 10000]
    trials = 5

    print("--- Analysis of Quick Sort Variants ---")

    for size in array_sizes:
        print(f"\nArray Size: {size}")
        avg_time_det = analyze_quick_sort(quick_sort_deterministic, size, trials)
        print(f"Deterministic Quick Sort (avg over {trials} trials): {avg_time_det:.4f} ms")
        avg_time_rand = analyze_quick_sort(quick_sort_randomized, size, trials)
        print(f"Randomized Quick Sort (avg over {trials} trials): {avg_time_rand:.4f} ms")
