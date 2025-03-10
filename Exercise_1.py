# Python code to implement iterative Binary  
# Search. 
#Time Complexity:- O(log n)
#Space Complexity:- O(log n)
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  #Check base case
  if r>=l:
    mid=(r+l)//2

    #If the element is present in the middle itself
    if arr[mid]==x:
       return mid

     #If element is smaller than mid, then it can only
     # be present in a left subarray
    elif arr[mid]>x:
        return binarySearch(arr, l, mid-1, x)

     #Else the element can only be present in right subarray
    else:
      return binarySearch(arr, mid+1, r,x)

  else:
     #Element is not present in the array
     return -1
    
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
