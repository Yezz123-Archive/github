#!/bin/usr/python3.8
#_UTF-8_


import os,sys,json
from time import sleep
try:
	import requests
except:
	os.system('pip install requests')




class Main:
	def __init__(self):
		self.Start()
	
	def Start(self):
		os.system('clear')
		print("{  Gihub Information  }".center(55))
		print(" Coded by : Yezz123".center(53))
		print("\n")
		print("[!] Example Target Username : https://github.com/user")
		print("[!] You only enter the 'user'")
		print(58*"-")
		self.User_Target = input("[?] Target Username : ")
		print("\nChecking....")
		sleep(1)
		try:
			self.Get = requests.get('https://api.github.com/users/%s'%(self.User_Target))
			self.Req = json.loads(self.Get.text)
			print("""
|--------------------------------------------------------------|
| Username :		| %s
| ID :			| %s
| Node ID :		| %s
| Avatar URL :		| %s
| HTML Url :		| %s
| Type :			| %s
| Name :			| %s
| Company :		| %s
| Blog :			| %s
| Location :		| %s
| Email :			| %s
| Hireable :		| %s
| Bio :			| %s
| Tweeter Username :	| %s
| Total Repos :		| %s
| Gits Total :		| %s
| Followers :		| %s
| Following :		| %s
| Join at :		| %s
| Update at :		| %s
|-----------------------|--------------------------------------|
			"""%(self.Req['login'], self.Req['id'], self.Req['node_id'], self.Req['avatar_url'], self.Req['html_url'], self.Req['type'], self.Req['name'], self.Req['company'], self.Req['blog'], self.Req['location'], self.Req['email'], self.Req['hireable'], self.Req['bio'], self.Req['twitter_username'], self.Req['public_repos'], self.Req['public_gists'], self.Req['followers'], self.Req['following'], self.Req['created_at'], self.Req['updated_at']))
			exit("\n")
		except (KeyboardInterrupt, EOFError):
			exit()
		except Exception as F:
			exit("\nNo Connection")

if __name__=='__main__':
	try:
		Main()
	except (KeyboardInterrupt, EOFError):
		exit()