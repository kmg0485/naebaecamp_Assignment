def get_grade(score):
    if 91 <= score <= 100:
        return "A"
    elif 81 <= score <= 90:
        return "B"
    elif 71 <= score <= 80:
        return "C"
    else:
        return "F"

score = int(input())
grade = get_grade(score)
print(grade) # A ~ F