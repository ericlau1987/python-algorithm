def recSumFirstN(n):
    if n == 0:
        return 0
    else:
        print(f'n: {n}')
        return recSumFirstN(n-1) + n 

def main():
    x = int(input("please enter a non-negative integer:"))

    if x:

        s = recSumFirstN(x)

        print(f'The sum of the first is {x} and integer is {s}')

    else:
        print("x is empty")


if __name__ == "__main__":
    main()