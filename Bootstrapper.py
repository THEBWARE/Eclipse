import os
import requests
import zipfile
from termcolor import colored

eclipse_art = """
 _____     _ _                
| ____|___| (_)_ __  ___  ___ 
|  _| / __| | | '_ \/ __|/ _ \
| |__| (__| | | |_) \__ \  __/
|_____\___|_|_| .__/|___/\___|
              |_|                            
"""
print(colored(eclipse_art, 'blue'))

url = 'https://github.com/THEBWARE/Saturngg/releases/download/Setup/Saturn.gg-V1.1.4.zip'
filename = 'Saturn.gg-V1.1.4.zip'

response = requests.get(url)
with open(filename, 'wb') as f:
    f.write(response.content)

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall()

os.remove(filename)
