import socket
import os

os.system("clear")

print('''\007


\033[0;34m██╗    ██╗██████╗ ███╗   ██╗   ██████╗    ██╗██████╗ 
\033[0;36m██║    ██║██╔══██╗████╗  ██║   ╚════██╗   ██║██╔══██╗
\033[0;34m██║ █╗ ██║██║  ██║██╔██╗ ██║    █████╔╝   ██║██████╔╝
\033[0;36m██║███╗██║██║  ██║██║╚██╗██║   ██╔═══╝    ██║██╔═══╝ 
\033[0;34m╚███╔███╔╝██████╔╝██║ ╚████║   ███████╗   ██║██║\033[0;31mv1.6    
\033[0;36m ╚══╝╚══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚══════╝   ╚═╝╚═╝    
                                                       
\033[1;36m =============================================\033[1;m
\033[0;32m|# Code By X-Dave                             |
\033[0;32m|  Contact On Whatsapp +94753704046           |
\033[0;32m|# Modified By Pinindu Tharushan              |
\033[0;32m|  Contact On Whatsapp +94702801713           |
\033[1;36m =============================================\033[1;m
\033[1;33m|     Best Web Domain Name To IP Converter    |
\033[1;36m =============================================\033[00m''')

def en():
    print("[1] සිංහල")
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
    
def English():
    print()
    print("Enter Your Web Domain: ")
    host = input((str))
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
    print()
    print("වෙබ් අඩවියේ වසම් නාමය ඇතුලත් කරන්න : ")
    host = input((str))
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
