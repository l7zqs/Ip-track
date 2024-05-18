import requests,json,os,sys
os.system("clear")
logo="""

\033[1;36m╔═════════════════════════════════════════╗
•       \033[1;33m<WELCOME TO TRACKING ZONE>        •
\033[1;36m╚═════════════════════════════════════════╝
\033[1;32m████████╗ █████╗ ███████╗██╗███╗   ██╗
\033[1;33m╚══██╔══╝██╔══██╗██╔════╝██║████╗  ██║
 \033[1;34m  ██║   ███████║███████╗██║██╔██╗ ██║
 \033[1;35m  ██║   ██╔══██║╚════██║██║██║╚██╗██║
  \033[1;31m ██║   ██║  ██║███████║██║██║ ╚████║
 \033[1;36m  ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝
\033[1;32m╔═════════════════════════════════════════╗
║  \033[1;32m[√] DEVOLPER    :     TASIN            ║
\033[1;32m║  \033[1;33m[√] FACEBOOK    :     TASIN            \033[1;32m║
\033[1;32m║  \033[1;34m[√] WHATAPP     :     01613942358     \033[1;32m ║
\033[1;32m║  \033[1;35m[√] GITHUB      :     l7zqs            \033[1;32m║
\033[1;32m║  \033[1;31m[√] VERSION     :     1.0              \033[1;32m║
\033[1;32m║  \033[1;36m[√] SERVER      :     DATA WORKING    \033[1;32m ║ 
\033[1;32m╚═════════════════════════════════════════╝
"""

print(logo)
#Note=input("This Tool Create By TAREK ISLAM")
victim=input(' \033[1;31mVICTIM IP ADDRESS : ')
url="http://ip-api.com/json/"+victim
ip=requests.get(url).json()

print("""\n
 \033[1;33m--------------------------------------------------
                \033[1;33m VICTIM INFORMATION            
--------------------------------------------------

""")

print(" \033[1;31mVICTIM IP : \033[1;36m "+ip['query'])
print(" \033[1;31mIP STATUS : \033[1;36m "+ip['status'])
print(" \033[1;31mCOUNTRY : \033[1;36m "+ip['country'])
print(" \033[1;31mCOUNTRY CODE : \033[1;36m "+ip['countryCode'])
print(" \033[1;31mDIVISION : \033[1;36m "+ip['regionName'])
print(" \033[1;31mCITY : \033[1;36m "+ip['city'])
#print("DISTRICT : "+ip['district'])
print(" \033[1;31mNETWORK SERVICE : \033[1;36m "+ip['isp'])
print(" \033[1;31mTIMEZONE : \033[1;36m "+ip['timezone'])


  

