def findRotationCount(arr):
    low, high = 0, len(arr)-1
    while(low < high):
        if arr[low] <= arr[high]:
            return low
        mid = (low + high)//2
        next = (mid+1)%len(arr)
        prev = (mid + len(arr)-1)%len(arr)
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid -1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    return -1

def main():
    arr = [12, 13, 14, 25, 26, 3, 4, 5, 6, 7, 8, 10]
    count = findRotationCount(arr)
    print(count)

if __name__ == "__main__":
    main()