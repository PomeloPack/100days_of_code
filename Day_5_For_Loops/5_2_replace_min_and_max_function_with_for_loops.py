student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# test input : 78 65 89 86 55 91 64 89


# replace max() using for loops:
highest_score = 0
for high in student_scores:
    if highest_score < high:
        highest_score = high

print(f"The highest score in the class is: {highest_score}")

# replace min() using for loops:
# lowest_score = 0
# for low in student_scores:
#    if lowest_score > low:
#        lowest_score = low




