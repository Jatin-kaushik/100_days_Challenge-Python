# Bubble Sort
#Time Complexity -- Best case :-> omega(n), Average case --> theta(n^2) and Worst case = O(n^2)
# Space Complexity -- O(1)
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

def Bubble_Sort(arr):
  for i in range(1,len(arr)):
    for j in range(len(arr)-i):
      if is_small(arr,j+1,j):
        swap(arr,j+1,j)
  return arr

arr = [5,9,8,1,2]
Bubble_Sort(arr)