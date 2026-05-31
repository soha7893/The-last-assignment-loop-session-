item_count = 0
total_price = 0
most_expensive = None
the_cheapest = None

while True:
    item_price = float(input("Enter item price or 0 to finish "))
    if item_price == 0 :
        break
    item_count +=1
    total_price += item_price
    if most_expensive is None or item_price > most_expensive :
        most_expensive = item_price
    if the_cheapest is None or item_price < the_cheapest :
        the_cheapest = item_price
    if item_count == 0:
        print ("No items were added")    
    else:
        average_price = total_price / item_count
    print(f"Number of items: {item_count}")
    print(f"Total price: {total_price}") 
    print(f"Average item price:{average_price}")
    print(f"Most expensive item: {most_expensive}") 
    print(f"Cheapest item: {the_cheapest}") 
    print (50*"=") 
    # Q 2
    num_students = int(input("How many students do you want to enter?  "))
    for i in range (num_students):
        print(50 * "-")
        name = input("Enter student name:  ")
        num_marks = int(input(f"How many marks for {name}"))
        student_total_marks = 0.0
        for j in range (1,num_marks + 1):
            mark = float(input(f"Enter mark {j}"))
            student_total_marks += mark
            if num_marks > 0 :
                student_average = student_total_marks / num_marks
                if student_average > 50:
                    result = "Passed"
                else:
                    result = "Failed"    
            print(f"{name}'s average is: {student_average}")
            print(f"Result: {result}")



            
               
            
            
              
            

                          
    
    



