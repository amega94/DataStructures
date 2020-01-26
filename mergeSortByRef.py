# Merge Sort passed by reference

def merge(arr, start, end):
    mid = (start + end) // 2
    tmp = []
    i = start
    j = mid + 1
    while (i < mid + 1) and (j < end + 1):
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i < mid + 1:
        tmp.extend(arr[i:mid+1])
    else:
        tmp.extend(arr[j:end+1])
    arr[start:end + 1] = tmp

def mergeSort (arr, start, end):
    if start < end:
        mid = (start+end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, end)
