// this is a sample of password-protected webcraping 

import requests
from bs4 import BeautifulSoup

username = 'email'
password = 'password'
scrape_url = 'http://fantasy.trashtalk.co/?tpl=classement&t=1'

login_url = 'http://fantasy.trashtalk.co/login.php'
login_info = {'email': username,'password': password}

#Start session.
session = requests.session()

#Login using your authentication information.
session.post(url=login_url, data=login_info)

#Request page you want to scrape.
url = session.get(url=scrape_url)

soup = BeautifulSoup(url.content, 'html.parser')

for link in soup.findAll('a'):
    print('\nLink href: ' + link['href'])
    print('Link text: ' + link.text)
