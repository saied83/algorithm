#this function will return left most occurrence of an Element from sorted Array
#using Binary Search
#use loop for implement Binary Search

def leftMostOccurrence(arr, target):
    low, high = 0, len(arr)-1
    result = -1
    while low < high:
        mid = (low+high)//2
        if arr[mid] == target:
            result = mid
            high = mid -1
        elif arr[mid] > target:
            high = mid -1
        else:
            low = mid +1
    return result

def main():
    arr = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]
    t = 5
    result = leftMostOccurrence(arr ,t)
    print(result)

if __name__ == "__main__":
    main()