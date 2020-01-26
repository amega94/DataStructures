# Recursively printing array elements by reference

if start > end ==> case when list is empty
if start == end ==> base case when a return is neccessary
if start < end ==> Keep the recursion going

def printer (arr, start, end):
  if start > end:
    return
  elif start == end:
    print(arr[start])
    return
  else: # equiv to start < end
    mid = (start+end)//2
    printer (arr, start, mid)
    printer (arr, mid+1, end)

Tests printer(arr, start, len(arr)-1): 

1. arr = [] -> Returns with nothing. ✔
2. arr = [1] -> print 1 to console . ✔
3. arr = [1,2,3,4] -> print 1\n2\n3\n4\n. ✔


This CONDITION start < end is used in "famous" sorting algorithms and its important to understand why this is the case.

 
 
