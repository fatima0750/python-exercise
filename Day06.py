#practice 1: make dictionary
'''
student={"name":"Fatima","age":20,"major":"computer science"}
print(student)
#practice 2:change value
student.update({"age":21})
print(student) 
#practice 3: add keys
student.update({"gpa":18.84,"phone":9916513493})
print(student)
#practice 4
if "phone" in student:
    print(f"the phone number is {student["phone"]} .")
else:
    print("phone not found")
'''
#=======================================
#practice 5: student information manager

mystudents={}
def add_student():
    name=input("Enter student name: ")
    age=int(input("Enter student age:"))
    grade=float(input("Enter student grade:"))
    mystudents[name]={"age":age,"grade":grade}

def show_all_students():
    print(mystudents)

def search_student():
    name=input("Enter student name: ")
    if name in mystudents:
        print(mystudents[name])
    else:
        print("Student not found!")

def delete_student():
    name=input('Enter student name that you want delete: ')
    del mystudents[name]

while True:
    choise=int(input("Menu:\n1.Add student\n2.Show all students\n3.Serach student\n4.Delete student\n5.Exit\nchoise: "))
    if choise==1:
        add_student()
    elif choise==2:
        show_all_students()
    elif choise==3:
        search_student()
    elif choise==4:
        delete_student()
    elif choise==5:
        break
    else:
        print("try again")
