##############################
#Coded by : Hagi Rizki Suherlan
##############################



import requests
import json
from datetime import datetime
import time
import os

now = datetime.now()
day = now.day
month = now.month
year = now.year


banner = """
/help            :    Menuju Menu Bantuan
/all             :    Menampilkan Semua List Negara
/provinsi        :    Menampilkan Kasus Di provinsi
/global          :    Menampilkan Data Global
/quit            :    Keluar Program
"""
logo = '''\033[32m
            ____ _____     _____ ____  _  ___
           / ___/ _ \ \   / /_ _|  _ \/ |/ _ \

          | |  | | | \ \ / / | || | | | | (_) |
          | |__| |_| |\ V /  | || |_| | |\__, |
           \____\___/  \_/  |___|____/|_|  /_/
            ==========> Navigate <===========
                \033[31m<=======> R3XD <=======>\033[0m 
'''

def logos():
	print(H + "UPDATE :"  ,day,"-",month,"-",year)
	
	print(logo)
	print("\033[1m-"*59)

		
	
def check():
	try:
		r = requests.get("https://api.kawalcorona.com")
		r = r.text
		f = open("json/data.json","w")
		f.write(r)
		f.close()
		
		s = requests.get("https://api.kawalcorona.com/indonesia/provinsi/")
		s = s.text
		t = open("json/provinsi.json","w")
		t.write(s)
		t.close()
		
		u = requests.get("https://api.kawalcorona.com/positif")	
		u = u.text
		v = open("json/positif.json","w")
		v.write(u)
		v.close()
		
		w = requests.get("https://api.kawalcorona.com/sembuh")
		w = w.text
		x = open("json/sembuh.json","w")
		x.write(w)
		x.close()
		
		y = requests.get("https://api.kawalcorona.com/meninggal")
		y = y.text
		z = open("json/meninggal.json","w")
		z.write(y)
		z.close()
		
		
		
		os.system("clear")
		print("\033[1mMode : \033[32mOnline")
		menu()
	
	except IOError:
		print(M+"Koneksi Gagal, Periksa Internet Anda!\nMasuk Secara offline?" + B)
		input("[ OFFLINE ]")
		os.system("clear")
		print("\033[1mMode : \033[31mOffline")
		menu()
	



U = "\033[35m"
K = "\033[33m"
H = "\033[32m"
M = "\033[31m"
B = "\033[0m"

def world():
	f = open("json/positif.json","r")
	g = open("json/sembuh.json","r")
	h = open("json/meninggal.json","r")
	f = json.load(f)
	g = json.load(g)
	h = json.load(h)
	print("POSITIF  :",f['value'])
	print("SEMBUH :",g['value'])
	print("MENINGGAL :",h['value'])
	print("-"*59)
	menu()
	

def province(num):
	f = open("json/provinsi.json","r")
	f = json.load(f)
	g = dict(f[num])
	h = g['attributes'].values()
	h = list(h)
	prov = h[2]
	pos = h[3]
	neg = h[4]
	men = h[5]
	display_province(prov,pos,neg,men)
		
def display_province(prov,pos,neg,men):
	print("\033[1mPROVINSI  \033[0m:",prov)
	print(M + "POSITIF   \033[0m:",pos)
	print(H + "SEMBUH    \033[0m:",neg)
	print(U + "MENINGGAL \033[0m:",men)
	print("="*59)

def navigate(num):
	f = open("json/data.json","r")
	f = json.load(f)
	g = dict(f[num])
	h = g['attributes'].values()
	h = list(h)
	
	n = h[1]
	p = h[5]
	s = h[6]
	m = h[7]
	display_global(n,p,s,m)
	


def display_global(negara,positif,sembuh,meninggal):
	
	print("\033[1mNEGARA   \033[0m :",negara)
	print(M + "POSITIF   \033[0m:",positif)
	print(H + "SEMBUH    \033[0m:",meninggal)
	print(U + "MENINGGAL \033[0m:",sembuh)
	print("\033[1m-"*59)
	
def menu():
	logos()
	navigate(36)
	a = input("\033[34m< COMMAND > " + B)
	if a == "/all":
		os.system("clear")
		print("\033[1mSource : Https://kawalcorona.com\033[0m [ COUNTRY DATA ] ")
		print("-"*59)
		c = 0
		while c < 169:	
			navigate(c)
			c += 1
		menu()
	if a == "/help":
		os.system("clear")
		print("-"*59)
		print(banner)
		print("-"*59)
		menu()
	if a == "/quit":
		os.system("exit")
		print("\033[32mTerima Kasih , Jaga Kesehatan ya :)"+B)
	

	if a == "/provinsi":
		os.system("clear")
		print("\033[1mSource : Https://kawalcorona.com\033[0m [ PROVINCE DATA ]")
		print("-"*59)
		i = 0
		while i < 20:
			province(i)
			i +=1
		menu()
	
	if a == "/global":
		os.system("clear")
		print("\033[1mSource : Https://kawalcorona.com\033[0m [ GLOBAL DATA ]")
		print("-"*59)
		world()	
		
	else:
		os.system("clear")
		menu()
	
			

check()


