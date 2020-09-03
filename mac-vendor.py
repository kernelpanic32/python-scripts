from urllib import urlopen
import sys
import json
import socket

if (len(sys.argv) > 1):
	print('')
	for i in range(1, len(sys.argv)):
		try:
			data = urlopen('https://api.macvendors.com/'+sys.argv[i]).read()
			print('MAC: '+sys.argv[i].upper()+' -> '+data)
		except:
			print('An error has occurred.')
else:
	print('')
	print('Please enter a valid MAC address.')

