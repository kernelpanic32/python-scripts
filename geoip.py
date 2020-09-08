from urllib import urlopen
import sys
import json
import socket

def GetPublicIP():
	#gets your own public ip address
	try:
		public_ip = urlopen('http://api.ipify.org').read()
		return public_ip
	except:
		print('An error has ocurred while retrieving public ip address, try again later.')

def GetData(ip_address):
	try:
		socket.inet_aton(ip_address)
		try:
			data = urlopen('http://ipinfo.io/'+ip_address).read()
			data = json.loads(data)
			return data
		except:
			print('')
			print('An error has ocurred, try again later.')
	except:
		print('')
		print('Please enter a valid IP address.')

def PrintData(data):

	countryCodes = []
	countryNames = []
	continentNames = []

	#if country codes json exists then outputs more specific region location
	try:
		with open('country_codes.json') as country_codes:
			json_data = json.load(country_codes)
			all_countries = json_data["country"]

			for json_row in all_countries:

				if data['country'] == json_row["countryCode"]:
					countryCodes.append(json_row["countryCode"])
					countryNames.append(json_row["countryName"])
					continentNames.append(json_row["continentName"])
					break

		region = data['region']+', '+json_row['countryName']+' ['+json_row["countryCode"]+'], '+json_row['continentName']

	except IOError:
		#if country codes json does not exist then outputs simple code
		region = data['region']+' ['+data['country']+']'
		print('Country codes file not accessible')

	finally:
		country_codes.close()


	try:
		print('')		
		print('IP: 			'+data['ip'])
		print('City: 			'+data['city'])
		print('Region: 		'+region)
		print('Avg. Location: 		'+data['loc'])
		print('ISP: 			'+data['org'])

	except:
		print('')
		print('An error has ocurred, try again later.')

if (len(sys.argv) > 1):
	
	if(sys.argv[1] == "?"):
		print('')
		print('syntax: "geoip" or "geoip xxx.xxx.xxx.xxx"')
	else:

		#remote public ip info
		data = GetData(sys.argv[1])
		PrintData(data)

else:
	#own public ip info
	data = GetData(GetPublicIP())
	PrintData(data)
	