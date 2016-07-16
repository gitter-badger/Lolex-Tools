import os, time
check = int (0)

print ("Module JTToolsMethods is running, using modules os and time.")
def flicker():
 count = 0
 while count != 2147483648:
        count = count +1
        os.system("color 4a")
        os.system("color 3b")
def logo():
    os.system ("color f9")
    print ("00000000000000000000000000000000000000000   00000000000000000000000")
    print ("00000000000000000000000000000000000000000   00000000000000000000000")
    print ("                                                    000000000")
    print ("           00000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("            00000000000000000                       000000000")
    print ("            0000000000000000                        000000000")
    print ("           00000000000000000                        000000000")
    print ("          00000000000000000                         000000000")
    print ("         0000000000000000                           000000000")
    print ("        000000000000000                             000000000")
    print ("      0000000000000                                 000000000")
    print ("    000000000000                                    000000000")
def exitnow():
    if check != 1:
        closing = 5
    while closing> 0.015:
        print("Closing in", round (closing, +3),"seconds.")
        time.sleep(0.017)
        closing = closing -0.015
