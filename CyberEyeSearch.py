#coded by @neosolar
import os
import sys
import time
import requests
import json
import urllib.request
from termcolor import colored
from bs4 import BeautifulSoup
# Баннер
print(colored("""
  ____      _               _____           ____                      _     
 / ___|   _| |__   ___ _ __| ____|   _  ___/ ___|  ___  __ _ _ __ ___| |__  
| |  | | | | '_ \ / _ \ '__|  _|| | | |/ _ \___ \ / _ \/ _` | '__/ __| '_ \ 
| |__| |_| | |_) |  __/ |  | |__| |_| |  __/___) |  __/ (_| | | | (__| | | |
 \____\__, |_.__/ \___|_|  |_____\__, |\___|____/ \___|\__,_|_|  \___|_| |_|
      |___/                      |___/                                      

""" , 'yellow'))
print(colored('Development / all questions - @Hugason\n', "red"))
time.sleep(3)
# Список стартового меню
def strat_menu():
	print(colored('[1] FULL SEARCH BY PHONE NUMBER', "green"))
	print(colored('[2] FULL SEARCH BY MAIL', "green"))
	print(colored('[3] FULL SEARCH BY NICKNAME INTERNET', "green"))
	print(colored('[4] FULL SEARCH BY PHOTO', "green"))
	print(colored('[5] SEARCH BY IP', "green"))
	print(colored('[6] SEARCH BY CARD NUMBER', "green"))
	print('')
	start_menu = input(colored('Enter number: ', "green"))
	# Конструкция отвечающая за выбор стартового меню
	if start_menu == '1':
		phone_info()
	elif start_menu == '2':
		pass
	elif start_menu == '3':
		pass
	elif start_menu == '4':
		pass
	elif start_menu == '5':
		search_ip()
	elif start_menu == '6':
		search_card()

# Получение стандартной информации о номере телефона
# UPD: Пробив по базе РФ 4млн человек
def phone_info():
	phone = input(colored('Enter phone number: ', "green"))
	try:
		getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + str(phone)
		DB = 'db/DB'


		try:
			infoPhone = urllib.request.urlopen(getInfo)
			with open(DB, mode='r', encoding='utf_8') as base:
				dbfile = base.readlines()

		except:
			print(colored("check your Internet connection", "red"))
		infoPhone = json.load(infoPhone)
		print(u"Country:", infoPhone["country"]["name"])
		print(u"Region:", infoPhone["region"]["name"])
		print(u"Region2:", infoPhone["region"]["okrug"])
		print(u"Operator:", infoPhone["0"]["oper"])
		print(u"World:", infoPhone["country"]["location"])
		for line in dbfile:
			if phone in line:
				print(line)
			elif len(phone) > 12:
				print(colored('Error, Enter valid phone number', "red"))


	except:
		print(colored("Not found!", "red"))
#Поиск информации по номеру карты РФ
def search_card():
	card = str(input(colored('Enter card number: ', "green",)))
	DB_card = 'db/DB'
	with open(DB_card, mode='r', encoding='utf_8') as base_card:
		dbfile_card = base_card.readlines()
		for line_card in dbfile_card:
			if card in line_card:
				print(line_card)
			elif len(card) < 16:
				print(colored('Error, Enter valid card number', "red"))


# получение информации о IP адресе
def search_ip():
	ip = input(colored('Enter IP address: ', "green"))
	try:
		getIp = 'http://htmlweb.ru/geo/api.php?json&ip=' + str(ip)
		r = requests.get(f'http://ip-api.com/json/{ip}').json()
		try:
			infoIp = urllib.request.urlopen(getIp)
		except:
			print(colored('sorry!'))
		infoIp = json.load(infoIp)
		print(u'Country:', infoIp["country"]["english"])
		print(u'Region:', infoIp["region"]["name"])
		print(u'City:', infoIp["capital"]["english"])
		print(u'Longitude:', infoIp["capital"]["longitude"])
		print(u'Latitude:', infoIp["capital"]["latitude"])
		print(u'City code:', infoIp["capital"]["telcod"])
		print(u'Organisation:', r["org"])
		print(u'ISP:', r["isp"])
		print(u'Zip:', r["zip"])
	except:
		print(colored('Not found!', "red"))



strat_menu()
























































