from colorama import init, Style, Fore, Back
import sys, itertools, threading, time, requests
from pprint import pprint
from tabulate import tabulate
from Spinner import Spinner



init(autoreset=True)
API_URL = 'https://api.github.com/'
API_URL_1 = 'https://api.github.com/users/'

usage = 'python github.py <username>\npython github.py <username> <reponame>'
example = '> python github.py hashimshafiq'
contribute = "Contribute to this project"

def argumentError():
	print(Style.BRIGHT + Fore.RED + "Argument Missing")
	print(Style.BRIGHT + Fore.YELLOW + "Usage:")
	print(Style.BRIGHT + Fore.CYAN + usage)
	print(Style.BRIGHT + Fore.YELLOW + "Example:")
	print(Style.BRIGHT + Fore.CYAN + example)


def getUSERDATA(username):
	spinner = Spinner()
	spinner.start()
	print(Fore.YELLOW + Style.BRIGHT + "Getting information about user ",end='')
	print(Fore.RED + Style.BRIGHT + username)
	url = API_URL + 'users/'+username
	response = requests.get(url)
	if(response.status_code==200):
		print(Style.BRIGHT + Fore.GREEN + "Successfull...")
	elif(response.status_code==404):
		print(Style.BRIGHT + Fore.RED + "username not found")
		spinner.stop()
		sys.exit()
	elif(response.status_code==403):
		print(Style.BRIGHT + Fore.RED + "Warning: Maximum Number of Ateempts Limit Crossed")
		spinner.stop()
		sys.exit()


	data = response.json()
	spinner.stop()

	if(data['login']):
		print(Style.BRIGHT+Fore.CYAN + "\nUsername: ",end='')
		print(Style.BRIGHT+data['login'])
	if(data['name']):
		print(Style.BRIGHT+Fore.CYAN +"Name: ",end='')
		print(Style.BRIGHT+data['name'])
	if(data['company']):
		print(Style.BRIGHT+Fore.CYAN +"Company: ",end='')
		print(Style.BRIGHT+data['company'])
	if(data['bio']):
		print(Style.BRIGHT+Fore.CYAN +"Bio: ",end='')
		print(Style.BRIGHT+data['bio'])
	if(data['blog']):
		print(Style.BRIGHT+Fore.CYAN +"Blog: ",end='')
		print(Style.BRIGHT+data['blog'])
	if(data['location']):
		print(Style.BRIGHT+Fore.CYAN +"Location: ",end='')
		print(Style.BRIGHT+data['location'])
	if(data['html_url']):
		print(Style.BRIGHT+Fore.CYAN +"Github Profile: ",end='')
		print(Style.BRIGHT+data['html_url'])

	headers = ["Public Repos","Public Gists","Followers","Following"]
	table = [[data['public_repos'],data['public_gists'],data['followers'],data['following']]]

	print(tabulate(table, headers, tablefmt="fancy_grid",numalign='center'))


def getREPODATA(username,reponame):
	spinner = Spinner()
	spinner.start()
	print(Fore.YELLOW + Style.BRIGHT + "Getting information about repo ",end='')
	print(Fore.RED + Style.BRIGHT + reponame)
	url = API_URL + 'repos/'+username+'/'+reponame
	response = requests.get(url)
	if(response.status_code==200):
		print(Style.BRIGHT + Fore.GREEN + "Successfull...")
	elif(response.status_code==404):
		print(Style.BRIGHT + Fore.RED + "username or repo not found")
		spinner.stop()
		sys.exit()
	elif(response.status_code==403):
		print(Style.BRIGHT + Fore.RED + "Warning: Maximum Number of Ateempts Limit Crossed")
		spinner.stop()
		sys.exit()

	data = response.json()
	spinner.stop()

	if(data['name']):
		print(Style.BRIGHT+Fore.CYAN + "\nRepository Name: ",end='')
		print(Style.BRIGHT+data['name'])
	if(data['description']):
		print(Style.BRIGHT+Fore.CYAN +"Description: ",end='')
		print(Style.BRIGHT+data['description'])
	if(data['homepage']):
		print(Style.BRIGHT+Fore.CYAN +"Project HomePage: ",end='')
		print(Style.BRIGHT+data['homepage'])
	if(data['html_url']):
		print(Style.BRIGHT+Fore.CYAN +"Github Link: ",end='')
		print(Style.BRIGHT+data['html_url'])
	if('parent' in data.keys()):
		print()
		print(Style.BRIGHT+Fore.CYAN+"This repo is forked from ",end='')
		print(Style.BRIGHT+data['parent']['owner']['login'])
		print(Style.BRIGHT+Fore.CYAN+"Origial Owner: ",end='')
		print(Style.BRIGHT+data['parent']['owner']['login'])
		print(Style.BRIGHT+Fore.CYAN+"Original Github Link: ",end='')
		print(Style.BRIGHT+data['parent']['html_url'])
	
	headers = ["Language","Watching","Stars","Forks","Issues","Size (KB)","Default Branch"]
	table = [[data['language'],data['subscribers_count'],data['stargazers_count'],data['forks_count'],data['open_issues_count'],data['size'],data['default_branch']]]
	print(tabulate(table, headers, tablefmt="fancy_grid",numalign='center'))




def getALLREPOS(username):
	spinner = Spinner()
	spinner.start()
	print(Fore.YELLOW + Style.BRIGHT + "Getting information about all repo of user ",end='')
	print(Fore.RED + Style.BRIGHT + username)
	count = 0
	boolean=True
	while boolean:
		url = API_URL_1 +username+'/repos'
		payload = {'type': 'all','page':count,'per_page':100}
		
		response = requests.get(url,payload)

		if(response.status_code==200):
			print(Style.BRIGHT + Fore.GREEN + "Successfull...")
		elif(response.status_code==404):
			print(Style.BRIGHT + Fore.RED + "username or repo not found")
			spinner.stop()
			sys.exit()
		elif(response.status_code==403):
			print(Style.BRIGHT + Fore.RED + "Warning: Maximum Number of Ateempts Limit Crossed")
			spinner.stop()
			sys.exit()

		link = response.headers.get('link',None)
		data = response.json()
		spinner.stop()

		for d in data:
			print(d['name'])
		if link is None:
			boolean=False
		count = count + 1

	spinner.stop()

	






def main():
	if(len(sys.argv)==2):
		username = sys.argv[1]
		getUSERDATA(username)
	elif(len(sys.argv)==3):
		username = sys.argv[1]
		reponame = sys.argv[2]
		if(reponame != '*'):
			getREPODATA(username,reponame)
		else:
			getALLREPOS(username)	
	else:
		argumentError()
		sys.exit()
		

if __name__ == "__main__":
	main()









 
		

	






