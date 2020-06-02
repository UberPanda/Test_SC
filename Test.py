## Test script 

import sys

task = int(sys.argv[1])

if task == 1: # First Task

	import ssl 
	from cryptography import x509
	from cryptography.hazmat.backends import default_backend

	URL = sys.argv[2] ## Formatting is basic, no --parameter
	port = sys.argv[3]

	connection = ssl.create_connection((URL, port))
	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	socket = context.wrap_socket(connection, server_hostname=URL) ## Cannot use get_server_certificate because it fails SNI
	
	cert_PEM = bytes(ssl.DER_cert_to_PEM_cert(socket.getpeercert(True)),'utf8') # Convert to bytes for x509
	
	certificate = x509.load_pem_x509_certificate(cert_PEM, default_backend()) # from PEM to human readable
	
	SAN = certificate.extensions.get_extension_for_class(x509.SubjectAlternativeName) # Get the SAN extension
	
	
	print('')
	print('Certificate Information:\n')
	print('Subject: ' + str(certificate.subject))
	print('Issuer: ' + str(certificate.issuer))
	print('SAN: ' + str(SAN.value.get_values_for_type(x509.DNSName)))
	print('Valid From: ' + str(certificate.not_valid_before) + ' to ' + str(certificate.not_valid_after))
	
	if (certificate.not_valid_before.today() >= certificate.not_valid_before) and (certificate.not_valid_after.today() <= certificate.not_valid_after):
		print('Certificate is valid')
	elif certificate.not_valid_before.today() < certificate.not_valid_before: 
		print('Certificate is not valid (not valid yet)')
	elif certificate.not_valid_after.today() > certificate.not_valid_after:
		print('Certificate is not valid (expired)')
	
	print('')
	
elif task == 2: # Second task
	
	import requests ## To perform the GET request
	from bs4 import BeautifulSoup ## Parser to navigate the HTML result
	
	URL = sys.argv[2] 
	
	fort_URL = 'https://fortiguard.com/webfilter?q=' + URL 
	
	response = requests.get(fort_URL)
	
	soup = BeautifulSoup(response.text, features="html5lib")
		
	print(soup.body.find('h4', attrs={'class':'info_title'}).text)
	
	
