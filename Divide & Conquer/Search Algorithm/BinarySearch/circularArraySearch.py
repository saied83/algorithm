def circularArraySearch(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        if arr[mid] <= arr[high]:
            if arr[mid] <target and target < arr[high]:
                low = mid +1
            else:
                high = mid -1
        elif arr[mid] >= arr[low]:
            if arr[low] < target and target < arr[mid]:
                high = mid -1
            else:
                low = mid +1
    return -1

def main():
    arr = [23, 24, 26, 26, 1, 2, 2, 3, 4]
    t = 24
    result = circularArraySearch(arr, t)
    print(result)

if __name__ == "__main__":
    main()