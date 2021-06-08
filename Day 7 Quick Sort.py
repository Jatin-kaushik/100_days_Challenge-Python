def partition(arr, pivot):
    # 0 to j-1 <= Pivot
    # j to i-1 > pivot
    # i to end =  unknown
    i = 0
    j = 0
    while i < len(arr):
        if arr[i] > pivot:
            i += 1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j += 1
    # print(j)
    return (j-1)

def quick_sort(arr, lo, hi):
    if lo >= hi: #at the time of partioting if len of arr =1 or 0 return None
        return
    pivot = arr[hi] #F.R pivot alwys Last index
    pi = partition(arr, pivot) #lo = start, hi = end
    quick_sort(arr, lo, pi-1)#partioning call
    quick_sort(arr, pi+1, hi)
    return arr


arr = [4, 3, 2, 1, 9, 6, 7, 8]
# print(partition(arr, arr[3]))
lo = 0
hi = len(arr)-1
print(quick_sort(arr,lo,hi))
