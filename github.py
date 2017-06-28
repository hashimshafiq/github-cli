from colorama import init, Style, Fore, Back
import sys, itertools, threading, time, requests
from pprint import pprint
from tabulate import tabulate

class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)



init(autoreset=True)
API_URL = 'https://api.github.com/'

usage = 'python filename username'
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




if(len(sys.argv)==2):
	username = sys.argv[1]
	getUSERDATA(username)
elif(len(sys.argv)==3):
	username = sys.argv[1]
	reponame = sys.argv[2]
	getREPODATA(username,reponame)
else:
	argumentError()
	sys.exit()









 
		

	






