# Write a recursive function that takes a string like “abcdefgh” and returns “badcfehg”. 
# Call this function swap since it swaps every two elements of the original string. 
# Put this function in a program and call it with at least a few test cases.

def swap(x):
    if x == "":
        return ""
    
    restrev = swap(x[2:])
    swap_first_two = x[1] + x[0]
    result = swap_first_two + restrev

    return result 

def main():
    print(swap("abcdefgh"))
    print(swap("bcdefg")=="cbedgf")

if __name__ == "__main__":
    main()