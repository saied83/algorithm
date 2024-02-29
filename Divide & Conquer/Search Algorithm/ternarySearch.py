#Ternary Search using Recursion
# arr -> Sorted Array
# l -> left pointer
#r -> right pointer
#target --> Target


def ternarySearch(arr, l , r, target):

    #Base Case
    #Return False if Left pointer cross Right pointer
    if l > r:
        return False

    #divide array into Three part using two middle index
    mid1 = l + (r-l)//3         #first mid index
    mid2 = r - (r-l)//3         #second mid index

    #check and return True if two mid indexed value is the target
    if arr[mid1] == target or arr[mid2] == target:
        return True

    else:

        #check if target is in First Part and call the function recursively
        if arr[mid1] > target:
            return ternarySearch(arr, l, mid1-1, target)
        
        #check if target is in last part and call the function recursively
        elif arr[mid2] < target:
            return ternarySearch(arr, mid2+1, r, target)
        
        #otherwise target can be in middle part
        return ternarySearch(arr, mid1+1, mid2-1, target)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 25, 46, 67, 78, 79, 82, 90, 94, 99, 100, 123, 154, 167]
    t = 123
    result = ternarySearch(arr, 0, len(arr)-1, t)
    print(result)

if __name__ == "__main__":
    main()