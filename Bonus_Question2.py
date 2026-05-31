# Bonus Q 2
student_total_marks = 0.0
num_students = int(input("How many students do you want to enter?  "))
for i in range (num_students):
        print(50 * "-")
        name = input("Enter student name:  ")
        num_marks = int(input(f"How many marks for   {name}  "))
        
        
        

        for j in range (1 , num_marks + 1 ):
            mark = float(input(f"Enter mark {j}  "))
        
            
            student_total_marks += mark
            student_average = student_total_marks / num_marks
    
    
            
            if student_average > 50.0:
                    
                result = "Passed"
            else:
                result = "Failed"    
        print(f"{name}'s average is: {student_average}")
        print(f"Result: {result}")
