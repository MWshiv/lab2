
def adding(last, first):
    f = open('students.txt', 'r+', encoding="utf8")
    stud = f.readlines()
    lines = list(line.strip() for line in stud)
    s = last + " " + first
    if s in lines:
        return print("Такой студент уже есть ")
    else:
        lines.append(s)
    lines.sort()

    f = open('students.txt', "w", encoding="utf8")
    for line in lines:
        f.write(line + "\n")


def find(last, first=" "):
    f = open('students.txt', 'r+', encoding="utf8")
    stud = f.readlines()
    lines = [line.strip() for line in stud]
    s = last + " " + first
    if first != " ":
        if s in lines:
            return print("Такой студент есть")
        else:
            return print("Такого студента нет")
    else:
        for line in f:
            if last in lines:
                return print(lines)


def delete(last, first=" "):
    f = open('students.txt', 'r+', encoding="utf8")
    stud = f.readlines()
    lines = [line.strip() for line in stud]
    if first != " ":
        s = last + " " + first
        if s in lines:
            lines.remove(s)
        else:
            return print("Такого студента нет")
        lines.sort()
    else:
        find(lastname)
        first = input("Введите имя студента ")
        s = last + " " + first
        if s in lines:
            lines.remove(s)
        else:
            return print("Такого студента нет")
        lines.sort()

    f = open('students.txt', "w", encoding="utf8")
    for line in lines:
        f.write(line + "\n")


def edit(last, first, nlast=" ", nfirst=" "):
    f = open('students.txt', 'r+', encoding="utf8")
    stud = f.readlines()
    lines = [line.strip() for line in stud]
    s = last + " " + first
    if s in lines:
        if nlast == " ":
            nlast = last

        if nfirst == " ":
            nfirst = first

        delete(last, first)
        adding(nlast, nfirst)
    else:
        return print("Такого студента нет")


