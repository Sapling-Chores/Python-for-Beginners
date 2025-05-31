import math

#Some basic operation in maths :

print(12+3) # 15
print(21-1) #20
print(4*2)  # 8
print(8/2)  #4.0 , 
print(26//5) #5  , 
print(26.0//5)
print(82%4)  #2 , 
print(5**3)  # 125

# operand Precedence

print(8*2+4) # 20
print(8/2-2) # 2
print(8*2/4+2) #6.0
print(4/2*8+2) #18
print(2**3+2/2) #9.0
print(2**3**2) # 512
print(2**1**4) #2
print((2+1)**3/3+1) #10.0
print(3**2/(2+1)*2/2-3) # 0.0

# Maths module

print(math.pi) #3.141592653589793
print(math.e)  #2.718281828459045

print(math.ceil(1.223))   # 2
print(math.floor(34.456)) # 34
print(math.trunc(234.2345678)) # 234

print(math.sqrt(9)) # 3.0
print(math.sqrt(3)) # 1.7320508075688772
print(math.pow(3,4)) # 81.0
print(math.exp(2))   # 7.38905609893065
print(math.log(64,2)) # 6.0
print(math.log(10)) #2.302585092994046
print(math.log(10,math.e )) #2.302585092994046
print(math.log(math.pi,math.e)) #1.1447298858494002
print(math.log10(10)) # 1.0

print(math.sin(30*math.pi/180)) # ~ .5
print(math.tan(45*math.pi/180)) # 0.9999999999999999
print(math.cos(0)) # 1.0
print(math.tan(60*math.pi/180)) # 1.7320508075688767
print(math.cos(60*math.pi/180)) # 0.5000000000000001

print(math.degrees(math.pi)) # 180.0
print(math.degrees(math.pi/6)) # 29.999999999999996
print(math.radians(180)) # 3.141592653589793
print(math.radians(60)) # 1.0471975511965976
print(math.radians(30)) # 0.5235987755982988

print(math.tan(math.radians(30))) # 0.5773502691896257
print(math.tan(math.radians(45))) # .9999999999998
print(math.sin(math.radians(0)))  # 0.0
print(math.tan(math.radians(90))) #ifnity

print(math.gcd(100,120)) #20
print(math.gcd(4,5)) #1
print(math.lcm(12,4,6,5)) #60
print(math.lcm(3,6,8,4)) #24
print(math.isqrt(17)) #4
print(math.isqrt(35)) #5
print(math.isqrt(37)) #6
