#------------------ASYNC FUNTION-----------------------

# it is defined through  Async def deploy()

# PAuse current task until the result is ready Await()
# Loops the task
# Egninee that run tasks
# Asyncio.run(main())

# # TO RUNN MULTIPLE TASKS
# Await asyncio.gather(task1(), task2() ...)

# EXAMPLE FOR THE ASYNC PROCESSING 

# import asyncio
# import time

# def checkServer(server):
#     time.sleep()


# async def ......
#     url = ""
#     try:
#         async.............

# import asyncio

# hosts = ['google.com', 'github.com']
# async def ping(host):
#     process = await asyncio.create_subprocess_exec(
#         "ping" , "-n", "1" , host,
#         stdout = asyncio.subprocess.PIPE,
#         stderr = asyncio.subprocess.PIPE,
#     )
#     out , err = await process.communicate()
#     if process.returncode == 0:
#         print(f'{host} up')
#     else:
#         print(f'{host} down')

# async def main():
#     await asyncio.gather(*(ping(h) for h in hosts))
# asyncio.run(main())


# ----------------WHERE TO NOT USE ASYNC---------- 
# AVOID IF TASK IS TAKES CPU HEAVY
        # VIDEO ENCODING
        # HUGE COMPRESSIONS
        # MACHINE LEARNING TRAINING 
        # LARGE PARSING 
# LOG FAILS LIMITED CONCURRENT TASKS SYSTEM SECURITY   

# JUST NEED TO SPEAK ABOUT AI MY TRAINER ASKING  

# WHAT AI IS AND TEACHING MACHINE BOW TO BEHAVE LIKE 
# --- ITS A OUTPUT PRODUCT OF MACHINE LEARING  
# HOW THE AI IS GOING ON 
# ABOUT AUTOMATION
# COMAPNY why companies uses this 
# EXAMPLE OF GOOGLE 
# WEE USED THE AI LIKE GOOGLE CHAT GPT OTHRT 
# THATS NOT FULL AI - THAT IS LLM IS THE FRIST ONE AI IS 
# --DEVLEOPINING DAY BY DAY IS NOT AI IS 
# DEVLOPING 
# NEED TO AFRID 


# NOW LEARING THE AI MODULES
# AI MACHINE LEARNING PERFORMING TAKS FOR THE REQUIRED HUMAN INTELLIGENCE 

# CHATBOTS ARE THE EXAMPLE 
# FRUAD DETECTION
# FACE REGONIZATION
# ML[MACHINE LEARNING]
# MACHINE LEARNS THE PATTEREN FROM THE DATA 

# INPUT - AS CPU USAGE , MEMORY USAGE PREDICCCT SERVERS FAILURES 
# ---DEEP LEARNNG ----------

# SPEECH REGONIXATION 
# VISION SYSTEMS
# LARGE LANGUAGE MODELS GENREATE THE NEXT PROBABLE TOKENS LIKE CHATGPT AND GEMINI AND CLUADE ETC...
# HOW TO RESRART NGNIX SERVER THSI IS AKED OF RRHT LLM THEN THE OUTPUT IS LIKELY PREDICTS NEXT WORD USE SYSTEM CTL AND RESTART NGINIX 
# SO FINALLY IT PREDICT BASED ON THE HUMAN AND MACHINE LEARINGN TRAINED 
# TOKENIZATION MEANS THE WORDS ARE SPLIT INTO CHUNKS 
# TEXT CONVERTS INTO VECTORS CALLED EMBEDDING FOR SEARCH

# HOW DEVOPS USE OF LLMS :
# - AUTO GENRATE THE TERAFORM 
# -KUBERNATES TROUBLE SHOOTING 
# - INCIDENT RCA ROOT CAUSE ANLAYSIS
# - INTEGTE THE DEVOPS WITH AI DOESNT DONE THAT.
# LOG SUMMERIXATION
# SECURUTY CHECKS CI/CD PIPLEINE

# WHAT IS AI AGENT HOW TO DEVLOP IN PYHTON IS THE TOMMORROW TOPIC 

# WHAT IS NLP?
# SCENTIMENT ANALYSISI , TRNASLATION , CHATBOTS 

# import requests 

# apiKey = "e579c2878232072d4e9edf16fce5e7f9"
# city = input("Enter the city: ")
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric'

# response = requests.get(url)
# data = response.json()

# print('Weather Data for {city}:')
# print(f"Temperature: {data['main']['temp']}*C")
# # print("Temp :", {data ['main'] ['temp']}, "*C")
# print(f"Weather :  {data['weather'][0]['description']}")
# print(f"Humidity : {data['main']['humidity']}")
# print(f"Wind Speed : {data ['wind']['speed'],'m/s'}")


# filename = f"{city}_weatherReport.txt"
# with open(filename, 'a') as file:
#     for key, value in data.items():
#         file.write(f"Weather Data for {city}:\n")
#         file.write(f"Temperature: {data['main']['temp']}*C\n")
#         file.write(f"Weather :  {data['weather'][0]['description']} \n")
#         file.write(f"Humidity : {data['main']['humidity']} \n")
#         file.write(f"Wind Speed : {data ['wind']['speed'],'m/s'} \n")
#     print(f"Weather data is saved to {filename}")


# create a .env file form that i need to get the env variables of my api key form that i 
# need to load the data from the .env
import os
import requests
from dotenv import load_dotenv

load_dotenv(".env.local")

apiKey = os.getenv("WEATHER_API_KEY")
city = input("Enter the city: ")
url = os.getenv("WEATHER_URL").format(city=city, api_key=apiKey)
response = requests.get(url)

data = response.json()

print(f"Weather Data for {city}:")
print(f"Temperature: {data['main']['temp']}*C")
print(f"Weather :  {data['weather'][0]['description']}")
print(f"Humidity : {data['main']['humidity']}")
print(f"Wind Speed : {data ['wind']['speed'],'m/s'}")


