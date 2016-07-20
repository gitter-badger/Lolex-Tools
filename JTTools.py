import time, os, subprocess,sys
sys.path.insert(0,"\\")
import JTToolsMethods,JTToolsOptions
JTToolsMethods.logo()
local =time.asctime( time.localtime(time.time()) )
with open("JT Tools Log File.txt", "a") as f: f.write(local)
with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools Initialized:version 7.0.0.1232.20.7.16\n")
print ("JT Tools script version 7.0.0 Beta")
from JTToolsOptions import Options
print ("Please wait two seconds...")
time.sleep (2)
vanish = int(0)
try:
 line = 17
 repeat = int(input("Please enter 1 to confirm you are not a robot."))
 if repeat != 1:
  local =time.asctime( time.localtime(time.time()) )
  with open ("JT Tools Log File.txt","a") as f: f.write (local)
  with open ("JT Tools Log File.txt","a") as f: f.write ("    JT Tools: User has proved that they either cannot read or are a robot.\n")
  JTToolsMethods.exitnow()
 if repeat == 1:
     local = time.asctime(time.localtime(time.time()))
     with open ("JT Tools Log File.txt","a") as f: f.write(local)
     with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools: User has proved they can read and aren't a robot.\n")  
 while repeat == int(1):
  if JTToolsOptions.Options.useusername == True:
       usernameenter = input("Please enter your username in brackets and speech marks.")
       while str(usernameenter) != JTToolsOptions.Options.username1 and  str(usernameenter) != JTToolsOptions.Options.username2 or str(usernameenter) == False:
           print ("Sorry: you inputted an invalid username.")
           usernameenter = input("Please enter your username.")
           if usernameenter == JTToolsOptions.Options.username1:
            username = JTToolsOptions.Options.username1
            local = time.asctime(time.localtime(time.time()))
            with open ("JT Tools Log File.txt","a") as f: f.write(local)
            with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools: User logged in with username:")
            with open ("JT Tools Log File.txt","a") as f: f.write(username,"\n")
       if usernameenter == JTToolsOptions.Options.username2:
        username = JTToolsOptions.Options.username2
        local =time.asctime( time.localtime(time.time()) )
        with open ("JT Tools Log File.txt","a") as f: f.write (local)
        with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools: User logged in with username:")
        with open ("JT Tools Log File.txt","a") as f: f.write(username,"\n")
       
  if JTToolsOptions.Options.pin == True:
    vanish = 0
    vanishprint = JTToolsOptions.Options.vanishprint 
    codeenter = int(input("Please enter the current NPIN."))
    while codeenter != JTToolsOptions.Options.code:
         codeenter = int(input("Please enter the current NPIN."))
         local =time.asctime( time.localtime(time.time()) )
         with open("JT Tools Log File.txt", "a") as f: f.write(local)
         with open ("JT Tools Log File.txt","a") as f: f.write("   JT Tools :Incorrect PIN entered.\n")
    if codeenter == JTToolsOptions.Options.code:
          local =time.asctime( time.localtime(time.time()) )
          with open("JT Tools Log File.txt", "a") as f: f.write(local)
          with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Correct PIN entered.\n")
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

  if JTToolsOptions.Options.menu == True:
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
           elif modewanted == 2:
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
           elif modewanted == 3:
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
           elif modewanted == 4:
               subprocess.call("JTTools.py", shell = True)
  elif groupmode == 2:
      print("Here is a list of modes available:")
      print ("1 = Call CMD")
      print ("2 = Call Documents")
      print ("3 = Call Task Manager")
      print ("4 = Call Python Shell")
      modewanted = int(input("Please enter the number of the mode you wish to enter."))
      if modewanted == 1:
          subprocess.call("cmd.exe")
      if modewanted == 2:
          subprocess.call("explorer.exe")
      if modewanted == 3:
          subprocess.call("taskmgr.exe")
      if modewanted == 4:
          subprocess.call("python.exe")
  elif groupmode == 3:
      print("Here is a list of modes available:")
      print ("1 = Colour Flicker")
      modewanted = int(input("Please enter the number of the mode you want to enter."))
      if modewanted == 1:
          JTToolsMethods.flicker()
except():
    pass
#except(NameError,ValueError,SyntaxError,ImportError,WindowsError):
   # print ("Dammit! Something went wrong!")
   # time.sleep(5)
