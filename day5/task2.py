student_scores = [54, 65, 76, 87, 23, 65, 76, 87, 65, 87, 43]
total_student_score = sum(student_scores)
print(total_student_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

max_score = max(student_scores)
print(max_score)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)