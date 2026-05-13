# TYPES OF INHERITANCE
# GETTING ALL THE PROPERTIES TO CHILD CLASS FROM PARENT CLASS 

# EXAMPLE IF WE HAVE MULTIPLE SERVERS THEN THE ACTUAL WORING OF THE INHERITANCE WE USE 

# SINGLE INHERITANCE ------ ONLY ONE PARENT AND ONE CHILD 

# class Server: #PARENT CLASS
#     var = "Parent class"
#     def start(self):
#         print("Server Started")
#     def stop(self):
#         print("Stop Server")
# class linuxServer(Server):
#     def patchUpdate(self):
#         print("Linux patch is installed")
#         print(self.var)

# l1 = linuxServer()
# l1.start()
# l1.patchUpdate()

# -------------MULTI LEVEL INHERITANCE ------------------
# METHOD RESOLUTION ORDER - Python searches for methods starting from the current class and move upwards thorugh inhheritance chain 

# class parentServer:
#     var = "PARENT SERVER"
#     def startServer(self):
#         print("Server is Strating")
# class childServer(parentServer): #CHILD CLASS
#     def child(self):        
#         print("This is the child server class")
# class childServer2(childServer): #DERIVED CLASS 
#     def needTo(self):
#         print("Need to update")
# ch2 = childServer2()
# ch2.child()

# ECOMMERCE CUSTOMER EXAMPLE

# class Customers:
#     def normalCustomers(self):
#         print("User is the Amazon Customer")

# class User:
#     def __init__(self, username):
#           self.username = username
#     def login(self):
#          print(self.username, "Login sucessfully")
# class Customer(User):
#     def __init__(self, username, customerId):
#          super().__init__(username)
#          self.customerId = customerId
#     def buyProducts(self):
#          print(f"Customer id : {self.customerId} is purchased the product")
# class primeCustomer(Customer):
#     def __init__(self, username, customerId, discount):
#          super().__init__(username, customerId)
#          self.discount = discount
#     def primeBenfits(self):
#         print(f"Prime customer gets the:  {self.discount} % discount")

# customerObj = primeCustomer("nanineelapu", 9094321, 40)
# customerObj.login()
# customerObj.primeBenfits()
# customerObj.buyProducts()
     
# ==============MULTIPLE INHERITANCE================

# in devops ther is loginmodule security module are there we nee do paste in one module so ther is 
# multiple inheritacne are there this is the example 

# class Logger: #PARENT CLASS 1
#     def loginModule(self, message):
#         print(f"Logs : {message}")
# class Security: #PARENT CLASS 2
#     def auth(self, username):
#         print(f"User Authenticated: {username}")
# class finalDeploy(Logger,Security):
#     def deployModule(self, application):
#         print(f"Application {application} is deployed with no [Errors]")

# dep = finalDeploy()
# dep.loginModule("Login successful")
# dep.auth()
# dep.deployModule()

#ONE CHILD CLASS GETTING PROPERTIES AND METHODS FROM DIFFERENT PARENT CLASSES

# HYBRID INHERITANCE 

# GETTING MULTIPLE PARENT CLASSES AND CHILD CLASSES WHICH IS HAVEING DIFFERNT TYEPS OF INHERITANCE ARE THERE THEN IT CALLED THE HYBRID IINHERITANCE 

# class developerTools: #BASE CLASS 1
#     def git(self):
#         print("Using VCS")
#     def docker(self):
#         print("Using docker for containerization")
# class cloudPlatform: #BASE CLASS 2
#     def aws(self):
#         print("Deploying resources in the AWS")
#     def kubernaties(self):
#         print("Managing containers with the Kubernaties")
# class devopsEngineer(developerTools, cloudPlatform):
#     def ciCd(self):
#         print("Running the CI/CD piplines using Jenkins")
    
# class seniorDevopsEngineer(devopsEngineer): #MULTI LEVEL INHERITANCE
#     def monitoring(self):
#         print("Monitoring the systems using the prometheus & grafana") #TOOLS FOR MONITOTING IN THE DEVOPS

# sde =  seniorDevopsEngineer()
# sde.git()
# sde.docker()
# sde.aws()
# sde.kubernaties()
# sde.ciCd()
# sde.monitoring()


#------------------ VARIABLES AND TYPES--------- 
# static variables
# class variables

# class Employee:
#     company = "wipro"
#     def __init__(self,name):
#         self.name = name 

# e = Employee("Nani")
# print(e.company)
# print(e.name)
# #ONE VARIABLE SHARE BY ALL OBJECTS
# Employee.company = "COGNIZANT"
# print(Employee.company) #CAN ACCESS  STATIC VARIABLES BY USING CLASS NAME 

#---------STATIC METHODS------------
# A STATIC METHOD IS DECLARED INSIDE THE CLASS THAT IS NOT USESE ANY OTHER METHODS OF CLASSES
# A method inside a class that doesnt use object self or any other object method 
# DECORATOR
# @staticmethod

# class Caliculator:
#     @staticmethod
#     def add(a, b):
#         return a+b
# # c = Caliculator()
# # print(c.add(12,22))
# print(Caliculator.add(10,30)) #NO NEED OF METHOD

# class Utils:
#     @staticmethod
#     def validateIp(ip):
#         print(ip)
# Utils.validateIp("......")

# THESE ARE USED IN THE DATE FORMATING 
# LOG FORMATING THIS STATIC METHODS WERE USED AS A DEVOPS ENGINEER
# FILE EXTENSION 
# PORT VALIDATION
# PASSWORD FORMAT AND STRENGTHS

# CLASS METHODS- METHOD THAT WORKS WITH CLASS VARIABLES AND CLASS DATA 
# DECOTATOR 
# @classmethod
# INSTED OF [SELF] WE USE ...[CLS]- USED TO MODIF A STATIC VARIABLE ALSO EXMPLE IN THE BOTOOMM

# class Student:
#     college = "giet"
#     @classmethod
#     def showCollege(cls):
#         print(cls.college)

# Student.showCollege()
# # to change 
# Student.showCollege("KIET")
# print(Student.college)

# ABSTRACT CLASSES LEARN THSEE 

# SMART HOSPATAIL MANAGMENT SUSTEM EXAMPLE
# A hospital wants software to manage staff responsibilities in levels.
# Structure:
# Person → basic details of every human
# Doctor → a person who treats patients
# SpecialistDoctor → senior doctor with specialization

# class User:
#     def __init__(self, username):
#           self.username = username
#     def login(self):
#          print(self.username, "Login sucessfully")
# class Customer(User):
#     def __init__(self, username, customerId):
#          super().__init__(username)
#          self.customerId = customerId
#     def buyProducts(self):
#          print(f"Customer id : {self.customerId} is purchased the product")
# class primeCustomer(Customer):
#     def __init__(self, username, customerId, discount):
#          super().__init__(username, customerId)
#          self.discount = discount
#     def primeBenfits(self):
#         print(f"Prime customer gets the:  {self.discount} % discount")

# customerObj = primeCustomer("nanineelapu", 9094321, 40)
# customerObj.login()
# customerObj.primeBenfits()
# customerObj.buyProducts()

# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name 
#         self.age = age
#         self.gender = gender
#     def getPersonDetails(self):
#         return f"Name: {self.name}, Age: {self.age}, Gender : {self.gender}"
#     def showPersonDetails(self):
#         print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

# class Doctor(Person):
#     def __init__(self, name, age, gender, doctorId, department):
#         super().__init__(name, age, gender)
#         self.doctorId = doctorId
#         self.department = department
#     def diagnoisePatient(self):
#         print("Diagnosing patient......")
#     def prescribeMedicine(self):
#         print("Prescribing medicine...")

# class SpecialistDoctor(Doctor):
#     def __init__(self, name, age, gender, doctorId, department, specialization, experienceYears):
#         super().__init__(name, age, gender, doctorId, department)
#         self.specialization = specialization
#         self.experienceYears = experienceYears
#     def performSurgery(self):
#         print("Performing surgery......")
#     def emergencyCase(self):
#         print("Handling emergency case.....")

# specialist = SpecialistDoctor("Dr. Meera",45, "Female", "D102", "Cardiology", "Heart Surgeon","18 Years")
# specialist.showPersonDetails()
# print(f"Doctor ID: {specialist.doctorId}")
# print(f"Department: {specialist.department}")
# print(f"Specialization: {specialist.specialization}")
# print(f"Experience: {specialist.experienceYears}")

# Doctor.diagnoisePatient(specialist)
# Doctor.prescribeMedicine(specialist)
# specialist.performSurgery()
# specialist.emergencyCase()

# filename = "doctorDetails.txt"

# with open(filename, "w") as file:
#     file.write(specialist.getPersonDetails() + "\n")
#     file.write(f"Doctor ID: {specialist.doctorId}\n")
#     file.write(f"Department: {specialist.department}\n")
#     file.write(f"Specialization: {specialist.specialization}\n")
#     file.write(f"Experience: {specialist.experienceYears}\n")

# ---------------Smart E-Commerce Delivery Management System-------------------

# class productManagement:
#     def __init__(self, productId, productName,):
#         self.productId = productId
#         self.productName = productName
#     def addProduct(self):
#         print(f"Product Added Successfully with product ID : {self.productId} and product NAME : {self.productName}")
#     def updateStock(self):
#         print(f"Stock Updated with product ID : {self.productId}")

# class paymentManagement:
#     def processPayment(self):
#         print("Payment Processed Successfully")
#     def refundPayment(self):
#         print("Payment Refunded Successfully")

# class DeliveryExecutive(productManagement, paymentManagement):
#     def __init__(self, productId, productName, executiveName, area):
#         super().__init__(productId, productName)
#         self.executiveName = executiveName
#         self.area = area
#     def assignOrder(self):
#         print(f"Order Assgined with exectiveName : {self.executiveName}")
#     def deliverOrder(self):
#         print(f"Order Delivered to the AREA : {self.area} ")

# class seniorDeliveryManager(DeliveryExecutive):
#     def __init__(self, productId, productName, executiveName, area, managerName):
#         super().__init__(productId, productName, executiveName, area)
#         self.managerName = managerName
#     def trackAllDeliveries(self):
#         print(f"Tracking All Deliveries by Manager : {self.managerName}")
#     def generateReport(self):
#         print(f"{self.managerName} has Generated Monthly Report")

#     def getAllDetails(self):
#         return f"PRODCUT ID : {self.productId}, PRODUCT NAME : {self.productName}, EXECUTIVE NAME : {self.executiveName}, AREA : {self.area}, MANAGER NAME : {self.managerName}"



# SDM = seniorDeliveryManager(1102,"Wild Stone Perfume", "Rajesh" , "Rajahmundry" , "Nani Reddy")
# SDM.addProduct()
# SDM.updateStock()
# SDM.processPayment()
# # SDM.refundPayment()
# SDM.assignOrder()
# SDM.deliverOrder()
# SDM.trackAllDeliveries()
# SDM.generateReport()

# fileName = "ecommerceDeliveryDetails.txt"

# with open(fileName, 'a') as file:
#     file.write(SDM.getAllDetails() + "\n")



# -------------VVV IMPORTANT--------------------

# ABOUT API

import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Error : {response.status_code}")

# HOW THE POST METHOD WORKS I MEAN POST REQUEST
# TO SUBMIT THE DATA JSON DATA 


# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title" :"TestAPI",
#     "body" : "checking data API",
#     "userId" : 909
# }

# response = requests.post(url, data)

# if response.status_code == 201:
#     print(f"success, new post created with {response.json()["id"]}")
# else:
#     print(f'ERROR ')

# PUT METHOD 

# url = "https://jsonplaceholder.typicode.com/posts/3"

# data = {
#     "title" :"TestAPI 2",
#     "body" : "updating data API",
#     "userId" : 901
# }

#MAKE A PUT METHOD REQUEST 

# response = requests.put(url,data)

# if response.status_code == 200:
#     print(f"success, POST UPDATED {response.json()["id"]}")
# else:
#     print(f'ERROR {response.status_code} ')

# # DELETE THE DATA DELETE REQUEST 

# response = requests.delete(url)

# if response.status_code == 200:
#     print("Sucess data deleted")
# else:
#     print(f"Error {response.status_code}")

apiKey = "e579c2878232072d4e9edf16fce5e7f9"
city = "Hyderabad"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric'

response = requests.get(url)
data = response.json()
print('Weather Data for Hyderabad:')
print(f"Temperature: {data['main']['temp']}*C")
print("Temp :", {data ['main'] ['temp']}, "*C")

# print(f"Weather: {data['weather'][0]['description']}")
# print(f"Humidity: {data['main']['humidity']}%")
# print(f"temparature : Data['main'] ['temp'],c *")
# print(f"weather : data['weather'][0]['description']")
# print(f"Humidity, data['main']['humidity']")
# print(f"Wind Speed , data['wind']['speed','m/s']")







 

