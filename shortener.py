from pyshorteners import Shortener
from time import sleep

u = input("Enter The URL: \n")
s = Shortener()
try:
    print(s.qpsru.short(u))
    sleep(100)
except:
    print("Error")