from os import system
from time import sleep

while True:
    system('/etc/init.d/example stop')
    sleep(10)
    system('/etc/init.d/example start')
    sleep(3060)
