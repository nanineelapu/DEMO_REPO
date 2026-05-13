# # Create the folders Task1 

import os

# for i in range(1, 4):
#     os.makedirs(f"/opt/project/releases/v{i}", exist_ok=True)
#     print(f"Created v{i}")


# Task 2
# log file scanner

# os.makedirs("var/log/app")

# files = os.listdir("var/log/app")

# for file in files:
#     if file.endswith(".log") or file.endswith(".err"):
#         print(files)

# # Task 3 Validatior wheather the files are exist or not

# os.makedirs("opt/app")

# # For static
# # paths = ["/opt/app/current","/opt/app/releases","/etc/nginx/nginx.conf"]

# # For DYNAMIC
# path = input("Enter the path : ")

# if os.path.exists(path):
#     print("FOUND")
# else:
#     print("MISSING")

# # Task 4

# backup_files = "backup_"

# import os

# backup_dir = "backup"

# folders = os.listdir(backup_dir) 

# backup_folders = []

# # filter  folders
# for f in folders:
#     if f.startswith("backup_"):
#         backup_folders.append(f)

# # sort based on number (backup_1, backup_2...)
# backup_folders.sort(key=lambda x: int(x.split("_")[1]))

# # if more than 3 delete it.
# if len(backup_folders) > 3:
#     delete = backup_folders[:-3] 


#     for folder in delete:
#         os.rmdir(f"{backup_dir}/{folder}")
#         print(f"Deleted: {folder}")



# Another way of Task 4.


# path = "/backup"

# folder = sorted(os.listdir(path))

# # print(folder) 

# print(type(folder))
# while len(folder) > 3:
#     old = folder.pop(0)
#     os.rmdir(os.path.join())

# path ="D:\Backup"
# folder=sorted(os.listdir(path))
# # print(type(folder))
# # print(folder)
# while len(folder) >3:
#     old=folder.pop(0) #pop method used to remove top element from the list
#     os.rmdir(os.path.join(path,old)) #create full path = D:\Backup\backup_1
#     print(old,"deleted")
 
# path ="D:\Backup"
# folder=sorted(os.listdir(path))
# # print(type(folder))
# # print(folder)
# while len(folder) >3:
#     old=folder.pop(0) #pop method used to remove top element from the list
#     os.rmdir(os.path.join(path,old)) #create full path = D:\Backup\backup_1
#     print(old,"deleted")


# Learing about the sys module 

# import sys
# # print(sys.argv)

# from sys import argv

# print(f"the toatal numebr of command line arguments{len(sys.argv)}")
# # Listof command line arguments 
# print(f"list of cmd arguments{sys.argv}")
# print(f"the cmd arguments one by one " )
# use loop to get onne bye one in good foramt 
# for arg in sys.argv:
#     print(arg)

# print sum of all cmd line arguments 
# args = sys.argv[1:]
# sum = 0
# for x in args:
    # sum = sum + x
    # Convert to integer format 
#     sum = sum + int(x)
# print(sum)


# f1 = open('file1.txt')
# f2 = open("file2. txt")
# f3 = open('combined_output.txt', 'w')

# for x in f1:
#     f3.write(x)
# for x in f2:
#     f3.write(x)

# args = argv[1:]
# print(f"Name: {args}")
#  or for plus the numebrs of argumes like 

# print(argv[1] + argv[2])

# output will be 2030

# so to concantinate we use type cast 


# print(int(argv[1]) + int(argv[2]))

# print(argv[100])

# if i give the array index in betweeen the index 

# in terms of producation we use aws has to handlled through arguments 
# env = argv[0]
# if env == "prod":
#     print("Deploying the production")
# elif env == "dev":
#     print("Deploying to the development")

# if requiremnts are not matching or script is completed we can exit through sys modules
# import sys

# print("Pr...")
# print("Loa...")
# sys.exit()
# print("Dep..Suc..")

# disk = 100
# if disk > 90:
#     print("Disk Full")
#     sys.exit(1)
# else:
#     print("Disk is healthy")



# File operations 

# Which means reading data and wriring the data from the files 


# f= open("paper.txt",'r')

# print(f.read())
# f.close()

# to get the other file data we can use paths like 

# file = open(r'c\......', 'r')

# print(file.read())

# file.close

# By using Context Manager to open the file 

# with open(r'paper.txt', 'r') as file:
#     # for line in file:
#         # print(file.read(10))
#         print(file.readlines())
# with open(r'paper.txt','r') as file :
#     for line in file:
#         print(line)

# with open('DEVOPS.txt', 'w') as file:
#     file.write("New File creation using Write ")

# Write a program to make a qurstion paper

# with open("paper.txt",'r') as file:
#     for line in file:
#         if line.startswith("Answer") is True:
#             with open('Answers.txt', 'a') as appendFile:
#                 appendFile.write(line)

# Final call learn about the sys.append

# Sys.Executable 

# python is avialable in the file when the file is executable 

import sys
print(sys.executable)

data = [1,2,3]

print(sys.getsizeof(data))

# learn about other modules 


        


