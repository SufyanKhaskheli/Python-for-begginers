""""
variables in python are basically containers
which store a specific value
you store a value/string in variable and then you can recall this again and again
"""

x="hi" # string variable
y=4 #integer variable
z= 36.7 #floating variable
m="bye"
a="4" #string
b="7" #string

print(type(x))
print(type(y))
print(type(z))
#all these print commands will tell us the type of variable

print(x*y)
print(y+z)

#you cant do any function with x and z together separately since one is a string and other one is a floating point

print (int(a)+int(b))#TYPE CASTING: if we want to convert from string to int we
"""
str()
int()
float()
"""

print(100*str(int(a)+int(b)))
"""
now persay if you want to print something 100 times normally it would be to multiply it by 100
but in this above print we initialize a and b as strings and multiply.
this is because otherwise 100 would multiply by int a and inturn not print our desired value 100 times
"""

##TAKING INPUT FROM THE USER
print("ENTER YOUR NUMBER")
inpnum=input() #THIS IS A STRING AT THIS POINT. its builtin that it will go as a string
print("you entered", inpnum)
#in order to convert it to an integer we do this print("you entered", " int(ipnum))
#print("you entered",int(inpnum)+5)




