marks = [90, 25, 67, 45, 80]

for num in range(len(marks)): # len(marks)가 5이므로 range(5)와 같음.
    if marks[num] < 60:
        continue
    print("Student %d passed. Congratulations!" %(num+1))