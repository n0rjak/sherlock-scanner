# Sherlock Scanner - by N0rjak
# Web path scanner

import requests
import sys

STATUSES = [200, 300, 302]

def create_url(host, resource):
	url = host + '/' + resource
	if ("://" in host) == False:
		url = "http://" + url
	return url

def do_request(url):
	if (url != None):
		try:
			response = requests.get(url)
			return response.status_code
		except:
			print("Error")

def scan_item(host, item):
	url = create_url(host, item)
	status = do_request(url)
	response = url + " ===> " + str(status)
	if (status in STATUSES):
		print(response)

def scan_wordlist(host, wordlist):
	wordlist = open(wordlist, "r")
	lines = wordlist.readlines()
	for line in lines:
		if ('#' in line) == False:
			scan_item(host, line.rstrip('\n'))
		

if __name__ == "__main__":
	if len(sys.argv) > 2:
		scan_wordlist(sys.argv[1], sys.argv[2])
	else:
		print("Please, enter host and wordlist path")
