print('''\007
\033[0;34m           __       __  _______   __    __       ______      ______  _______  
\033[0;34m          |  \  _  |  \|       \ |  \  |  \     /      \    |      \|       \ 
\033[0;34m| \033[0;35m$$ \033[0;34m/ \ | \033[0;35m$$\033[0;34m| \033[0;35m$$$$$$$\033[0;34m\| \033[0;35m$$\033[0;34m\ | \033[0;35m$$    \033[0;34m|  \033[0;35m$$$$$$\033[0;34m\    \\033[0;35m$$$$$$\033[0;34m| \033[0;35m$$$$$$$\033[0;34m\
\033[0;34m| \033[0;35m$$\033[0;34m/  \033[0;35m$\033[0;34m\| \033[0;35m$$\033[0;34m| \033[0;35m$$  \033[0;34m| \033[0;35m$$\033[0;34m| \033[0;35m$$$\033[0;34m\| \033[0;35m$$     \033[0;34m\\033[0;35m$$\033[0;34m__| \033[0;35m$$     \033[0;34m| \033[0;35m$$  \033[0;34m| \033[0;35m$$\033[0;34m__/ \033[0;35m$$
\033[0;34m| \033[0;35m$$  $$$\033[0;34m\ \033[0;35m$$\033[0;34m| \033[0;35m$$  \033[0;34m| \033[0;35m$$\033[0;34m| \033[0;35m$$$$\033[0;34m\ \033[0;35m$$     \033[0;34m/      \033[0;35m$$     \033[0;34m| \033[0;35m$$  \033[0;34m| \033[0;35m$$    $$
\033[0;34m| \033[0;35m$$ $$\033[0;34m\\033[0;35m$$\033[0;34m\\033[0;35m$$\033[0;34m| \033[0;35m$$  \033[0;34m| \033[0;35m$$\033[0;34m| \033[0;35m$$\033[0;34m\\033[0;35m$$ $$    \033[0;34m|  \033[0;35m$$$$$$      \033[0;34m|\033[0;35m $$  \033[0;34m| \033[0;35m$$$$$$$ 
\033[0;34m| \033[0;35m$$$$  \033[0;34m\\033[0;35m$$$$\033[0;34m| \033[0;35m$$\033[0;34m__/ \033[0;35m$$\033[0;34m| \033[0;35m$$ \033[0;34m\\033[0;35m$$$$    \033[0;34m| \033[0;35m$$\033[0;34m_____     _| \033[0;35m$$\033[0;34m_ | \033[0;35m$$      
\033[0;34m| \033[0;35m$$$    \033[0;34m\\033[0;35m$$$\033[0;34m| \033[0;35m$$    $$\033[0;34m| \033[0;35m$$  \033[0;34m\\033[0;35m$$$    \033[0;34m| \033[0;35m$$     \033[0;34m\   \033[0;34m|   \033[0;35m$$ \033[0;34m\| \033[0;35m$$      
\033[0;34m \\033[0;35m$$      \033[0;34m\\033[0;35m$$ \033[0;34m\\033[0;35m$$$$$$$  \033[0;34m\\033[0;35m$$   \033[0;34m\\033[0;35m$$     \033[0;34m\\033[0;35m$$$$$$$$    \033[0;34m\\033[0;35m$$$$$$ \033[0;34m\\033[0;35m$$ \033[0;31mv1.0      
\033[0;32m# Code By X
\033[0;32m# Modified By Pinindu Tharushan
\033[1;36m =============================================\033[1;m
\033[1;33m|       Best Web Domain To IP Converter       |
\033[1;33m|            CONTACT ME ON WHATSAPP           |
\033[1;33m|                +94702801713                 |
\033[1;36m =============================================\033[00m''')

print("𝐖𝐞𝐥𝐜𝐨𝐦𝐞")

print("web address to ip converter ")
#socket tool script

import socket
host = input(str("enter your web domain :"))
print(socket.gethostbyname(host))