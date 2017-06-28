from colorama import init, Style, Fore, Back
from termcolor import colored
import requests
import sys, itertools
import threading,time

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
	print("Argument Missing")
	print("Usage:")
	print(usage)
	print("Example:")
	print(example)


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
print(Fore.GREEN + Style.BRIGHT + Fore.GREEN + "Getting information")
time.sleep(3)
spinner.stop()





 
		

	






