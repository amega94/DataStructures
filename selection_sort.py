myarr = [10,200,3,4]

def findmin (arr,start):
    min = start
    for i in range(start+1,len(arr)):
        if (arr[i] < arr[min]):
            min = i
    return min
    
def selectionsort (arr):
    for i in range(len(arr)):
        min = findmin(arr, i)
        arr[min], arr[i] = arr[i], arr[min]
    return arr
    
    
print(selectionsort(myarr))
