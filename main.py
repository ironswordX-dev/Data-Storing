import replit
from replit import *
import time
from time import *
def clr(pausetime):
  adress = 0
  value = 0
  sleep(pausetime)
  print("\033c", end="")
def system():
  choice = input("Read, Write, List, or Delete?: ")
  if choice == "read":
    adress = input("Adress?: ")
    print(db[adress])
    clr(0.8)
    system()
  elif choice == "write":
    adress = input("Adress?: ")
    value = input("Value?: ")
    db[adress] = value
    clr(0.8)
    system()
  elif choice == "delete":
    adress = input("Adress?: ")
    del db[adress]
    clr(0.8)
    system()
  elif choice == "list":
    keys = db.keys()
    print(db.keys())
    clr(10)
    system()
system()