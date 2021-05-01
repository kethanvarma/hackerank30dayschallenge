n = int(input())
total = [0] * 5

for i in range(n):
    marks = []
    stu_marks = input().split()
    marks.extend(stu_marks[1:])

    marks = list(map(int,marks))
    for i in range(5):
        total[i] = total[i] + marks[i]

print(total)

