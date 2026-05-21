def calculate_cgpa():
    num_subjects = int(input("Enter number of subjects: "))
    total_grade_points = 0
    total_credits = 0
    subjects = []
    grades = []
    credits = []
    for i in range(num_subjects):
        print(f"\nSubject {i+1}")
        subject = input("Enter subject name: ")
        grade_point = float(input("Enter grade point: "))
        if grade_point > 10:
            print("Invalid Grade Point")
            return
        credit = float(input("Enter subject credit: "))
        subjects.append(subject)
        grades.append(grade_point)
        credits.append(credit)
        total_grade_points += grade_point * credit
        total_credits += credit
    cgpa = total_grade_points / total_credits
    percentage = (cgpa - 0.75) * 10
    print("\n      RESULT      ")    
    print("\nSubject-wise Details")
    print("-----------------------------")
    for i in range(num_subjects):
        print(f"{subjects[i]}  |  Grade: {grades[i]}  |  Credit: {credits[i]}")
    print("\n-----------------------------")
    print(f"Total Credits = {total_credits}")
    print(f"CGPA = {cgpa:.2f}")
    print(f"Percentage = {percentage:.2f}%")
    if cgpa >= 9:
        print("Grade: Outstanding")
    elif cgpa >= 8:
        print("Grade: Excellent")
    elif cgpa >= 7:
        print("Grade: Very Good")
    else:
        print("Grade: Good")
calculate_cgpa()
