def revList(lst):

    if lst == []:
        return []
    
    rerestrev = revList(lst[1:])
    first = lst[0:1]

    result = rerestrev + first 

    print(f'lst[1:]: {lst[1:]}; rerestrev: {rerestrev}; first: {first}; result: {result}')

    return result 

def main():
    print(revList([1,2,3,4]))

if __name__ == "__main__":
    main()