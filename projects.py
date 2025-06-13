# 1 

# Car game
import time
import math

car_key = '7808'
car_password = input("Enter car password : ")
if car_password.strip() == car_key:
 print("Access granted")
 while car_password.strip() == car_key:
     start = input("Type start to continue").lower()
     if start == "start":
      while start == "start":
         i = 3
         while i>=0:
             print(i)
             i = i-1
             time.sleep(1)
         print("Vroom vroom >>!!","Car engine has started !!",sep="\n")
         break
      c_s = input("Press 'continue' to start your journey  : ")
      if c_s == "continue":
       while c_s == "continue":
        destination1 = input("Speed (integer):")
        destination2 = input("Distance(integer) :")
        Time = int(destination2)/int(destination1)
        for j in range(round(Time)):
            print(f"Journey time spent {j}")
            time.sleep(1)
        print("You have reached on the destination ")
        final = input("Engine is still start press 'stop' or 'continue' ")
        if final == "continue":
            while final == "continue"  :
                destination1 = input("Speed (integer):")
                destination2 = input("Distance(integer) :")
                Time = int(destination2)/int(destination1)
                for j in range(round(Time)):
                    print(f"Journey time spent {j} s")
                    time.sleep(1)
                    print("You have reached on the destination ","Car Engine is too hot,it need to cool down ",sep = "\n")
                    break
                break
            break
        elif final == "stop":
         print("car Engine has stopped running")
         break
        break
       break
      elif c_s == "start":
       print("The engine is already running ")

      else :
          print("Invalid prompt!!")
          break
     elif start == "stop":
        print("Car engine is already stopped !!")
        break
else :
    print("Access denied")