### v1: MERGE BY VALUE 

def merge(arr_1, arr_2):
    i = j = 0
    new = []
    
    # 'try-catch' to supress exception raised in corner-case (i.e. when arr_1 or arr_2 is empty!)
    try:
        if arr_1[i] > arr_2[j]:
            new.append(arr_2[j])
            j += 1
        else:
            new.append(arr_1[i])
            i += 1
    except Exception:
        pass    
        
    if i == len(arr_1):
        new += arr_2[j:]

            
    if j == len(arr_2):
        new += arr_1[i:]
    
    return new

arr_1 = [1]
arr_2 = [10, 20, 30]

print(merge(arr_1, arr_2))
