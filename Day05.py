#practice 1: Lists 
'''
mylist=["banana","apple","cherry","orange","watermelon"]
for item in mylist:
   print(item)
#practice 2:add item 
fruit1=input("please enter your fruit: ")
mylist.append(fruit1)
print(mylist)
#practice 3:remove duplicated item
''
fruit2=input("please enter your fruit: ")
if fruite2 in mylist:
   mylist.remove(fruit2)
   print(mylist)
else:
   print("fruit not found!")
'''
#==================================== 
#practice 4:find bigest item
'''
numbers=[15,3,28,10,7]
numbers.sort()
print(f'The bigest number is {numbers[-1]}.')
practice 5: print even numbers
newlist=[]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        newlist.append(numbers[i])
print(newlist)
'''
#=====================================
#practice 5: average of grades
'''
grades=[12,14,20,19,20,12,18,17,4,19.5,9.5]
sum=0
for i in range(len(grades)):
    sum+=grades[i]
avg=sum/len(grades)
print(f"The average of the grades are {avg}.")
'''
#======================================
#practice 7
'''
mylist=[]
for i in range(1,11):
    number=int(input(f"Please enter your {i}th number: "))
    mylist.append(number)
#print biggest & smallest
mylist.sort()
print(f"The biggest number in ypur numbers is {mylist[-1]}.")
print(f"The smallest number in your numbers is {mylist[0]}.")
#print average of numbers
sum=0
for i in range(len(mylist)):
    sum+=mylist[i]
avg=float(sum/len(mylist))
print(f"The average of your numbers is {avg}")
#print the odd and even numbers
oddcounter=0
evencounter=0
for item in mylist:
    if item%2==0:
        evencounter+=1
    else:
        oddcounter+=1
print(f"The odd numbers in your numbers is {evencounter}.")
print(f"The even numbers in your numbers is {evencounter}.")
'''
#=================================
#practice 8:small project for Grades
'''
mygrade=[]
def Add_graade():
        grade=float(input(f"Enter your grade: "))
        mygrade.append(grade)
        print("grade added.")

def Show_grades():
    if mygrade==[]:
        return "Your list is empty!"    
    else:
        for i in range(len(mygrade)):
            print(f"grade is {mygrade}.")
        
def Average():
    if mygrade==[]:
        return "Your list is empty!"    
    else:
        sum=0
        for i in range(len(mygrade)):
            sum+=mygrade[i]
        avg=sum/len(mygrade)
        print(f"The average of grades are {avg}")

def Highest_grade():
    if mygrade==[]:
        return "Your list is empty!"    
    else:
        mygrade.sort()
        print(f"The highest grade is {mygrade[-1]}.") 
    
while True:
    choice=int(input("The menu:\n1.Add grade\n2.Show grades\n3.Average\n4.Highest grade\n5.Exit\nchoise:"))
    if choice==1:
        print(Add_graade())
    elif choice==2:
        print(Show_grades())
    elif choice==3:
        print(Average())
    elif choice==4:
        print(Highest_grade())
    elif choice==5:
        print("Goodbye!")
        break
'''
