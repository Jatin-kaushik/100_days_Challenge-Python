# Python program for implementation of MergeSort
# Time Complexity -- Best case :-> omega(n), Average case --> theta(n) and Worst case = O(n)
# Space Complexity -- O(n)
def merge_array(arr1, arr2):
    res_array = [None] * (len(arr1) + len(arr2))
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res_array[k] = arr1[i]
            i += 1
            k += 1
        else:
            res_array[k] = arr2[j]
            j += 1
            k += 1

    while i < len(arr1):
        res_array[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        res_array[k] = arr2[j]
        j += 1
        k += 1
    return res_array


arr1 = [1, 3, 5, 7, 8, 9]
arr2 = [2, 4, 6, 10, 11, 24]
print(merge_array(arr1, arr2))
