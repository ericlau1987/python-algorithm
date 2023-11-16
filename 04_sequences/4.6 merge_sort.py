def merge(seq, start, mid, stop):
    
    lst = []
    i, j = start, mid 

    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1

        else:
            lst.append(seq[j])
            j += 1

    while i < mid:
        lst.append(seq[i])
        i += 1

    for i in range(len(lst)):
        seq[start+i] = lst[i]

def mergeSortRecursively(seq, start, stop):
    if start >= stop -1:
        return 
    
    mid = (start+stop) // 2 

    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)

    merge(seq, start, mid, stop)

def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))


def main():
    seq = [5,2,3,1,0,-1,4]
    mergeSort(seq)
    print(seq)

if __name__ == "__main__":
    main()

