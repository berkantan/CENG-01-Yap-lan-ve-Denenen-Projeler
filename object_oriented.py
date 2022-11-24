class Doctor():
    def __init__(self,name,age,job,salary,hospital):
        self.name=name
        self.age=age
        self.job=job
        self.salary=salary
        self.hospital=hospital
        
    def set_name(self,value):
        self.name=value
       
    def set_age(self,value):
        self.age=value
        
    def set_job(self,value):
        self.job=value
        
    def set_salary(self,value):
        self.salary=value
       

    def set_hospital(self,value):
        self.hospital=value

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_job(self):
        return self.job
    def get_salary(self):
        return self.salary
    def get_hospital(self):
        return self.hospital
    
    def __str__(self):
        return f"name:{self.name},age:{self.age},job:{self.job},salary{self.salary},hospital{self.hospital}"


name=input( "please enter your name")
if name.isalpha()== True:
    print(name)
else:
    print("print a correct value")
age=int(input( "please enter your age"))
if age>=24:
    print(age)
elif age<24:
    print("Persons under 24 years of age cannot be doctors.")
elif age<0:
    print(  "age must be positive")
else:
    ("please enter a valid value")
job=input("plase enter your job")
if job== "doctor" or job==   "doktor":
    print(job)
else:
    print("only for doctor")
salary=int(input("plase enter your salary"))
if salary<0:
    if salary<5250:
        print("Salary cannot be below the minimum wage.")
    print("salary must not be positive")
else:
    print(salary)

def submit():
    print("hospital is:")
    print(listbox.get(listbox.curselection()))
from tkinter import *

hospital = Tk()

listbox = Listbox(hospital,
bg="#f7ffde",
font=("Constantia",50),
width = 12)
listbox.pack()
listbox.insert(1,"Etlik Şehir Hastenesi")
listbox.insert(2,"Hacettepe Üniversitesi Eğitim ve Araştırma Hastanesi")
listbox.insert(3,"Ankara Üniversitesi Eğitim ve Araştırma Hastanesi")
listbox.insert(4,"Dışkapı Yıldırım Beyazıt Hastanesi")
listbox.insert(5,"Bilkent Şehir Hastenesi")
listbox.config(height=listbox.size())



submit_Button = Button(hospital,text="submit",command=submit)
submit_Button.pack()

hospital.mainloop()



doctor=Doctor(name,age,job,salary,hospital)
print(doctor.get_name())
print(doctor.get_age())
print(doctor.get_job())
print(doctor.get_salary())
print(doctor.get_hospital())



