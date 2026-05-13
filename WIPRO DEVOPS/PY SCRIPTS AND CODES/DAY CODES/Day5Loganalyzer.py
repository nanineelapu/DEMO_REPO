# About the math module 
# math.something()

# import math
# print(math.sqrt(20))

# import random
# print(random.randint(20,30))


# info = 0
# error = 0
# warning = 0
# critical = 0

# with open("DAY CODES/file.log",'r') as file:
#     for line in file:
#         if "INFO" in line:
#             info+= 1
#         elif "ERROR" in line:
#             error+=1
#         elif "WARNING" in line:
#             warning+=1
#         elif "CRITICAL" in line:
#             critical+=1
# print(f"INFO: {info}\n ERROR:{error}\n WARNING : {warning} CRITICAL : {critical}")
            
# import subprocess

# def run_cmd(cmd):
#     result = subprocess.run(
#         cmd,
#         shell=True,
#         capture_output=True,
#         text=True,
#         encoding="utf-8"
#     )
#     return result.stdout.strip()

# Command Line arguments

# Devops  CICD Pipelines and CRON JOBS SERVER

# Argparse are the second one to use in command line arguments Which means we need to pass the arguments in the command line
# Manual parsing Sys.argv() | Argparse automaatic parsing No need to asign manually
#              No Help Texts   Auto help using (-h)
#              No validation   Auto validation  
#              Not Scalabe     Wide Range of Scalability (Perfect for big applications)

import argparse

# parse = argparse.ArgumentParser(description="Basic Example")
# parse.add_argument("Name" , help="Enter the name ")
# parse.add_argument("Number" , type=int, help="Enter your moblie number")
# args = parse.parse_args()
# print("Name" , args.Name)
# print("Mobile" , args.Number)

#File analyser using the Argparse 

# parser = argparse.ArgumentParser(description="File Reading anlayser")
# parser.add_argument("filename" , help="Please enter the file name - TO ANALYSE")

# # Before that you have to learn about the optional flags 
# parser.add_argument("--lines" , action="store_true", help="show lines count")
# parser.add_argument("--words" , action="store_true", help="show words count")
# parser.add_argument("--char" , action="store_true", help="show char count")
# parser.add_argument("--all" , action="store_true" , help="Run all the arguments") #to pass all the args in the parser optional flags

# args = parser.parse_args()
# with open(args.filename , 'r') as file:
#     data = file.read()
#     total_lines = data.count("\n") + 1
#     total_words = len(data.split()) + 1
#     total_chars = len(data)
# if args.all:
#     print(f"\n Complete analysis report")
#     print("-" * 40)
#     print("Lines :" , total_lines)
#     print("Words :" , total_words)
#     print("Char :" , total_chars)
# else:
#     if args.lines:
#         print("Lines : " , total_lines)
#     if args.words:
#         print("Words :" ,  total_words)
#     if args.char:
#         print("Char: " , total_chars)
#     if not(args.lines or args.words or args.char):
#         parser.print_help()

# ------------------------------------USe of the Date and Time Module --------------------------

# Server Logs
# Monitoring Alerts
# BAckup automation
# Time IST Managament Time zone managment
# CI/CD Pipelines
# Job scheduling

from datetime import date, datetime, timedelta
import datetime as dt
# now = datetime.now()
# print(now)

# today = date.today()
# print(today)

# now = datetime.now()
# print(now.hour)

# start = datetime(2026)
# end = datetime(2026 )
# dif = end - start
# print(dif)

# now = datetime.now()
# after_5Days = now + timedelta(days=5)
# print(after_5Days)

# import time
# print("Starting")
# time.sleep(15) #holds the execution time
# print("Nani Reddy")

# import time 
# print(time.time())

# # converted_timestamp used in linux 
# time_now = time.time()
# print(datetime.fromtimestamp(time_now))


# # Calculate server downtime

# from datetime import datetime

# # Server up time
# server_up = datetime(2026, 4, 20, 10, 0, 0)   # 10:00 AM

# # Server down time
# server_down = datetime(2026, 4, 20, 12, 30, 0)  # 12:30 PM

# # Calculate downtime
# downtime = server_down - server_up

# # Print result
# print("Server was down for:", downtime)

# By , Create a banking application deposit , withdrawl , balance ENQ and ohter there will be min balance for the deposit some amut threr will be 1000 will the balance 
# snd min balance withdral 600 and there has to be statemtn the current balcne statemnet has to be execute , and agian wihtdrwal 900 then the amout is grather then balance so there will 
# not allow soexecute the steatement by amount not able to to eithdrawl

import argparse
# parser=argparse.ArgumentParser(description="File analizer")
# parser.add_argument("filename",help="please put file name to analyze ")
# #optional flags
# parser.add_argument("--lines",action="store_true",help="show line count") #short ---first character ,, long means full argument
# parser.add_argument("--words",action="store_true",help="show words count")
# parser.add_argument("--chars",action="store_true",help="show character count")
# parser.add_argument("--cam",action="store_true",help="show character count")
# parser.add_argument("--all",action="store_true",help="shows full report")
 
# args=parser.parse_args()
 
# with open(args.filename,"r") as file:
#     data=file.read()
#     total_line=data.count("\n")+1
#     total_words=len(data.split())
#     total_chars=len(data)
# if args.all:
#     print(f"\n complete analysis report")
#     print("-" * 40)
#     print("Lines:",total_line)
#     print("Words",total_words)
#     print("Characters:",total_chars)
# else:
#     if args.lines:
#          print("Lines:",total_line)
#     if args.words:
#         print("Words",total_words)
#     if args.chars:
#         print("Characters:",total_chars)
#     if args.cam:
#         print("camera")
#     if not(args.lines or args.words or args.chars):
#         parser.print_help()
        

import argparse
parser=argparse.ArgumentParser(description="Banking amount Analyser")


# Flags
parser.add_argument("--deposit",type=int,help="show deposit")
parser.add_argument("--withdrawl",type=int,help="show withdrwl")
parser.add_argument("--balanceenq",action="store_true",help="show balance Enq")
parser.add_argument("--statement",action="store_true",help="shows recent transaction")

balance = 1200
min_balance = 500

args = parser.parse_args()

if args.deposit is not None:
    if args.deposit > 0:
        balance += args.deposit
        print(f"Deposited : {args.deposit}" )
        print(f"Real Money : {balance}")
    else:
        print("Amout not valid") 

if args.withdrawl:
    if args.withdrawl > 0 and (balance - args.withdrawl >= min_balance):
        balance -= args.withdrawl
        print(f"Withdrwal : {args.withdrawl}")
        print(f"Available Balance : {balance}")
    else:
        print("Amount {args.withdrawl} is not able to withdraw")
if args.balanceenq or args.statement:
    print(f"Current Balance : {balance}")








    




