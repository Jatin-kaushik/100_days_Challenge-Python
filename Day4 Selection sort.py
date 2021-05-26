# Python program for implementation of MergeSort
# Time Complexity -- Best case :-> omega(n^2), Average case --> theta(n^2) and Worst case = O(n^2)
# Space Complexity -- O(1) #In place algorithm
arr = [5,9,8,1,2]
def is_small(arr, i,j):
  print("Comparing" + str(arr[i])+ "and" + str(arr[j]))
  if arr[i] < arr[j]:
    return True
  else:
    return False
def swap(arr,i,j):
  print("Swapping" + str(arr[i])+ "and" + str(arr[j]))
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def selection_sort(arr):
  for i in range(len(arr)-1):
    min_index = i #storing minimum index
    for j in range(i+1,(len(arr))):
      if is_small(arr,j,min_index) is True:
        min_index = j
    swap(arr,i,min_index)
  return arr

selection_sort(arr)
print(arr)