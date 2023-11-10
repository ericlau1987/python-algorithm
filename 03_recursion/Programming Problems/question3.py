# Write a recursive function that computes the length of a string. 
# You cannot use the len function while computing the length of the string. 
# You must rely on the function you are writing. Put this function in a program that prompts the user to enter a string and then prints the length of that string.

def len_string(string):
    if string =='':
        return 0
    
    return len_string(string[1:]) + 1


def main():
    test = "mmmmmmmmm"
    print(len_string(test))
    print(len_string(test)==len(test))

if __name__ == "__main__":
    main()
    
    