import findOccurrenceBS as fbs

def main():
    arr = [1,2, 3, 4, 5, 5, 5, 5, 5, 5, 7, 89, 89, 96, 100]
    t = int(input("Number you want to search: "))
    firstOccurrence = fbs.findOccurrence(arr, t, True)
    if firstOccurrence == -1:
        print(0)
    else:
        lastOccurrence = fbs.findOccurrence(arr, t, False)
        count = lastOccurrence-firstOccurrence+1
        print(count)

if __name__ =="__main__":
    main()
