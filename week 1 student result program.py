def total_marks(marks):
    return sum(marks)


def average_marks(total):
    return total / 3


def grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))

marks = [m1, m2, m3]

total = total_marks(marks)
average = average_marks(total)
result = grade(average)

print("\nName:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", result)