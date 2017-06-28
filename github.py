import requests
import sys

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


print("Getting information")




 
		

	






