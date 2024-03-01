# Time Complexity - O(N)

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 25, 46, 67, 78, 79, 82, 90, 94, 99, 100, 123, 154, 167]
    t = 123
    result = search(arr, 0, len(arr)-1, t)
    print(result)

if __name__ == "__main__":
    main()
