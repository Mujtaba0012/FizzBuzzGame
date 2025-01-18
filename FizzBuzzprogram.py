#FizzBuzz Program

for number in range(1,51):

    if number % 3 == 0 and number % 5 == 0: #loop through numbers 1 to 50
        print("FizzBuzz") # Divisible by both 3 and 5

    elif number % 3 == 0:
         
         print("Fizz") # Divisble by 3
        
    elif number % 5 == 0 :
       
       print ("Buzz") # Divisible by 5

    else:
       
       print(number) # Not divisible by 3 or 5

