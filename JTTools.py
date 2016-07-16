import time, os, subprocess,sys
sys.path.insert(0,"\\")
import JTToolsMethods,JTToolsOptions
JTToolsMethods.logo()

local =time.asctime( time.localtime(time.time()) )
with open("JT Tools Log File.txt", "a") as f: f.write(local)
with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools Initialized:version 7.0.0.28.06.16.121937\n")
print ("This script is copyrighted by Jensen Taylor 2014 - 2016(C). JT Tools script version 7.0.0 Beta Re-Written for Python 2.7 instead of 3.4 due to a bug in python 3.4.1.\n")
import sys
sys.path.insert(0,"\\")
import JTToolsOptions
from JTToolsOptions import Options

print ("Please wait two seconds...")
time.sleep (2)
vanish = int(0)
try:
 repeat = int(input("Please enter 1 to confirm you are not a robot."))
 if repeat != 1:
  
  JTToolsMethods.exitnow()

  vanishabc = JTToolsOptions.Options.vanishprint

 while repeat == int(1):

  if JTToolsOptions.Options.useusername == True:
       usernameenter = input("Please enter your username.")
       while usernameenter != JTToolsOptions.Options.username1 and  usernameenter != JTToolsOptions.Options.username2 or usernameenter == False:
           print ("Sorry: you inputted an invalid username.")
           usernameenter = input("Please enter your username.")

  if JTToolsOptions.Options.pin == True:

    vanish = 0
    vanishprint = JTToolsOptions.Options.vanishprint 
    codeenter = int(input("Please enter the current NPIN."))
    while codeenter != JTToolsOptions.Options.code:
         codeenter = int(input("Please enter the current NPIN."))
         local =time.asctime( time.localtime(time.time()) )
         with open("JT Tools Log File.txt", "a") as f: f.write(local)
         with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Incorrect PIN entered.\n")
    if codeenter == JTToolsOptions.Options.code:
        if JTToolsOptions.Options.idle == True:
           pass
        if JTToolsOptions.Options.idle == False:
           
         while vanish != vanishprint:
             print ("")
             vanish = vanish +1
         if vanish == vanishprint:
             pass
  elif JTToolsOptions.Options.pin == False:
          pass
  
      
  
  local =time.asctime( time.localtime(time.time()) )
  with open("JT Tools Log File.txt", "a") as f: f.write(local)
  with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Correct PIN entered.\n")
  if JTToolsOptions.menu == True:
   print ("Here is a list of mode groups available:")
   print ("1 = Power Menu Related Options:Restart, Logoff (2 methods available), Hibernate, Shutdown (2 methods available), Lock Workstation")
   print ("2 = Call Programs: CMD, Documents, Python Shell, Task Manager, Auto-Clicker, Notepad, Restart This Script")
   print ("3 = Miscellaneous Options")

  groupmode = int(input("Please enter the number of the group mode you wish to enter."))
  if groupmode == 1:

           local =time.asctime( time.localtime(time.time()) )
           with open("JT Tools Log File.txt", "a") as f: f.write(local)
           with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Mode Group 1 (Power Menu) entered.\n")
           print ("Here is a list of options available in this mode group:")
           print ("1 = Restart")
           print ("2 = Logoff")
           print ("3 = Hibernate")
           modewanted = int(input("Please enter the number of the mode that you want."))
           if modewanted == 1:
                 local =time.asctime( time.localtime(time.time()) )
                 with open("JT Tools Log File.txt", "a") as f: f.write(local)
                 with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Restart (mode 1.1) entered.\n")
                 restart = int(input("Please enter 1 to confirm restart."))
                 if restart == 1:
                  waittime =int(input("How long, in minutes, do you wish to wait?"))
                  time.sleep (waittime*60)
                  local =time.asctime( time.localtime(time.time()) )
                  with open("JT Tools Log File.txt", "a") as f: f.write(local)
                  with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Performing Restart Operation.\n")

                  os.system ("shutdown -r -f")

                  os.system ("shutdown -l -f")
           if modewanted == 2:

            local =time.asctime( time.localtime(time.time()) )
            with open("JT Tools Log File.txt", "a") as f: f.write(local)
            with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Logoff (mode 1.2) entered.\n")
            logoff = int(input("Please enter 1 or 0 to confirm logoff."))
            if logoff == 1:
             waittime =int(input("How long, in minutes, do you wish to wait?"))
             time.sleep (waittime*60)
             local =time.asctime( time.localtime(time.time()) )

             with open("JT Tools Log File.txt", "a") as f: f.write(local)
             with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Performing Logoff Operation.\n")
             os.system ("shutdown -l -f")
           if modewanted == 3:
            local =time.asctime( time.localtime(time.time()) )

            with open("JT Tools Log File.txt", "a") as f: f.write(local)
            with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Hibernate(mode 1.3) entered.\n")
            hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
            if hibernate == 1:
 
             time.sleep (waittime*60)
             local =time.asctime( time.localtime(time.time()) )
             with open("JT Tools Log File.txt", "a") as f: f.write(local)
             with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Performing Hibernate Operation.\n")
             os.system ("shutdown -h -f")
           if modewanted == 4:
               subprocess.call("JTTools.py", shell = True)
except():
    pass
