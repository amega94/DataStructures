myarray = [99,98,97,100,1,2,3]

def bubblesort ( myarray ):
    swap = True
    count = len(myarray)
    while swap:
        swap = False
        for i in range(count-1):
            if myarray[i] > myarray[i+1]:
                myarray[i], myarray[i+1] = myarray[i+1], myarray[i]
                swap = True
        count -= 1
    return myarray 
  
print( bubblesort(myarray) )  
