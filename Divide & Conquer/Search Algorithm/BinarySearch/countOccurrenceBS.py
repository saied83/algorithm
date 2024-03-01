import leftmostOccurrenceBS as lbs
import rightmostOccurrenceBS as rbs

def main():
    arr = [1,2, 3, 4, 5, 5, 5, 5, 5, 5, 7, 89, 89, 96, 100]
    firstOccurrence = lbs.leftMostOccurrence(arr, 5)
    lastOccurrence = rbs.rightMostOccurrence(arr, 5)
    count = lastOccurrence-firstOccurrence+1
    print(count)

if __name__ =="__main__":
    main()
