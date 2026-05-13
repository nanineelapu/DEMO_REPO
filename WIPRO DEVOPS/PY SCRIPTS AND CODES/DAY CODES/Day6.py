# import argparse
# import os
 
# FILE = "balance.txt"
# MIN_BALANCE = 500
 
 
# # Initialize file if not exists
# def init():
#     if not os.path.exists(FILE):
#         with open(FILE, "w") as f:
#             f.write("1000")   # default balance
 
 
# def get_balance():
#     with open(FILE, "r") as f:
#         return int(f.read())
 
 
# def update_balance(amount):
#     with open(FILE, "w") as f:
#         f.write(str(amount))
 
 
# # Deposit
# def deposit(amount):
#     balance = get_balance()
#     balance += amount
#     update_balance(balance)
#     print("Deposited:", amount)
#     print("Current Balance:", balance)
 
 
# # Withdraw
# def withdraw(amount):
#     balance = get_balance()
 
#     if balance - amount < MIN_BALANCE:
#         print("Insufficient funds! Minimum balance should be 500")
#     else:
#         balance -= amount
#         update_balance(balance)
#         print("Withdrawn:", amount)
#         print("Current Balance:", balance)
 
 
# # Check balance
# def check_balance():
#     balance = get_balance()
#     print("Current Balance:", balance)
 
 
# # Argument Parser
# def main():
#     init()
 
#     parser = argparse.ArgumentParser(description="Banking Application")
 
#     parser.add_argument("action", choices=["deposit", "withdraw", "balance"],
#                         help="Action to perform")
 
#     parser.add_argument("--amount", type=int,
#                         help="Amount for deposit/withdraw")
 
#     args = parser.parse_args()
 
#     if args.action == "deposit":
#         if args.amount:
#             deposit(args.amount)
#         else:
#             print("Please provide --amount")
 
#     elif args.action == "withdraw":
#         if args.amount:
#             withdraw(args.amount)
#         else:
#             print("Please provide --amount")
 
#     elif args.action == "balance":
#         check_balance()
# import argparse
# parser=argparse.ArgumentParser(description="Banking amount Analyser")
 
 
# # Flags
# parser.add_argument("--deposit",type=int,help="show deposit")
# parser.add_argument("--withdrawl",type=int,help="show withdrwl")
# parser.add_argument("--balanceenq",action="store_true",help="show balance Enq")
# parser.add_argument("--statement",action="store_true",help="shows recent transaction")
 
# balance = 1200
# min_balance = 500
 
# args = parser.parse_args()
 
# if args.deposit is not None:
#     if args.deposit > 0:
#         balance += args.deposit
#         print(f"Deposited : {args.deposit}" )
#         print(f"Real Money : {balance}")
#     else:
#         print("Amout not valid")
 
# if args.withdrawl:
#     if args.withdrawl > 0 and (balance - args.withdrawl >= min_balance):
#         balance -= args.withdrawl
#         print(f"Withdrwal : {args.withdrawl}")
#         print(f"Available Balance : {balance}")
#     else:
#         print("Amount {args.withdrawl} is not able to withdraw")
# if args.balanceenq or args.statement:
#     print(f"Current Balance : {balance}")


# Very very Important Exception handling
# a= 10
# b= 0
# div = ()
# print(a/b)
# print("End of the program")

# try:
#     num = a/b
# except:
#     print("A is not divisible by 0")


# try:
#     num = int(input("Enter the number: "))
#     print("Mobile number : ", num )
# except ValueError: #---------------Value error is used to irrelavent input is passing in the input console 
#     print("Invalid number")

# How mutiple errors can be handled 
# try:
#     x = int(input("Enter the number"))
#     divison = 10/x
#     print(divison)
# except ZeroDivisionError:
#     print("Divison by 0 is not possible")
# except ValueError:
#     print("Enter the value of integer only")

# super object for exception can be handled through Exception
# try:
#     x = int(input("Enter the number"))
#     divison = 10/x
#     print(divison)
# except Exception as exe:
#     print(exe)

# NOW FULL SYNTAX FOR EXCEPTION 
# try:
#     code()
# except error(1):
#     code()
# except error(2):
#     code()
# else:
#     code()  ELSE IS GONNA WORK WHEN THERE IS NO EXCEPTIONS ARE THERE
# or
# finally:
#     code() THIS WILL GONNA MAKE TO FINALIZE THE CODE AFTER ALL THE CODE EXECTURED EVEN THOUGH ITS NOT DEPENDING UPON THE CODE AND LOGIC JUST EXECUTES

# -----------------BUILT IN EXECPTIONS-----------------
# FIRST EXCEPTION - ZERO DIVISION ERROR 
# VALUE ERROR       - IF WE PASS INVLAID VALUE IN THE CODE OR INPUT
# TYPE ERROR        - WRONG DATA TYPE
# NAME ERROR       -  WHEN WE PASS Y INSTED OF X THERE WILL BE ERROR OF PASSING NAME 
# INDEX ERROR      - INVLAID INDEX LIST ERROR
# KEY ERROR        - MISSING THE DICTIONORY KEY 
# FILE NOT FOUND ERROR - FILE MISSING EXCEPTION 
# IMPORT ERROR       - MODULE MISSING KEY ERROR

# ---------------------USER DEFINED EXCEPTIONS--------------------
# RASING THE MANUAL EXCPETIONS OR USER DEFINED 

# age = -1 
# try:
#     if age < 0 :
#         print(ValueError)
# except :
#     pass

# class serverDownError(Exception):
#     pass
# raise serverDownError("production server is down")

# ------------------NESTED EXCEPTIONS------------------
# try:
#     try:
#         x = 10/0
#     except:
#         print("Inner error")
#     x = 10/15
# except:
#     print("Outer error")

# RESTART THE SERVER AUTOMATICALLY SO HOW IT CAN BE HANDLED BY THE EXCEPTIONS 

# import subprocess
# try:
#     print("Restarting the Nginix services ..... ")
#     subprocess.run(
#         ["sudo su" ,"restartcommand", "nginx"],
#         check=True
#     )
#     print("Nginix Server is restated sucesfully")
# except FileNotFoundError:
#     print("Sudo su command not found")
# except PermissionError:
#     print("Permission denied run with ADMINSTRATOR or SUDO SU")
# except subprocess.CalledProcessError:
#     print("Nginix server restart failed")
# except Exception as exe:
#     print("UNEXPECTED ERROR " , exe)
# finally:
#     print("Execution completed")


