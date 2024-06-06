import time
import generateLists

comparisons = 0


def compare(a, b):
    global comparisons
    comparisons += 1
    if a <= b:
        return True
    else:
        return False


# implement the sorting functions
def insertion_sort(list):
    global i_comparisons
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while (j >= 0) and compare(key, list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list


def merge(left, right):
    merged_list = []
    l = 0
    r = 0
    ll = len(left)
    rr = len(right)
    while l < ll and r < rr:
        if compare(left[l], right[r]):  ## even if same, remove from left first
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[r])
            r += 1
    if l == ll:  ## thus left more likely to hit 0 elements first, can just concatenate
        merged_list.extend(right[r:])
    else:
        merged_list.extend(left[l:])
    return merged_list


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        array = merge(left_half, right_half)

        return array


def hybrid_sort(array, S):
    if len(array) <= S:
        array = insertion_sort(array)
    else:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        left_half = hybrid_sort(left_half, S)
        right_half = hybrid_sort(right_half, S)

        array = merge(left_half, right_half)

    return array


def check_sorted(slist):
    for i in range(1, len(slist)):
        if slist[i - 1] > slist[i]:
            return False
    return True


def HybridSort(list, S):
    global comparisons
    comparisons = 0
    print("Start of Hybrid Sort")
    print("Hybrid Sorting!!!")
    start_time = time.time()
    sorted_list = hybrid_sort(list, S)
    end_time = time.time()
    print("End of Hybrid Sort")
    if check_sorted(sorted_list):
        print("List is Checked and it is Sorted!!")
    else:
        print("Not Sorted! Try Again!")
    print(f"S used: {S}")
    print(f"Comparisons: {comparisons}")
    time_taken = end_time - start_time
    print(f"The Time Taken: {time_taken:5f}s")
    return comparisons, time_taken


def MergeSort(list):
    global comparisons
    comparisons = 0
    print("Start of Merge Sort")
    print("Merge Sorting!!!")
    start_time = time.time()
    sorted_list = merge_sort(list)
    end_time = time.time()
    print("End of Merge Sort")
    if check_sorted(sorted_list):
        print("List is Checked and it is Sorted!!")
    else:
        print("Not Sorted! Try Again!")
    print(f"Comparisons: {comparisons}")
    time_taken = end_time - start_time
    print(f"The Time Taken: {time_taken:5f}s")
    return comparisons, time_taken
