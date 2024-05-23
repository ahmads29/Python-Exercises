#====================================Formating===================================#
#Sting Formating:
name="welcome to python"
print(name.upper())
print(name.lower())
print(name.find("e"))
print(name.find("E"))
print(name.replace("to","2"))
print(name)
print("python" in name)

#opperations formating:
minimum=min(10,23,32,54,65,4)
print(minimum)        #as the bellow
print(f"{minimum}")

maximum=max(23,34,54,12,64,76,43,63)
print(f"{maximum}")
print(maximum)

#=================================================================================#

#==================================B-In functions=================================#
#1
x=bin(8)
print(x)
y=oct(32)
print(y)
print(hex(32))

#2
x="welcome to python"
print(len(x))
print(x[0])
print(x[0:10])
print(x[0:15:2])

#3
x=pow(2,5)
print(x)

x=pow(2,5,7) #(7) IS MOD %
print(x)


y=round(2.67)
print(y)

y=round(2.67,1)
print(y)

#4
z=sorted([2,5,1,8,6])
print(z)

#=================================================================================#

#====================================List-Notes===================================#

"""
list.append(a) inserts a at the end of the list
• list.insert(index,a) insert a at certain index
• list.remove(a) remove first occurence of a
• del a[index] remove element at index of list a
• list.pop(a) remove element at index a and returns
it, by default a is last index
"""

a=(15,12,13,8)
a[0]=3
#>>> Error, tuple elements cannot be modified
a+=(19)
#>>> Error, a tuple cannot be concatenated with an integer

a+=(19,)
print(a)
#>>> (15,12,13,8,19)
b,c,d,e,f=a
print(b,c,d,e,f)
#>>> 15 12 13 8 19

a=(“Hello”,3,4)
print(a[0])
#>>> Hello
print(a[0][1])
#>>> e
#=================================================================================#

#====================================List-Notes===================================#

a={'A':1,'B':2,'C':3,'D':4}
print(a['A'])
#print(a[1])    #error
a['D']=6
print(a)
a['F']=9        #adds an key&value to the dictionary
print(a)
b=a.keys()
print(b)
c=a.values()
print(c)


fruits="cherry,banana,mango,peach"
a=fruits.split()
print(a[0])
#>>> cherry,banana,mango,peach

a=fruits.split(',')
print(a[0])
#>>> cherry

#=================================================================================#

#==============================Break&Continue Statments===========================#

for i in range(5):
    if i == 2:
        print("Skipping iteration 2.")
        continue
    print(i)

for i in range(5):
    if i == 2:
        print("Skipping iteration 2.")
        continue
    print(i)

#=================================================================================#

#=================================A Basic Calculator==============================#

num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))   
while True:
   opp=input("Enter the opperation you want(+,-,*,/,-1 to exit): ")
   if opp==-1:
       print("exiting the calculator,goodbye..!")
       break
   if opp=="+":
       result1=num1+num2
       print(f"The sum of the two nums is:{num1}+{num2}={result1}")
   elif opp=="-":
       result2=num1-num2
       print(f"The subtraction of the two nums is:{num1}-{num2}={result2}")
   elif opp=="*":
       result3=num1*num2
       print(f"The multiplication of the two nums is:{num1}*{num2}={result3}")
   elif opp=="/":
       if num2!=0:
         result4=num1/num2
         print(f"The division of the two nums is:{num1}/{num2}={result4}")
       else:
           print("cannot divide any number by zero!")
   else:
       print("invalid,please enter a correct opperation")
   num1=float(input("enter the first number:"))
   num2=float(input("enter the second number:"))

#=================================================================================#

#=============================Circle calculator project===========================#

radius = int(input("Enter the radius of a circle (in cm) (-1 to exit): "))
while True:
    if radius == -1:
        print("Exiting... Goodbye!")
        break

    print("1 - Calculate Diameter")
    print("2 - Calculate Area")
    print("3 - Calculate Perimeter")

    user_input = int(input("What do you want to calculate? : "))

    if user_input == 1:
        diameter = 2 * radius
        print(f"The diameter of the circle with the radius you entered is: {diameter}")
    elif user_input == 2:
        area = 3.14 * radius**2
        print(f"The area of the circle with the radius you entered is: {area}")
    elif user_input == 3:
        perimeter = 2 * 3.14 * radius
        print(f"The perimeter of the circle with the radius you entered is: {perimeter}")
    else:
        print("Invalid, please choose a choice between (1-3)!")
    radius = int(input("Enter the radius of a circle (in cm) (-1 to exit): "))

#=================================================================================#

#==========================min max application project(#error)====================#

print("Welcome to the min max calculator!")

while True:
    #(Taking input from the user)
    user_input = input("Enter values separated by spaces: ")

    #(Split the input string into a list of strings)
    input_list = user_input.split()
    if '-1' in input_list:
        print("exiting...goodbye!")
        break

    #(Convert the list of strings to a list of integers (or any other desired type))
    integer_list = [int(item) for item in input_list]

    #(Print the resulting list)
    print("List:", integer_list)
    print("\nMenu")
    print("1-Display minimum numbers of the list")
    print("2-Display maximum numbers of the list")
    
    userinput_2=int(input("Choose your choice (1-3)(-1 to exit): "))
    if userinput_2==1:
        print("List:", integer_list)
        print("The minimum number in your list is: ",min(input_list))
    elif userinput_2==2:
        print("List:", integer_list)
        print("The maximum number in your list is: ",max(input_list))

    else:
        print("invalid.please enter a number between (1-3)")
        print("-----------------------------------------------")

#=================================================================================#

#===============================factorial calculator==============================#

def factorial(n):
    if n==0:
        return 1
    if n<0:
        print("invalid.please enter a pstv integer.")
    if n>0:
        return n*factorial(n-1)
user_input=int(input("Enter a number to calculate its factorial: "))
while(user_input<0):
    print("invalid.please enter a pstv integer.")
    user_input=int(input("Enter a number to calculate its factorial: "))
result=factorial(user_input)
print(f"the factorial of {user_input} is {result}")
    
#=================================================================================#

#=================================Grades Calculator===============================#

print("Welcome to the Grade Calculator!")
failed_count=0
succeed_count=0
user_grade=float(input("Enter your grade and i will till u its letter(A-B-C...)(-1 to exit): "))
for i in range(0,11):

    if user_grade==-1:
        print("exiting...")
        break
    if user_grade>=90 and user_grade<=100:
        print("->your grade letter is A")
        succeed_count+=1
    elif user_grade>=80 and user_grade<=80.9:
        print("->your grade letter is B")
        succeed_count+=1
    elif user_grade>=70 and user_grade<=79.9:
        print("->your grade letter is C")
        succeed_count+=1
    elif user_grade>=60 and user_grade<=69.9:
        print("->your grade letter is D")
        succeed_count+=1
    else:
        print("->You Failed,your grade is F ")
        failed_count+=1
    print("------------------------------------------------------------------------------------")

    user_grade=float(input("Enter your grade and i will till u its letter(A-B-C...)(-1 to exit): "))
print(" _____________________")
print("|_______Summary_______|")
print(f"|Succeed Student:{succeed_count}    |")
print(f"|Falied Student:{failed_count}     |")
print("|_____________________|")

#=================================================================================#

#==================================Range Examples=================================#

#example 1:
n=int(input("Enter a number: "))
sum=0
for i in range(0,n+1):
    if i%2==0:
        sum=sum+i
print(f"{sum}")
#example 2:
n=int(input("enter a number: "))
sum=0
for i in range(0,n+1,2):
    sum+=i
print(f"{sum}")

#=================================================================================#

#===========================Descending order range ex=============================#

n=int(input("enter a number: "))
for i in range(n,0,-1):
    if i%2!=0:
        print(f"{i}")

#=================================================================================#
        
#==================================String size ex=================================#

un=input("Enter a string: ")
size=0
for letter in un:
    size+=1
print(f"The size of the string id: {size}")

#=================================================================================#

#===============================Cel to Fah converter==============================#

def ctofah(c):
    return (9/5)*c+32
print("Celsuis\tFahrenheight")
for i in range(0,101):
    result=ctofah(i)
    print(f"{i}\t{result:0.2f}")

#=================================================================================#

#==============================Multiplication Quiz ex=============================#
    
import random
def randm():
    a=random.randrange(0,10)
    b=random.randrange(0,10)
    return a,b
x,y=randm()
ui=int(input(f"(-1 to exit).What is {x}*{y}?: "))
while(ui!=-1):
    if ui==x*y:
        print("very good!")
        x,y=randm()
        ui=int(input(f"(-1 to exit).What is {x}*{y}?: "))
    elif ui!=x*y:
        print("no please try again!")
        ui=int(input(f"(-1 to exit).What is {x}*{y}?: "))
ui=int(input(f"(-1 to exit).What is {x}*{y}?: "))

#=================================================================================#

#===============================Even odd sum in list==============================#

a=[5,4,5,9,8,3,2]
sum_odd=0
sum_even=0
for i in a:
    if i%2==0:
        sum_even+=1
    elif i%1==0:
        sum_odd+=1
print(f"number of odd: {sum_odd}")
print(f"number of odd: {sum_even}")

#=================================================================================#

#===============================Rating freq Histogram=============================#

import random
print("Rating\tFrequency")
responses=[]
freq=[]
for i in range(0,40):
    responses+=[random.randrange(1,11)]

for i in range(0,11):
    freq+=[responses.count(i)]

print("Responses:",responses)
print("Frequency:",freq)

print("Rating\tFrequency\tHistogram")
for i in range(0,11):
    print("%6d\t%9d\tA"%(i,freq[i]),"*"*freq[i],sep="")

#=================================================================================#

#==================================List Histogram=================================#
    
list=[19,3,15,7,11]
print("Index\tValue\tBarGraph")
for i in range (0,5):
    print(f"{i}\t{list[i]}\t{'*'*list[i]}")

#=================================================================================#
    


import matplotlib.pyplot as plt

x = ['java', 'c++', 'php', 'js', 'c#']
popularity = [22.22, 17.7, 8.8, 8, 7.7]  # Remove the extra element in this line
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color='red')
plt.xlabel("langs")
plt.ylabel("popularity")
plt.title("absr shu \n" + "abse shu kmn")
plt.xticks(x_pos, x)
plt.show()