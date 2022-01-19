def bubblesort(array):
    for i in range(0,len(array)-1):
        swapped = 0
        
        for j in range(0,len(array)-1):
            if(array[j]>array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                
                swapped = 1
        
        if swapped == 0 :
            break
        
array = [-1,3,46, 47,62,23,56,43]
bubblesort(array)
print(array)
