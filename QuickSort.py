def partition(Array, low, high):
    pivot = Array[high]
    i=low-1
    for j in range(low,high):
        if Array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i=i+1
            # swapping element at i with element at j
            (Array[i], Array[j]) = (Array[j], Array[i])
    # swap the pivot element with the greater element specified by i
    (Array[i + 1], Array[high]) = (Array[high], Array[i + 1])
    return i+1 # return pivot position 
    
def quickSort(Array, low, high):
  if low < high:
      # find pivot element such that
      # element smaller than pivot are on the left
      # element greater than pivot are on the right
      pi = partition(Array, low, high)
      # left of pivot recursion
      quickSort(Array, low, pi - 1) 
      #right of pivot recursion
      quickSort(Array, pi + 1, high)  
    
Array=[9, 7, 5, 11, 12, 2, 14, 3, 10, 6];
print('Unsorted Array ')
print(Array)
size =len(Array)
quickSort(Array, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(Array)
