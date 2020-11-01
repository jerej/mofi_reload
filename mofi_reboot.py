#!/usr/bin/env python3
""" Reboot Mofi 4500 router without a browser

USAGE:
    ```
    export MOFI_IP=192.168.10.1
    export MOFI_USER=root
    export MOFI_PASS=somepassphrase
    pipenv run ./mofi_reboot.py
    ```
    or
    `pipenv run ./mofi_reboot.py <router_ip>`
    """

import os
import sys
import requests
import urllib3

from getpass import getpass
from bs4 import BeautifulSoup

router_ip = os.environ.get("MOFI_IP", None) or sys.argv[1]
username = os.environ.get("MOFI_USER", "root")
password = os.environ.get("MOFI_PASS", None) or getpass()
print(f"Rebooting {router_ip}...")

mofi = requests.Session()
mofi.verify = False
urllib3.disable_warnings()

response = mofi.post(
    "https://192.168.10.1/cgi-bin/luci",
    headers={"Content-type": "application/x-www-form-urlencoded"},
    data={"username": username, "password": password},
)
if response.status_code != requests.codes.ok:
    print("\n*** Login Failed! ***\n")
    mofi.raise_for_status()

# Find the custom session ID generated on login
soup = BeautifulSoup(response.content, "html.parser")
system_link = None
links = soup.find_all("a")
for link in links:
    if "System" in link.get_text():
        system_link = link.get("href")

(base_path, other) = system_link.split("/quick", 1)

response = mofi.get(
    f"https://192.168.10.1{base_path}/quick/system/reboot", params={"reboot": 1}
)
if response.status_code == requests.codes.ok:
    print("Mofi Router rebooting... Please wait 3 minutes.")
else:
    mofi.raise_for_status()
