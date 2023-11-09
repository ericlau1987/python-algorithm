# Write a recursive function called intpow that given a number, x, and an integer, n, will compute x ^ n. 
# You must write this function recursively to get full credit. 
# Be sure to put it in a program with several test cases to test that your function works correctly.

def intpow(x, n):
    if n == 0:
        return 1
    
    # restrev = intpow(x, n-1)
    # result = restrev * x 

    return intpow(x, n-1) * x


def main():
    print(intpow(3,3))
    print(intpow(10,2))
    print(intpow(4,3))

if __name__ == "__main__":
    main()