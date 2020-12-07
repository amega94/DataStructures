# v1 is more effecient (than v2) since it stops looping when the sorting is finished
arr = [99,98,97,100,1,2,3]

for j in range(len(arr) - 1):
    for i in range(len(arr)-1-j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
print(arr)
