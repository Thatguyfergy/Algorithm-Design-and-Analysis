import generateLists
import sortingFunctions


def HybridSorting(x, n, S):
    list = generateLists.generate_random_list(x, n)
    comparisons, time_taken = sortingFunctions.HybridSort(list, S)
    print(f"x used: {x}")
    print(f"n used: {n}")
    # print(f"S used: {S}")
    return comparisons, time_taken


def MergeSorting(x, n):
    list = generateLists.generate_random_list(x, n)
    comparisons, time_taken = sortingFunctions.MergeSort(list)
    print(f"x used: {x}")
    print(f"n used: {n}")
    return comparisons, time_taken
