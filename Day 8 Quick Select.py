# Python program for implementation of Quick select means search element at index
# Time Complexity -- Worst case :-> O(n),


def partition(arr, pivot):
    # 0 to j-1 <= Pivot
    # j to i-1 > pivot
    # i to end =  unknown
    i = 0
    j = 0
    while i< len(arr)-1:
        if arr[i]>pivot:
            i+=1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j+=1
    return (j-1)
def quick_select(arr,lo,hi,search_index):
    if lo>= hi:
        return
    pivot =  arr[hi]
    p_ind = partition(arr,pivot)
    if p_ind == search_index:
        return (f'element present at the index {p_ind} is {arr[p_ind]}')
    elif p_ind > search_index:
        quick_select(arr,lo,p_ind-1,search_index)
    else:
        quick_select(arr,p_ind +1, hi, search_index)

arr = [4, 3, 2, 1, 9, 6, 7, 8]
lo = 0
hi = len(arr) - 1
print(quick_select(arr, lo, hi, 5))