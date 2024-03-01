#this function will return left most occurrence of an Element from sorted Array
#using Binary Search
#use loop for implement Binary Search

def findOccurrence(arr, target, searchFirst):
    low, high = 0, len(arr)-1
    result = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            result = mid
            if searchFirst:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

def main():
    arr = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]
    t = int(input())
    leftMostOccurrence = findOccurrence(arr ,t, True)
    rightMostOccurrence = findOccurrence(arr ,t, False)
    print(f"Left Most Occurrence of {t} is {leftMostOccurrence}")
    print(f"Right Most Occurrence of {t} is {rightMostOccurrence}")

if __name__ == "__main__":
    main()