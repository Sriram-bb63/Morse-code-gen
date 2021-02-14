#Importing Beep() from winsound
from winsound import Beep

#Import sleep() from time
from time import sleep

#Morse func
def morse(msg):
    
    #Defining freq and duration
    f=2250      #Frequncy
    d1=250      #Short beep
    d2=600      #Long beep
    d3=0        #End gap bw letters

    #Converting to lower case
    msg=msg.lower()

    #Assigning values in dictionary
    dic={
        "a":[d3,d1,d2],
        "b":[d3,d2,d1,d1,d1],
        "c":[d3,d2,d1,d2,d1],
        "d":[d3,d2,d1,d1],
        "e":[d3,d1],
        "f":[d3,d1,d1,d2,d1],
        "g":[d3,d2,d2,d1],
        "h":[d3,d1,d1,d1,d1],
        "i":[d3,d1,d1],
        "j":[d3,d1,d2,d2,d2],
        "k":[d3,d2,d1,d2],
        "l":[d3,d1,d2,d1,d1],
        "m":[d3,d2,d2],
        "n":[d3,d2,d1],
        "o":[d3,d2,d2,d2],
        "p":[d3,d1,d2,d2,d1],
        "q":[d3,d2,d2,d1,d2],
        "r":[d3,d1,d2,d1],
        "s":[d3,d1,d1,d1],
        "t":[d3,d2],
        "u":[d3,d1,d1,d2],
        "v":[d3,d1,d1,d1,d2],
        "w":[d3,d1,d2,d2],
        "x":[d3,d2,d1,d1,d2],
        "y":[d3,d2,d1,d2,d2],
        "z":[d3,d2,d2,d1,d1],
        "1":[d3,d1,d2,d2,d2,d2],
        "2":[d3,d1,d1,d2,d2,d2],
        "3":[d3,d1,d1,d1,d2,d2],
        "4":[d3,d1,d1,d1,d1,d2],
        "5":[d3,d1,d1,d1,d1,d1],
        "6":[d3,d2,d1,d1,d1,d1],
        "7":[d3,d2,d2,d1,d1,d1],
        "8":[d3,d2,d2,d2,d1,d1],
        "9":[d3,d2,d2,d2,d2,d1],
        "0":[d3,d2,d2,d2,d2,d2],
        ".":[d3,d1,d2,d1,d2,d1,d2],
        ",":[d3,d2,d2,d1,d1,d2,d2],
        "?":[d3,d1,d1,d2,d2,d1,d1],
        "'":[d3,d1,d2,d2,d2,d2,d1],
        "!":[d3,d2,d1,d2,d1,d2,d2],
        "/":[d3,d2,d1,d1,d2,d1],
        "(":[d3,d2,d1,d2,d2,d1],
        ")":[d3,d2,d1,d2,d2,d1,d2],
        "&":[d3,d1,d2,d1,d1,d1],
        ":":[d3,d2,d2,d2,d1,d1,d1],
        ";":[d3,d2,d1,d2,d1,d2,d1],
        "=":[d3,d2,d1,d1,d1,d2],
        "+":[d3,d1,d2,d1,d2,d1],
        "-":[d3,d2,d1,d1,d1,d1,d2],
        "_":[d3,d1,d1,d2,d2,d1,d2],
        "\"":[d3,d1,d2,d1,d1,d2,d1],
        "@":[d3,d1,d2,d2,d1,d2,d1]}

    #Takes every character one by one
    for i in range(len(msg)):
        print(msg[i])#Just to check, will not be a part of the final version
        #Five sec gap for space bw words
        if msg[i]==" ":
            sleep(5)
        else:
            #Get the list containing morse char for the any given alphabet
            lst=dic[msg[i]]
            for j in range(len(lst)):
                #If the list element is not d3, play sound
                if lst[j]!=0:
                    Beep(f,lst[j])
                else:
                #If it is d3, give 3 sec gap
                    sleep(3)
      
#Main()
msg=input("Enter your message:\n")
morse(msg)
