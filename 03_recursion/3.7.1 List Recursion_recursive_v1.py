def revList(lst):

    def revListHelper(index):

        if index == -1:
            return []
        
        restrev = revListHelper(index-1)
        first = [lst[index]]

        result = first + restrev

        print(f'rerestrev: {restrev}; first: {first}; result: {result}')

        return result 
    
    return revListHelper(len(lst)-1)


def main():
    print(revList([1,2,3,4]))

if __name__ == "__main__":
    main()