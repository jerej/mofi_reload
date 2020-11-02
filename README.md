# Mofi Router Reboot

While troubleshooting issues with devices and ISPs, sometimes you just need to get things back working and troubleshoot later. Is this valuable to anyone else? perhaps more as an example of how to get into the Mofi API using Python to do something more interesting.

## Usage

Setup your venv the first time

`pipenv install`

Then to run it:

```
export MOFI_IP=192.168.10.1
export MOFI_USER=root
export MOFI_PASS=somepassphrase
pipenv run ./mofi_reboot.py
```

or

`pipenv run ./mofi_reboot.py <router_ip>`
