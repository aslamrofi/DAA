import time
import random
import csv

# Import the functions from your separate files
from merge_sort import merge_sort
from quick_sort import quick_sort

def get_experimental_time(sort_func, data, repeats=5):
    total_time = 0
    for _ in range(repeats):
        data_copy = data.copy()
        start = time.perf_counter()
        sort_func(data_copy)
        end = time.perf_counter()
        total_time += (end - start)
    return (total_time / repeats) * 1000  # Convert to milliseconds

def run_assignment_tests():
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]

    # Open CSV file to save data for your graphs
    with open('sorting_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write CSV Header
        writer.writerow(["Size", "Case", "MergeSort(ms)", "QuickSort(ms)"])

        # Print Console Header
        print(f"\n{'Size (n)':<10} | {'Test Case':<12} | {'MergeSort (ms)':<15} | {'QuickSort (ms)':<15}")
        print("-" * 61)

        for n in sizes:
            # 1. Average Case: Randomly shuffled elements
            avg_data = list(range(1, n + 1))
            random.shuffle(avg_data)

            # 2. Worst Case for Quicksort (First Elem Pivot): Already Sorted
            worst_data = list(range(1, n + 1))

            # Run Tests
            ms_avg = get_experimental_time(merge_sort, avg_data)
            qs_avg = get_experimental_time(quick_sort, avg_data)

            ms_worst = get_experimental_time(merge_sort, worst_data)
            qs_worst = get_experimental_time(quick_sort, worst_data)

            # Write rows to CSV without decimal points (.0f)
            writer.writerow([n, "Average", f"{ms_avg:.0f}", f"{qs_avg:.0f}"])
            writer.writerow([n, "Worst", f"{ms_worst:.0f}", f"{qs_worst:.0f}"])

            # Print neatly aligned rows to the console without decimal points (.0f)
            print(f"{n:<10} | {'Average':<12} | {ms_avg:<15.0f} | {qs_avg:<15.0f}")
            print(f"{n:<10} | {'Worst':<12} | {ms_worst:<15.0f} | {qs_worst:<15.0f}")
            print("-" * 61)

    print("\nData successfully saved to 'sorting_results.csv' for graphing.")

if __name__ == "__main__":
    run_assignment_tests()