import socket
import os

os.system("clear")

print('''\007


\033[0;34m██╗    ██╗██████╗ ███╗   ██╗   ██████╗    ██╗██████╗ 
\033[0;36m██║    ██║██╔══██╗████╗  ██║   ╚════██╗   ██║██╔══██╗
\033[0;34m██║ █╗ ██║██║  ██║██╔██╗ ██║    █████╔╝   ██║██████╔╝
\033[0;36m██║███╗██║██║  ██║██║╚██╗██║   ██╔═══╝    ██║██╔═══╝ 
\033[0;34m╚███╔███╔╝██████╔╝██║ ╚████║   ███████╗   ██║██║\033[0;31mv1.9
\033[0;36m ╚══╝╚══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚══════╝   ╚═╝╚═╝    
                                                       
\033[1;36m =============================================\033[1;m
\033[0;33m|\033[0;32m# Code By X-Dave                             \033[0;33m|
\033[0;33m|\033[0;32m  Contact On Whatsapp +94753704046           \033[0;33m|
\033[0;33m|\033[0;32m# Modified By Pinindu Tharushan              \033[0;33m|
\033[0;33m|\033[0;32m  Contact On Whatsapp +94702801713           \033[0;33m|
\033[1;36m =============================================\033[1;m
\033[1;33m|     Best Web Domain Name To IP Converter    |
\033[1;36m =============================================\033[00m''')

def en():
    print()
    print("\033[0;37m[1] සිංහල")
    print("[2] English")
    print("[3] Any Problem? Contact us")
    print("[4] Share This Tool")
    print("[5] Exit")
    print()
    print("\033[0;35mඔබගේ භාෂාව හෝ වෙනත් දෙයක් තෝරන්න: ")
    print("\033[0;35mSelect Your language Or Other: ")
    ya = input('''\033[0;37m[+]=====> ''')
    if ya == "1":
        sinhala();
    elif ya == "2":
        english();
    elif ya == "3":
        print('''https://wa.me/+94702801713''')
        print('''https://wa.me/+94753704046''')
    elif ya == "4":
        print('''https://github.com/Pinindu-Tharushan/WDN-2-IP''')
    elif ya == "5":
        print('''exit''')
    else:
        print('''\033[0;31mවැරදි ඇතුලත් කිරීමකි...!''')
        print('''\033[0;31minvalid number...!''')
        print()
        print('''\033[0;31mනැවත උත්සහ කරන්න...!''')
        print('''\033[0;31mTry Again...!''')
        print()
        en()

def english():
    print("\033[0;37m[1] https://")
    print("[2] http://")
    print("[3] ftp://")
    print("[4] tcp://")
    print("[5] ip://")
    print("[6] smtp://")
    print("[7] icmp://")
    print("[8] none")
    print()
    print("Select Your Web Protocol:")
    p = input()
    if p == "1":
        p1 = "https://"
    elif p == "2":
        p1 = "http://"
    elif p == "3":
        p1 = "ftp://"
    elif p == "4":
        p1 = "tcp://"
    elif p == "5":
        p1 = "ip://"
    elif p == "6":
        p1 = "smtp://"
    elif p == "7":
        p1 = "icmp://"
    elif p == "8":
        p1 = "none"
    else:
        p1 = "none"
    print("Your Web Protocol is " + p1)
    print()
    print("Enter Your Web Domain(eg:- github.com): ")
    host = str(input())
    print()
    print("Your Web IP Is:")
    print(socket.gethostbyname(host))
    print()
    print("Do You Want Get onther Web IP?(Y/N)")
    ans = input('''\033[0;37m[+]=====> ''')
    if ans == "Y" or "y":
        en()
    else:
        print()
        print("Thank You For Using This Tool")
        print("Exit")

def sinhala():
    print("\033[0;37m[1] https://")
    print("[2] http://")
    print("[3] ftp://")
    print("[4] tcp://")
    print("[5] ip://")
    print("[6] smtp://")
    print("[7] icmp://")
    print("[8] none")
    print()
    print("ඔබගේ වෙබ් අඩවියේ Protocol එක තෝරන්න:")
    p = input()
    if p == "1":
        p1 = "https://"
    elif p == "2":
        p1 = "http://"
    elif p == "3":
        p1 = "ftp://"
    elif p == "4":
        p1 = "tcp://"
    elif p == "5":
        p1 = "ip://"
    elif p == "6":
        p1 = "smtp://"
    elif p == "7":
        p1 = "icmp://"
    elif p == "8":
        p1 = "none"
    else:
        p1 = "none"
    print(p1 + "යනු ඔබගේ වෙබ් අඩවියේ Protocol එකයි")
    print()
    print("වෙබ් අඩවියේ වසම් නාමය ඇතුලත් කරන්න(උදා:- github.com): ")
    host = str(input())
    print()
    print("ඔබගේ වෙබ් අඩවියේ IP ලිපිනය වන්නේ:")
    print(socket.gethostbyname(host))
    print()
    print("තවත් වෙබ් අඩවියක IP ලිපින අවශ්‍යද?(Y/N)")
    ans = input('''\033[0;37m[+]=====> ''')
    if ans == "Y" or "y":
        en()
    else:
        print()
        print("මෙම මෙවලම භාවිත කල ඔබට ස්තුතියි.")
        print("Exit")

en()
