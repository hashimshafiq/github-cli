from colorama import init, Style, Fore, Back
from termcolor import colored
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


if(len(sys.argv)==2):
	username = sys.argv[1]
elif(len(sys.argv)==3):
	username = sys.argv[1]
	reponame = sys.argv[2]
else:
	argumentError()
	sys.exit()


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
	print("\nUsername: "+data['login'])
if(data['name']):
	print("Name: "+data['name'])
if(data['company']):
	print("Company: "+data['company'])
if(data['bio']):
	print("Bio: "+data['bio'])
if(data['blog']):
	print("Blog: "+data['blog'])
if(data['location']):
	print("Location: "+data['location'])
if(data['html_url']):
	print("Github Profile: "+data['html_url'])










 
		

	






