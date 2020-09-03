from urllib import urlopen
import sys
import json
import socket

if (len(sys.argv) > 1):
	
	if(sys.argv[1] == "?"):
		print('')
		print('IP address information provider. Coded by SANGUB - 2020')
		print('syntax: Leave blank to provide your own ip info or enter another ip ex.: "geoip 152.312.53.256"')

	else:

		try:
			socket.inet_aton(sys.argv[1])
			try:
				data = urlopen('http://ipinfo.io/'+sys.argv[1]).read()
				data = json.loads(data)

				print('')		
				print('IP: 			'+data['ip'])
				print('City: 			'+data['city'])
				print('Region: 		'+data['region']+' ['+data['country']+']')
				print('Avg. Location: 		'+data['loc'])
				print('ISP: 			'+data['org'])

			except:
				print('')
				print('An error has ocurred, try again later.')
		except:
			print('')
			print('Please enter a valid IP address.')

else:

	try:
		remote_ip = urlopen('http://api.ipify.org').read()
		try:
			data = urlopen('http://ipinfo.io/'+remote_ip).read()
			data = json.loads(data)

			print('')		
			print('IP: 			'+data['ip'])
			print('City: 			'+data['city'])
			print('Region: 		'+data['region']+' ['+data['country']+']')
			print('Avg. Location: 		'+data['loc'])
			print('ISP: 			'+data['org'])

		except:
			print('')
			print('An error has ocurred, try again later.')
	except:
		print('')
		print('Please enter a valid IP address.')