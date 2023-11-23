def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    
    item_greater, item_lower = [], [] 
    pivot = sequence.pop()

    for item in sequence:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)

def main():
    print(quick_sort([5, 8, 2, 6, 9, 1, 0, 7, -1, 10, 4, 4, 3, 3]))

if __name__ == '__main__':
    main()