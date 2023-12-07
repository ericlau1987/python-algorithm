def countStudents(students: list[int], sandwiches: list[int]) -> int:
    
    n = len(students)
    unable_eat_count = 0
    count = 0 

    while n > 0:
        curr_student = students[0]
        curr_sandwich = sandwiches[0]

        if curr_student == curr_sandwich:
            n -= 1
            students.pop(0)
            sandwiches.pop(0)

        else:
            students.append(students.pop(0))
            unable_eat_count += 1

        print(f'student: {students}; sanwiches: {sandwiches}')

        # break

    return unable_eat_count
    

def main():
    n = countStudents(students=[1,1,0, 0], sandwiches=[0, 1,0,1])
    print(n)

if __name__ == "__main__":
    main()