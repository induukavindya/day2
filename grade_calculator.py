# Student Grade Calculator

while True:
    # Ask for student's name
    name = input("Enter the student's name: ")
    
    if name.lower() == "exit":
        break
    
    # Ask for 3 subject marks
    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    
    # Calculate the average
    average = sum(marks) / len(marks)
    
    # Assign grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    # Display result
    print("-" * 30)
    print(f"Name   : {name}")
    print(f"Average: {average:.1f}")
    print(f"Grade  : {grade}")
    print("-" * 30)