student_scores = [150, 142, 185, 324, 171, 184, 149, 24, 210, 68, 199, 78, 65, 523, 86, 55, 789, 964, 989]
num = len(student_scores)-1

temp = 0

for i in range(0, (len(student_scores)-1)):
    if student_scores[i] > student_scores[num]:
           temp = student_scores[i]
           student_scores[i] = student_scores[num]
           student_scores[num] = temp

print(student_scores[num])