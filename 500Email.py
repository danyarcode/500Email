#Tool 500 Email By @Danyar.code

#Rangakan (Color) 
red = "\033[31m"
green = "\033[32m"
white = "\033[0;1m"
yellow = "\033[33;1m"
blue = "\033[34m"
dlm ="\033[36;1m"






# Ip zanen Kasaka active be yan na 
def ip():
	import os,time
	import requests
	os.system("clear")
	url = "https://api.ipify.org"
	active = "https://textuploader.com/tak5f/raw"
	req = requests.get(url).text
	id = requests.get(active).text
	if req in id:
		print(f"{green}Ip Yoir Active (:{white}")
		time.sleep(2)
		pass
	else:
		print(dlm+f" {req} : Your Ip Is Not Ative ):{white}")
	
ip()
	
	
	

#Anime (aniemayshn) Just varible animee
# la naw defe yakama 
		
#Kat zanen (time)






import os 
os.system("clear")

def make_email():
	import random
	import time
	os.system("clear")
	print("[+] Pleas Input Name \n\n")
	name = input("[!] Name :")
	txt = "1234567890011"
	ft = open("Email.txt","w")
	for wwwe in range(1500):
		x1 = random.choice(txt)
		x2 = random.choice(txt)
		x3 = random.choice(txt)
		end = name+x1+x2+x3
		json = end+"@yahoo.com"
		ft.write(json+"\n")
	os.system("clear")
	animee = (yellow+"Email Find Pleas wait For Check Die or Live"+white)
	import sys
	import time
#global animee
	for x in animee:
		print(x,end ="")
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(3)
	os.system("clear")
		
		
#make_email()


def zhmardn():
	ani=0
	os.system("clear")
	file = input("[!] File :")
	fss = open(file,"r").readlines()
	for x in fss:
		ani+=1
		os.system("clear")
		print("All Email :{}".format(ani))
	print("\n\n[-] All Email Check (:")
	time.sleep(4)
#zhmardn()


def owner():
	os.system("clear")
	import requests
	die=0
	live=0
	wastan = 0
	sytem = open("Email2.txt","w")
	import sys
	import time
	import datetime
	tnt = open("Email.txt","r").readlines()
	for w in tnt:
		time.sleep(8)
		wwe = w.strip()
		new_api = "https://dangersyumyum.000webhostapp.com/api.php?email={}".format(wwe)
		t = requests.get(new_api).text
		
		if "DIE" in t:
			die+=1
			os.system("clear")
		#	global time
			aha = """
	-----------^•^•^•^•^•^•------------
	-                                 -
	-         CHECKER EMAIL           -
	-                                 -
	-----------^•^•^•^•^•^•------------
			"""
			print(aha)
			print(green+"[+] DIE : "+str(die))
			print(red+"[-] LIVE : "+str(live))
			print(white)
			sytem.write(wwe+"\n")
		else:
			os.system("clear")
			live+=1
			aha = """
	-----------^•^•^•^•^•^•------------
	-                                 -
	-         CHECKER EMAIL           -
	-                                 -
	-----------^•^•^•^•^•^•------------
			"""
			print(aha)
			print(green+"[+] DIE : "+str(die))
			print(red+"[-] LIVE : "+str(live))
			print(white)
	os.system("clear")
	print(f"{yellow}All Email Check {white}")
	time.sleep(2)
	pass
			
			
			
		
#owner()




def instagram():
	import user_agent
	import datetime,requests
	from datetime import datetime
	from user_agent import generate_user_agent
	
	p=generate_user_agent()
	os.system("clear")
	hub = open("Email.txt","r").readlines()
	hyb = open("Email3.txt","w")
	kotay=0
	axer=0
	for x in hub:
		u = x.strip()
		time.sleep(1)
		url_insta = 'https://www.instagram.com/accounts/login/ajax/'
		head_insta= {
                        'accept':'*/*',
                        'accept-encoding':'gzip,deflate,br',
                        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                        'content-length':'269',
                        'content-type':'application/x-www-form-urlencoded',
                        'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
                        'origin':'https://www.instagram.com',
                        'referer':'https://www.instagram.com/',
                        'sec-fetch-dest':'empty',
                        'sec-fetch-mode':'cors',
                        'sec-fetch-site':'same-origin',
                        'user-agent':p ,
                        'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
                        'x-ig-app-id':'936619743392459',
                        'x-ig-www-claim':'0',
                        'x-instagram-ajax':'8a8118fa7d40',
                        'x-requested-with':'XMLHttpRequest'
		}
		time_now = int(datetime.now().timestamp())
		data_insta = {
                        'username': u,
                        'enc_password': "#PWD_INSTAGRAM_BROWSER:0:"+str(time_now)+":11",
                        'queryParams': {},
                        'optIntoOneTap': 'false'
		}
		end = requests.post(url_insta,headers=head_insta,data=data_insta).text
		if '"user":true' in end:
			os.system("clear")
			kotay+=1
			hyb.write(u+"\n")
			print("\n\n")
			print(f"{green}FAKE : {kotay}{white}")
			print(f"{red}EMAIL : {axer}{white}")
		if '"message":"Please wait a few minutes before you try again."' in end:
			time.sleep(250)
			pass
		else:
			os.system("clear")
			axer+=1
			print("\n\n")
			print(f"{green}FAKE : {kotay}{white}")
			print(f"{red}EMAIL : {axer}{white}")
	print("\n\nAll Email Check (:")
	time.sleep(3)
			
			
logo = """
	
    .'``.``.
 __/ (o) `, `.
'-=`,     ;   `.
    \    :      `-.
    /    ';        `.
   /      .'         `.
   |     (      `.     `-.._
    \     \` ` `. \         `-.._
     `.   ;`-.._ `-`._.-. `-._   `-._
       `..'     `-.```.  `-._ `-.._.'
         `--..__..-`--'      `-.,'
            `._)`/
             /--(
          -./,--'`-,
       ,^--(                    
       ,--' `-,         
       
       **************************************
        * -> Instagram: danyar.code          *
        * -> Telegram: https://T.me/n9tn0w   *
        * -> Staf: ❌                        *
        ************************************** 
        
       """
		
def minu():
	os.system("clear")
	global logo 
	print(logo)
	print(f"{yellow}[ 1 ] Get Email")
	print("[ 2 ] Check Die Or Live")
	print("[ 3 ] Check Instagram True")
	print(f"[ 4 ] Loop Email{white} ")
	print(f"{blue}[ 5 ] Exit{white} ")
	de = int(input(f"\n\n{dlm}[!] Choice :{white}"))
	if de==1:
		os.system("clear")
		make_email()
		minu()
	if de==2:
		os.system("clear")
		owner()
		minu()
	if de==3:
		os.system("clear")
		instagram()
		minu()
	if de==4:
		os.system("clear")
		zhmardn()
		minu()
	if de ==5:
		os.syatem("clear")
		exit()
	else:
		import time
		print("\n")
		print("[!] Choice Erorr")
		time.sleep(3)
		minu()
	
		
minu()
