import sys

# Increase recursion depth for the worst-case analysis (already sorted arrays)
sys.setrecursionlimit(20000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Pivot is the first element
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)