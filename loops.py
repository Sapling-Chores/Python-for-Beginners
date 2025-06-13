# While loop /

i = 0
while i < 5:
    i += 1     # same as i = i + 1
    print(i)

# break 
while True :
    print("Looping forever ")
    break 

# If statement with break

x = 1
while True :
    print(f"Number : {x}")
    x += 1
    if x == 1000:
        break 
    
print("Done")

# Continue 

y = 0
while y<1000:
    y += 1
    if y % 2 == 0 :
     continue  # leaves the even number 
    print(f"Odd Number : {y}")
    
print("Done")

 # else 
p = True 
Number = 0
while p :
    Number  += 1
    if Number % 2 == 1:
        continue
    print(f"Even Number : {Number}")
    if Number == 100:
        print("Done")
        break
else :
    print("Turn p to True ! ")
    
# Nested while loop 

Xaxis = 0
while Xaxis <= 10 :
    Yaxis = 0
    while Yaxis  <=10:
        print(f"x : {Xaxis} y : {Yaxis}")
        Yaxis += 1
    Xaxis +=1     
    
# For loops 

for test in range (5):
    print("this will print 4 times")

# Improved version for the code above !!

for test2 in range (6):
  print(f"Number : {test2}")
print("Done")

for test3 in range (10,20):
    print(test3)
print("Finish")

for test4 in range (10,20,2):
    print(test4)
    if test4 == 16:
      break

# nested loop

for test5 in range (6):
    for test6 in range (6):
        for test7 in range (6):  
          print(f"co-ordinate: {test5},{test6},{test7}")

anime = ["Naruto","Demon","One peice"]
for yo in anime:
    print(yo , end = " ")
print("\n") 

for kiss in "fuck":
    print(kiss)

coordinates = (10, 20, 30)
for point in coordinates:
    print(point)


data = {"name" : "sarfaraz" , "age" : 18}
for data1 in data.items() :
    print(data1)

data2 = {"name" : "Sararaz" , "age " : 17}
for data3 , value in data2.items():
    print(data3,value)


data4 = {"id": "naman" " raj" " sarfaraz", "username" : "sapling"  " aboo"  " baddie"}
for data_give , value in data4.items():
    print(data_give,value)