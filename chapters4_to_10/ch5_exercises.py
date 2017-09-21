import math

week_days = ["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def what_week_day(day_number):
    if day_number % 7 == 0:
        return "Monday"
    elif day_number % 7 == 1:
        return "Tuesday"
    elif day_number % 7 == 2:
        return "Wednesday"
    elif day_number % 7 == 3:
        return "Thursday"
    elif day_number % 7 == 4:
        return "Friday"
    elif day_number % 7 == 5:
        return "Saturday"
    else:
        return "Sunday"


def exam_mark(mark):
    if mark >= 75:
        return 'First'
    elif mark >= 70:
        return 'Upper Second'
    elif mark >= 60:
        return 'Second'
    elif mark >= 50:
        return 'Third'
    elif mark >= 45:
        return 'F1 Supp'
    elif mark >= 40:
        return 'F2'
    else:
        return 'F3'


def evaluating_exam_mark():
    xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39, 9, 2, 9]
    for x in xs:
        print("Your mark was", x, "and that gives you a grade of", exam_mark(x))


def find_hypot(x, y):
    c = (x**2 + y**2)**(1/2)
    return c


def is_rightangled(a, b, d):
    if abs(find_hypot(a, b) - d) < 0.000001:
        return True
    else:
        return False

a = math.sqrt(2.0)
print(a, a**a)
print(a*a == 2.0)

if __name__ == "__main__":
    #print(what_week_day(999))
    # print(exam_mark(74))
    # evaluating_exam_mark()
    print(find_hypot(5, 5))
    print(is_rightangled(5, 5, 7.071067))

