def merge(arr_1, arr_2):
    arr_1 = arr_1[:]
    arr_2 = arr_2[:]
    
    new = []
    
    while (arr_1 and arr_2):
        if (arr_1[0] < arr_2[0]):
            new.append(arr_1[0])
            arr_1.pop(0)
        else:
            new.append(arr_2[0])
            arr_2.pop(0)
    
    new += arr_1 + arr_2
    
    return new
    
arr_1 = []
arr_2 = [10, 20, 30]

print(merge(arr_1, arr_2))
