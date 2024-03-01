import findOccurrenceBS as fbs

def main():
    arr = [1,2, 3, 4, 5, 5, 5, 5, 5, 5, 7, 89, 89, 96, 100]
    target = int(input("Number you want to search: "))
    firstOccurrence = fbs.findOccurrence(arr, 5, True)
    lastOccurrence = fbs.findOccurrence(arr, 5, False)
    count = lastOccurrence-firstOccurrence+1
    print(count)

if __name__ =="__main__":
    main()
