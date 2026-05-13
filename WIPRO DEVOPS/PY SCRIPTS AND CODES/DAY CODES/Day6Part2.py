# ----------------OOPS in PYTHON----------------------

# IT IS A WAY OOF DEISGNING APPLICATION USING OBJECTS THAT CONSITS OF DATA WHICH IS NOTING BUT A BLUE PRINT

# DATA WE REQURED ATTRIBUTES/ VARIABLES AND METHODS AND PROPERTIES AND BEHVAIOUR

# A SERVER CAN HAVE IN DEVOPS HOW THE OOPS ARE 
# -SERVER NAME 
# IP ADDRESSES 
# OS TYPE 
# METHODS LIKE START() STOP() OTHER STUFF


# USAGE OF OOPS 
# 1. REUSABLITY   
# 2. MAINTAINBILITY [IF ANY OF THE CHNAGE WE WANT WE CAN CHANGE ON TIME INSTED OF MANY TIMES]
# 3. SCALABILITY [EASY TO EXPAND THE SYSTEM IN THE CODE]
# 4. SECURITY [SENSITVE DATA CAN BE PROTECTED]
# 5. READABILITY [EASLIY TO UNDERSTAND AND ORGANIZE THE CODE ]

# IN THE BANKING SOFTWARE WE USE THIS OOPS 
# ECOMMERCE APPLICATION 
# HOSPTAIL SYSTEMS APPS DEVLOPMETS CLOUD PLATFORMS DEVOPS AUTOMATION NETWERKING TOOLS MONOTIRING SYSTEMS  

# class Employee:
#     company = "Solutions"
#     def __init__(self):
#         pass
# emp = Employee()
# print(id(emp))
# print(emp.company)






# ---------------ABOUT CONSTRUCTOR---------- 
# Most commonly used constructur is __init (self) : with in the class
# Constructor can return null value if doesnt have any parameter of return 

# class Student:
#     def __init__(self):
#         print("Construtor EXE....")
#         self.name = "murlai"
#         self.rollno = 101
#         self.mark = 90

#     def details(self):
#         print("Hello, I am", self.name)
#         print("My roll number is", self.rollno)
#         print("My marks are", self.mark)


# # Create object
# s1 = Student()
# s2 = Student()


# Call method
# s1.details()
# WHEN CREATION OF OBJECT IS CREATED EACH TIME THE CONSTRUCTR WILL CALL AUTOMATICALLY

# print(id(s1))
# print(id(s2)) # SO THE PUROSE OF THE CONSTRUCTUOR IS MEMORY AND ALLOCATION 

# STUDENT()
#     WE ARE CREATING THE OBJECT THE PVM WILL CREATE OBJ AND MEMORY ALLOCATION 
#     PVM WILL EXE __init__() TO DECLARE AND INITALIZE VARABLES OF THE OBJECT (INSTANCE VARIABLE)

# WE GONNA INTAILIZE THE OBJECT THORUGH ASSIGNING THE REFERANCE VARIABLLE 
# THOUGH THE REFRANCE VARIBLE WE CAN ACCES PROPERTIES AND OTHER METHODS

# -----ABOUT SELF KEYWORD--------EXAMPLE

# class Student:
#     def __init__(self):
#         self.name = "Nani"
#         self.rollno = "Roll no "


# class Server:
#     def __init__(self, hostname, ip, os):
#         self.hostname = hostname
#         self.ip = ip
#         self.os = os

#     def start(self):
#         print(self.hostname, "started")

#     def stop(self):
#         print(self.hostname, "stopped")

#     def restart(self):
#         print(self.hostname, "restarting...")
#         self.stop()
#         self.start()

# s1 = Server("Server1", "192.168.1.1", "Linux")

# s1.start()
# s1.stop()
# s1.restart()

# LEARN ALL THE OOPS CONCEPT IN THE PYHTON 

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary # HERE THE SALARY IS PRIVATE SO TO HIDE THE DATA IN THE CLASS AND THE FLOW OF CONTROL USE ENCAP
#         pass
#     def showSalary(self):
#         print(self.__salary)
#     def increaseSalary(self, amount):
#         self.__salary += amount
#         print("Salary Updated")
        

# e1  = Employee("Nani", 28000)
# e1.showSalary()
# e1.increaseSalary(2000)
# e1.showSalary()

# --------------------ANOTHER EXAMPLE OF ENCAPSULATION---------------

# -------------------------POLYMORPHSISM-------------------------------
# ONE METHOD USES MUTLTIPLE WAYS

# class Upi:
#     def pay(self):
#         print("Pay using UPI")
# class Card:
#     def pay(self):
#         print("Pay using CARD")   
# class netBanking:
#     def pay(self):
#         print("Pay using NET BANKING")

# method = [Upi(), Card(), netBanking()]
# for m in method:
#     m.pay()

# ________DEPLOY APPLICATION IN THE AWS AND GCP AND ASURE__________


class AWS:
    def deploy(self):
        print("Deployed into AWS")
class GCP:
    def deploy(self):
        print("Deployed into GCP")   
class AZURE:
    def deploy(self):
        print("Deployed into AZURE")

providers = [AWS(), GCP(), AZURE()]
AWS.deploy(providers)

