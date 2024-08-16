import time 

beg = input("Would you like to set a timer for minutes or seconds? ")
start = int(input("How long would you like to set a timer for? "))

if beg.lower() == "seconds":
    for i in range(0, start):
        print(i)
        time.sleep(1)
    print("TIME IS UP!")

        
elif beg.lower() == "minutes":
    for x in range(0, start):
        print(x)
        time.sleep(60)
    print("TIME IS UP!")

else:
    print("Invalid input. Try again soon!")
    quit()



  
        
