import os
import requests
url = 'www.seasky.org'
starter_dos = os.system(f'ping -t -l 1000 {url}')
os.system('echo do not include http or https')


