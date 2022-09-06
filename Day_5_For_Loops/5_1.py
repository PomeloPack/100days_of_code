student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


student = 0
height = 0

# testovaný input : 156 178 165 171 187

# pro kazdy element z listu student heights
for i in student_heights:
    # tento krok pricte k i jednotlivy input výšky studenta z výše uvedeneho listu ( 156 + 178 + 165 + 171 + 187 = 857)
    student += i
    # po přičtení i ( výšek ) se za každou výšku přičte jeden student ( máme 5 studentů = 857 / 5)
    height += 1

average = round(student / height)
print(average)