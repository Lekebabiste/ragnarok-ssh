import colorama
from colorama import Fore
from colorama import Style

def print_file(filename,color,style=Style.NORMAL):
    with open(filename,'r') as f:
        a = f.read()
        print(color,style,a,Style.RESET_ALL)
        f.close()

def print_banner():
    print_file('bannerprint/banner.txt',Fore.RED,Style.BRIGHT)
    #print_file('banner-text.txt',Fore.WHITE)#(You can uncoment this line if you want)