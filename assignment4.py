#Q 1 Mutiplication Table
user_number = int (input ("enter a number  :  "))
for number in range (1, 11):
    result = user_number * number
    print (f"{user_number} X {number} = {result}")
print ( 50* "=" )
#Q 2 Count even number
counter = 0
for i in range (1, 31):
    if i %2 == 0:
        print (f"{i}")
        counter += 1
print (f"Total even number = {counter} ") 
print ( 50* "=" )
#Q 3 Password Attempt
correct_password = "python123"
attemps = 0
max_attemps = 3
while attemps < max_attemps:
    user_password = input("Please enter your password:  ")
    attemps += 1
    if user_password == correct_password:
        print("Acess granted")
        break
    else:
        if attemps == max_attemps:  
            print("Account locked")
        else:
            print("Incorrect password, try again")

#Q 4 Calculate Average Marks
input_user_mark = int(input("How many marks do you want to enter?  "))
total_marks = 0
count = 1
while count <= input_user_mark:
    mark = float(input(f"Enter mark {count} "))
    total_marks += mark
    count +=1
average = total_marks / input_user_mark
print (f"Average: {average}")
print ( 50* "=" )
#Q 5 Number Guessing Game
secret_number = 7
while True:
    user_guess_number = int(input("Guess the number :  "))
    if user_guess_number > secret_number:
        print("Too high")
    elif user_guess_number < secret_number:
     print ("Too low")
    elif user_guess_number == secret_number:
           print ("correct !")
           break  
#Q 6 Simple ATM menu
balance = 100
while True:
    print ("1. Check balance")
    print ("2. Deposite money")
    print ("3. Withdraw money")
    print ("4. Exit")
    user_choice = int(input("Please enter an option (1-4):  "))
    if user_choice == 1:
        print (f"current balance is: {balance}")
    elif user_choice == 2:
        deposit_amount = float (input("Enter amount you want to deposite:  "))
        balance += deposit_amount
        print(f"You deposited {deposit_amount}. Your new balance is: {balance}")
    elif user_choice == 3:
        withdraw_amount = float(input("Enter amount you want to withdraw:   "))
        if withdraw_amount > balance:
            print ("insufficient balance")
        else:
            balance -= withdraw_amount
            print(f"you withdrawed {withdraw_amount}.the remaining balance is:{balance}")            
    elif user_choice == 4:
        print ("thank you!")
        break
    else:
        print("Invalid optin, please choose a valid option (1-4)")





          