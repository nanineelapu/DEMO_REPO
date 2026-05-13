

# Working on the salary i think

# so here 

# ctc, detuctions = map.float(input("Enter ctc, detuctions").split())

# see the split fucntion and also we are passsing the two values in the input. So here 
# the input will variables are works as a list 
# print("Net salary  = " , ctc - detuctions)

# import os 

# path = "www\name\mails.txt"
# # here the files has to split to one var and the file name to another variable
# directory, file = os.path.split(path)
# print(f"directory{directory} \n files: {file}")

# # About seperator
# print("a", "b","c")

# print("www", "var", "version", sep="/")

# End 
# used to put the new line we use end key 

# Want  create the salary slip 

# import sys

# # name = input("enter the EMP name : ")
# name = sys.argv[0]
# # baseSalary = float(input("Enter the Basic Salary"))
# base_salary = sys.argv[1]

# # allownces = float(input("Enter the allowneces : "))
# allowences = sys.argv[2]

# # detuctions = float(input("Enter the Deductions: "))
# detuctions = sys.argv[3]


# gross_salary =  float(base_salary) + float(allowences)

# net_salary = gross_salary -  float(detuctions)


# print(f"Base salary :  {base_salary}")




# # Items question 

# print("Scan the Item") #gets the item name 
# item = print(input("Enter the item name : "))

# quantity = print(input("Enter the quantity number : "))


# print("Systems assigns the price : ")
# price = print(float(input("Enter the price of the above item: ")))

# final_price = price * quantity

# print(f"Enter the name of the item  {item}" )

# print(f"Enter the quantity : {quantity}")

# print(f"Enter the pric e: {price}")

# print(f"Final Price is {final_price}")


import sys

# print(sys.version)

# username = input("enter the username ")

# if username == "":
#     print("no username is entered ")
#     sys.exit()
# else:
#     print("Welcome ",  username)

# Using the custom module built in differnt folder 
# using sys.append() path 

# data = [10,20,30]
# servername = "webserver1server2server3server4"

# print(f"Data{sys.getsizeof(data)}, bytes")
# print(f"Servername {sys.getsizeof(servername)}, bytes")

# if sys.getsizeof(servername) > 80:
#     print("Servername size is large ")
# else:
#     print("Expected servername size ")

import os
# print(os.listdir())
# print(os.getcwd())
# os.walk

# files = os.walk(os.getcwd())

# for cur_dir, list_dir, list_files in files:
#     print(cur_dir)
#     print(list_dir)
#     print(list_files)

# os.remove(path)...
# os.rmdir() removes the empty directory

# C:\Users\nania\OneDrive\Desktop\WIPRO DEVOPS\PY SCRIPTS AND CODES\DAY CODES\
# path = "C:\Users\nania\OneDrive\Desktop\WIPRO DEVOPS\PY SCRIPTS AND CODES\DAY CODES"

# os.remove(input(f"Enter the path:" ) )

# # About shutile Module 
# import shutil

# shutil.rmtree("C:\Users\nania\OneDrive\Desktop\WIPRO DEVOPS\PY SCRIPTS AND CODES\DAY CODES\file.err")

# # print(os.name)

# f = open("\3dfile.py", 'r')
# print(f.close())
#  ----------------------------with dynamic -------------
# with open("file.err") as file:
#     for line in file:
#         print(line, end='')

# with open("file.err", "w") as f:
#     a = 10
#     b = 20
#     sum = a+b
#     f.write(f"\n {str(sum)} \n")

# Now how can we get data of file operatios from another file 




# print("Scan the Item") #gets the item name 
# item = input("Enter the item name : ")
# print("Enter the Quantity")
# quantity = input("Enter the quantity number : ")
# print("Systems assigns the price : ")
# price = float(input("Enter the price of the above item: "))

# final_price = price * quantity

# with open("bills.txt" , "w") as bill:

#     # print(f"Enter the name of the item  {item}" )
#     bill.write(f"Item name : {item} \n")
#     # print(f"Enter the quantity : {quantity}")
#     bill.write(f"Enter the quantity: {str(quantity)} \n")
#     # print(f"Enter the pric e: {price}")
#     bill.write(f"Enter the price : {str(price)} \n")
#     # print(f"Final Price is {final_price}")
#     bill.write(f"Final bill :  {str(final_price)}")


# The read method and the stdin
# import sys

# text = sys.stdin.read()
# print(text.upper())
# sys.stdout.write()

#Std error

# sys.stderr.write("Kubernates load errror") #used to error messages can be asigned in thelogs.

# Main dif betweeen input print and 
    # Print is only one tool that give direcct stream
    # Sys module is have better control compared to the print 
    # We can sepraete the errros with seprate outputs 
    # Integrate with pipelines
    # Machine readable automation output
    # ____________________________They are ________________________
        #    (Standard input ) stdin 
        #    (Standard output )  stdout
        #    (Standard error) stderr


# history is used to list the history of the commands
# How git is connected to the conatiners of the AWS Dockers etc...
# Learn this frist



# Sub process module______________________
# Need to learn that i mean the sub process modules and the Sys module 

# Learning in the middle sub process .pipe (it is used to capture stdout stderr stdin)

# import subprocess



# process = subprocess.Popen(
#     ["python" , "--version "],
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text= True
# )
# out, err = process.communicate()
# print(out)

# subprocess.run(["python" , "3dfile.py"])

# _________________________________LOGGING MODULE________________________
# What it is reccodrding the messgaes about a program exectuion while running it 
# insetd of printing statement we use logging statement modules becuase of the standrad way to record error messgaes and 
# diagnoise issues and , monotor systems (Why we use is for professional monitoring insted of print statements)

# _________________FEATURES_______________
# 1) Loging gives Sevierity(About priority levels) levels
# 2)Time stramps 
# 3) filtering the data 
# 4) Record strucutre 
# 5) File output 
# 6) Production monitoring 
# 7) Error Tracking 

# # Warning logging like low memory disk 
# logging.warning("Low disk space")

# LOGGING LEVELS 
# level -debugging purpose - Detailed info sevierity - 10

# level - info purppose - general info severity - 20
# level- warining purpose - something unexpeccted severity - 30
# level - error purpose - failure happen seveirty - 40
# level - criitical purpose - when the program may crash severity - 50

# Lets know the diff between the logging and print .......................
# import logging

# logging.basicConfig(filename='namecheck.log', level=logging.DEBUG)
# def namecheck(name):
#     if len(name) < 2:
#         logging.debug("Checking for name length")
#         return "Invalid name"
#     elif name.isspace():
#         logging.debug("Checking for name has spaces")
#         return  "Invalid"
#     elif name.isalpha():
#         logging.debug("Checking for name is an alphabets or not")
#         return  "Invalid"   
#     elif name.replace(' ','').isalpha():
#         logging.debug("Checking for name has full name and also haev alphabets")
#         return  "Invalid"
#     else:
#         logging.debug("Failed all cases")
#         return "Invalid name"
# logging.debug(namecheck("Twinkle"))

# logging.basicConfig(filename='log_level_1.log',filemode='w', level=logging.DEBUG) #format= cana be used to store the time stamps 
# # we get the warrning and the error and critical messages here becuse we can see those messages in tht file name we have given to store the messages
# logging.debug("This is debug messages")
# logging.info("This is logging info message through info module")
# logging.warning("Warning KEEW KEEW")
# logging.error("Error ohh GOTCHAA")
# logging.critical("KEWW KEWW BOOM")

# https://docs.python.org/3/library/logging.html#logrecord-attributes This is for logging FORMATS

# Analyse the Logging module and no need to save we use disable()
# About the warrnings and anlayse we checks through login module 

import logging
import datetime

filename = "stu_details.txt" # Need to create dynamically file ?
logging.basicConfig(filename="students.log", level=logging.INFO)

def add_student():
    roll = input("Roll : ")
    name = input("Name : ")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, 'a') as file:
        file.write(roll + "," + name +  "\n")

    print(" Student Added")
    logging.info(" Student Roll Number : " + roll)
    # logging.info("Student Name : " + name)

def showStudents():
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())


def searchStudent():
    roll = input("Enter the roll ")

    found = False


    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(roll + ","):
                print("Found" + line)
                logging.info("Found " + line.strip())
                found = True
                return
            else: 
                logging.warning("Invalid roll")

def deleteStudent():
    roll = input("Enter the roll : ")

    with open(filename, "r") as f:
            lines = f.readlines()

    with open(filename, "w") as f:
            found = False
            for line in lines:
                data = line.strip().split(",")
                if data[0] != roll:
                    f.write(line)
                else:
                    found = True
    if found:
         print("Student Deleted")
         logging.info("Student Deleted")
    else:
         logging.warning("Enter valid roll")

def updateStudent():
    roll = input("Enter roll: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    found = False

    with open(filename, "w") as f:
        for line in lines:
            if line.startswith(roll + ","):
                name = input("New name: ")

                import datetime
                now = datetime.datetime.now()

                f.write(f"{roll},{name},{now}\n")
                found = True
            else:
                f.write(line)

    if found:
        print("Updated")
        logging.info("Updated: " + roll)
    else:
        print("Invalid roll")
        logging.warning("Invalid roll")
        

while True:
    print("\n1.Add 2.Show 3.Search 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        showStudents()
    elif ch == "3":
        searchStudent()
    elif ch == "4":
        deleteStudent()
    elif ch == "6":
        break
    else:
        print("Invalid choice")






















