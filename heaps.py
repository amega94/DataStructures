# Max Heap: Parents >= Children
# Min Heap: Parents <= Children

#Max Heap --Condition--> Children are smaller than their parents. 
#This means that a lower level can have a node with a higher val than an upper node (in Max Heap)

#Removing an element is done from the top (i.e root node). 
# 1. Remove top element (at the root)
# 2. Bring the bottom right element to replace the root element
# 3. Comparing parent with both children until condition is met!


#Adding an element is done at the bottom right. 
# 1. Comparing to parent until condition is met!

''' Some useful functions for this data structure
   17
  /  \
 15   9
/ \  / \
1 12 3 8
1) Getting the children values from the parent
heap = [17, 15, 9, 1, 12, 3, 8] --> The heap is stored in a list with the following order
Lchild(heap[i=0]) = 2*i + 1 = 2*0 + 1 = 1
Rchild(heap[i=0]) = 2*i + 2 = 2*0 + 2 = =2
The above two equations are used as we trickle down the top node (i.e. step 3 in Removing an element)

2) Getting the parent value from the children
We can rearrange the above two equations to get the parent's position from the child

i (parent's position) = (Lchild - 1)/(2)
i (parent's position) = (Rchild - 2)/(2)

So the twist is that you have to know if you are a right or left child to use appropriate equation.

This is actually not True. For example: What is the parent of a) node 3? b) node 8?

a) We know that the parent of 3 is 9. However the code doesn't.

using i = (L-1)/(2)
using i = (L-2)/(2)

If we assume that 3 is left child of 9 --> i=(L-1)/(2)=(5-1)/(2)=2
If we assume that 3 is right child of 9--> i=(R-2)/(2)=(5-2)/(2)=1.5

Note that we can use R equation and round up and we don't need to know anything more.

b) We know that the parent of 8 is 9. We also know that 8 is the right child of 9. The code doesn't.

If we assume that 8 is left child of 9 --> i=(L-1)/(2)=(6-1)/(2)=2.5
If we assume that 8 is right child of 9 --> i=(R-2)/(2)=(6-2)/(2)=2

Note that we can use R equation and roud up or L equation and round down. Both strategies
will give us the same results.



Implementation of Max Heap
'''

class Heap:
    def __init__(self):
        self._list = []
        
    def append(self, val):
        child = len(self._list)
        self._list.append(val)
    
        parent = round((child-1)/2)
        while ( (((child-1)/2) >= 0) & (self._list[child] > self._list[parent]) ):
            #First condition makes sure that there is at least one element in the list
            #If the list is empty, child = 0 --> p = (child-1)/2 = -0.5
            #If the list has one element, child = 1 --> p = (1-1)/2 = 0
            #The first condition is very important, since in Python round(-0.5) = -1 and list[-1] returns the last element in a list
            self._list[child], self._list[parent] = self._list[parent], self._list[child]
            child = parent
            parent = round((child-1)/2)
    
    def delete(self):
        if ( len(_list) == 0 ):
            print("Heap is Empty")
        else:
            self._list[0] = self._list[len(_list)-1]
            self._list = self._list[:-1]
            
            //trickle down
            if ()
            
            

myheap = Heap()
myheap.append(5)
print(myheap._list)
myheap.append(6)
print(myheap._list)
myheap.append(7)
print(myheap._list)
myheap.append(70)
print(myheap._list)
