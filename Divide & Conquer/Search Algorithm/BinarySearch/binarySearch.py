#Ternary Search using Recursion
# arr -> Sorted Array
# l -> left pointer
#r -> right pointer
#target --> Target

# Time Complexity - O(log(N))
def binarySearch(arr, l , r, target):

    #Base Case
    #Return -1 if Left pointer cross Right pointer
    if l > r:
        return -1

    #divide array into Two part using one mid index
    mid = l + (r-l)//3         #mid index

    #check and return index of target if indexed value is the target
    if arr[mid] == target:
        return mid

    #check if target is in First Part and call the function recursively
    elif arr[mid] > target:
        return binarySearch(arr, l, mid-1, target)
    
    #check if target is in last part and call the function recursively
    elif arr[mid] < target:
        return binarySearch(arr, mid+1, r, target)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 25, 46, 67, 78, 79, 82, 90, 94, 99, 100, 123, 154, 167]
    t = 123
    result = binarySearch(arr, 0, len(arr)-1, t)
    print(result)

if __name__ == "__main__":
    main()