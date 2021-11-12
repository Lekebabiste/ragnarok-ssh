#! /usr/bin/python3


import os
from bannerprint.bannerprint import print_banner
import bruteforce_script
try:
    import paramiko
except:
    print ("Paramiko is not installed please do 'pip3 install paramiko'")
    quit()
try:
    import colorama
except:
    print("Colorama is not installed please do 'pip3 install colorama'")
    quit()
Port = 22
Host = "localhost"
Wordlist_path = "wordlist.txt"
Username = "root"
while True:
    os.system('clear')
    print_banner()
    print("DISLAIMER :\nDon't use this tool on system that not belong to you .Hacking is illegal.I will not be responsible of your acte.\n")
    try:
        choice = int(input("1 - Set the HOST name \n2 - Set the port \n3 - Set the Username \n4 - Set the directory of the wordlist\n5 - Start bruteforce attack\n6 - Show set info\n7 - Quit the programm \n\n(Please choose a number beetwen 1 and 7) > "))
    except ValueError:
        choice = input("Please enter a number > ")
    except KeyboardInterrupt:
        print("\nGoodbye ")
        quit()
    if choice == 1 :
        os.system('clear')
        print("*****************************************************************************************************************\n")
        Host = input("Set the HOST name (Exemple : hostame.net, 122.555.6,) > ")
    elif choice == 2 :
        os.system('clear')
        print("*****************************************************************************************************************\n")
        while True:
            try:
                Port = int(input("Set the PORT (Exemple : 22 , 45452 , 2222) > "))
            except ValueError:
                print("Please enter a integer (exemple 22 or 54)")
            except KeyboardInterrupt :
                os.system("clear")
                print("\nGoodbye")
                quit()
            else:
                break
    elif choice == 3 :
        os.system('clear')
        print("*****************************************************************************************************************\n")
        Username = input("Set the username (Exemple : root, admin) > ")
    elif choice == 4:
        os.system('clear')
        print("*****************************************************************************************************************\n")
        Wordlist_path = input("Set the wordlist path (Exemple : /home/lekebabiste/Documents/worldlist.txt) > ")
    elif choice == 5 :
        bruteforce_script.bruteforce(Wordlist_path,Host,Port,Username)
        input("Enter any key to continue")
    elif choice == 6:
        os.system('clear')
        print("Host : ",Host,"\nPort : ",Port,"\nWordlist path : ",Wordlist_path,"\nUsername : ",Username)
        input("Enter anything to quit ... > ")
    elif choice == 7:
        print("Goodbye")
        quit()
    else:
        print("Please choose a number beetwen 1 and 7") #69 lines ? NICE