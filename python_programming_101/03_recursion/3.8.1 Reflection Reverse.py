def reverse(seq):
    seqType = type(seq)
    emptySeq = seqType()

    if seq == emptySeq:
        return emptySeq
    
    restrev = reverse(seq[1:])
    first = seq[0:1]
    result = restrev + first

    return result 

def main():
    print(reverse([1,2,3,4]))
    print(reverse("hello world"))

if __name__ == "__main__":
    main()