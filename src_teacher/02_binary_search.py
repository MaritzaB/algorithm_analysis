
def binary_search(a, l, h, x):
   
        if h < l:
          return -1
          
        mid = (h + l) // 2
 
        if a[mid] == x:
            return mid
 
        if a[mid] > x:
            return binary_search(a, l, mid - 1, x)
 
        else:
            return binary_search(a, mid + 1, h, x)
 
 
