import os 
shutdown = input("Do YOU WISH TO SHUTDOWN YOUR COMPUTER? (yes / no): ") 
  
if shutdown == 'no': 
    exit() 
else: 
    os.system("shutdown /s /t 1") 