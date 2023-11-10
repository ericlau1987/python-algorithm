def select(seq, start):
    minIndex = start 

    for index in range(start+1, len(seq)):
        if seq[minIndex] > seq[index]:
            minIndex = index
            # print(minIndex)

    return minIndex 

def selSort(seq):
    for index, value in enumerate(seq):
        minIndex = select(seq, index)
        seq[index], seq[minIndex] = seq[minIndex], seq[index]
        # print(seq)

    return seq 

def main():
    print(selSort([5,2,3,1,0,-1]))

if __name__ == "__main__":
    main()