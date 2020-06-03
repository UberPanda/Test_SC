# Test_SC

This is an interactive python 3.8 script designed to perform 2 tasks: 

1. Get SSL certificate information from a given URL (Subject, Issuer, SAN and Validity).

2. Get the category of a given URL through Fortiguard. 

To run, the script requires the following modules : 
- sys (standard python)
- ssl (standard python)
- cryptography (standard python)
- requests
- bs4 (BeautifulSoup)
 
To use it, simply run the script and, when asked, input: 
1. The task number (1 or 2)
2. The URL to use
3. For task 1, the port to use (default used if empty is 443)
