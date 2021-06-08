# imp problems on Partitioning ;- (<= pivot, >pivot), (odd-even), (0,1), (0, non zero)
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


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
            swap(arr, i, j)
            i += 1
            j += 1
    return arr


arr = [4, 3, 2, 1, 9, 6, 7, 8]
print(partition(arr, arr[3]))
