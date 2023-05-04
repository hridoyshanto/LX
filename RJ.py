#_________[ IMPORTING MODULE ]_________>>
import re,os,sys,smtplib,requests,itertools,json,zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
#from g4rzk.module import*
from bs4 import BeautifulSoup as bs
from os import system as cmd
from os import listdir as lst
from sys import exit as exit
from sys import argv as arg
from time import sleep as slp
from random import randint as rr
from requests import get as get
#_________[ BASIC COLOURS ]_________>>
red = "\033[1;31m"
green = "\033[1;32m"
white = "\033[1;37m"
blue = "\033[1;35m"
#_________[ SCRIPT BANNER ]_________>>
bannerID = f"""{white}  [ crecreaterAHSAM ] [ Version : {green}0.0.1{white} ]
	  d888b         d88b        d8888b  
	 88  Y8b       8P  d8       88   8D 
{blue}	 88           88    88      88   88 
	 88  ooo      88    88      88   88 
{white}	 88   88       8b  d8       88   8D 
	  Y888P         Y88P        Y8888D"""
	#_________[ BANNER DEF ]_________>>
def banner():
	cmd("clear")
	print(bannerID)
	print("--------------------------------------------------")
	print("    No Technology thats connected to internet")
	print("                is Unhackable")
	print("--------------------------------------------------")
	#___________[ FACEBOOK CLONING TOOL ]__________>>
def fb_clone():
	banner()
	print("[01] KingQadir - uid")
	print("[02] Hannan-404 - TEST")
	print("[03] XERX-XD - RXN")
	print("[04] USMAN-RAJPOOT - NOTHING")
	print("[05] Pavel-Mahmud-Alif - BAHA-PRO")
	print("[06] SEXY-RIKI-404 - RD")
	print("[07] FARAZ-ID - Test")
	print("[08] hop09 - hpro")
	print("[09] hop09 - file")
	print("[10] REFAT-156 - RNDM")
	print("[11] Hackerrv33 - rahulrbc")
	print("[12] ShahWahid0785 - random-afg")
	print("[13] Sarfraz-Ssb SSB")
	print("[14] AKING110 - AKING-PRO")
	print("[15] syedzada1100 - Crack-Pro")
	print("[16] JUTTBRAND - pro")
	print("[17] ANONYMOUS-U7P4L - File")
	print("[18] essasoomro - jaadu")
	print("[19] FaisalRehman111 - faisal")
	print("[20] AHMADOAFRIDI - FILE_CLONING")
	print("[21] XAIVER-XD - KLEIN")
	print("[22] binyaminbinni - bxi")
	print("[23] Mr-Qureshi-xd - KING")
	print("[00] Main Menu")
	print("--------------------------------------------------")
	fbc = input("[>>] Input Your Option : ")
	if fbc in ["01","1"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""pkg update -y
pkg upgrade -y
pkg install git -y
pkg install python -y
pip install requests
pip install mechanize
rm -rf uid
git clone https://github.com/KingQadir/uid.git
cd uid
python Qadir.py""")
	elif fbc in ["02","2"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf TEST
git clone https://github.com/Hannan-404/TEST
cd TEST
python Test.py""")
	elif fbc in ["03","3"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""apt update -y
apt upgrade -y
pkg install python -y
pkg install git -y
pip unistall requests
pip install requests bs4 rich mechanize 
git clone https://github.com/XERX-XD/RXN
cd RXN
python rxn.py""")
	elif fbc in ["04","4"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/USMAN-RAJPOOT/NOTHING
cd NOTHING 
python USMAN.py""")
	elif fbc in ["05","5"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""$ pkg update
pkg upgrade -y
pkg install python -y
pkg install python2 -y
pip install requests
pip install mechanize
pip install bs4
pip install rich
pkg install git -y
pip uninstall requests chardet urllib3 idna certifi -y
pip install chardet urllib3 idna certifi requests
rm -rf BAHA-PRO
git clone https://github.com/Pavel-Mahmud-Alif/BAHA-PRO
cd BAHA-PRO
python run.py""")
	elif fbc in ["06","6"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/SEXY-RIKI-404/RD
cd RD
python Random.py""")
	elif fbc in ["07","7"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/FARAZ-ID/Test.git
cd Test
python Test.py""")
	elif fbc in ["08","8"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""termux-setup-storage
pkg update 
pkg install python git -y
rm -rf hpro
git clone https://github.com/hop09/hpro
cd hpro
python hop.py""")
	elif fbc in ["09","9"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""termux-setup-storage
pkg update 
pkg install python git -y
rm -rf file
git clone https://github.com/hop09/file
cd file
python file.py""")
	elif fbc in ["10","010"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf RNDM
git clone https://github.com/REFAT-156/RNDM.git
cd RNDM
python Rndm.py""")
	elif fbc in ["11","011"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf rahulrbc
git clone --depth=1 https://github.com/Hackerrv33/rahulrbc
cd rahulrbc
python RAHUL.py""")
	elif fbc in ["12","012"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf random-afg
git clone https://github.com/ShahWahid0785/random-afg.git
cd random-afg
ls
python Random.py""")
	elif fbc in ["13","013"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf SSB
git clone --depth=1  https://github.com/Sarfraz-Ssb/SSB
cd SSB
python SSB.py""")
	elif fbc in ["14","014"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf AKING-PRO
git clone --depth=1 https://github.com/AKING110/AKING-PRO.git
cd AKING-PRO
python AKING.py""")
	elif fbc in ["15","015"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""pkg update -y
pkg upgrade -y
pkg install git -y
pkg install python -y
pip install requests
pip install mechanize
pip install bs4
pip install future
rm -rf Crack-Pro
git clone https://github.com/syedzada1100/Crack-Pro.git
cd Crack-Pro
git pull 
python Syed.py""")
	elif fbc in ["16","016"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""pkg update -y
pkg upgrade -y
pkg install git -y
pkg install python -y
pip install bs4
pip install rich 
pip install mechanize
pip install requests 
rm -rf pro
git clone https://github.com/JUTTBRAND/pro
cd pro
python JXB.py""")
	elif fbc in ["17","017"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/ANONYMOUS-U7P4L/File.git
cd File
python File.py""")
	elif fbc in ["18","018"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""git clone https://github.com/essasoomro/jaadu.git
cd jaadu
python XYZ.py""")
	elif fbc in ["19","019"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""termux-setup-storage
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git -y
pip install bs4
pip install requests
pip install rich
pip install FLAST
rm -rf faisal
git clone https://github.com/FaisalRehman111/faisal
cd faisal
python faisy.py""")
	elif fbc in ["20","020"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf FILE_CLONING
git clone https://github.com/AHMADOAFRIDI/FILE_CLONING
cd FILE_CLONING
python FILE1.py""")
	elif fbc in ["21","021"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf KLEIN
git clone https://GitHub.com/XAIVER-XD/KLEIN
cd KLEIN
python KLEIN.py""")
	elif fbc in ["22","022"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf bxi
git clone https://gitHub.com/binyaminbinni/bxi
cd bxi
chmod 777 bxi
./bxi""")
	elif fbc in ["23","023"]:
		print("\n----------------------------------------------")
		print(f"          {blue}Installing Tool Please Wait{white}")
		print("----------------------------------------------")
		cmd("""rm -rf KING
git clone https://github.com/Mr-Qureshi-xd/KING
cd KING
git pull 
python KING.py""")
	elif fbc in ["00","0"]:
		slp(1)
		menu()
	else:
		slp(1)
		fb_clone()