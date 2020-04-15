if __name__ == "__main__":
    n = int(input("Enter number of students:"))
    print("Add {} students marks(M/P/C)".format(n))
    marksheet = {}
    for _ in range(n):
        stud = input().split()
        name = stud[0]
        marks = stud[1:]
        marksheet[name] = map(float,marks)

    print(marksheet)

    stud_name = input("Enter student name:")
    print("{0:.2f}".format(sum(marksheet[stud_name])/len(marks)))