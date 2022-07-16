#Write this Code in file with .py extension
#Just Copy Link of any Youtube Video Input......
#IF Output is Showing Error Than -Go To Terminal And Just type "pip install pytube" it will Install Pytube module 
import os
os.system('pip install pyfiglet')
os.system('pip install pytube')
os.system('clear')

R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("CodeAx1")
print(R+br)
print(G+'''
[Scraping Content From Website ]
Coded By CodeAx1
_________________________________________________''')
import os
os.system('pip install pytube')
from pytube import YouTube
from pytube.cli import on_progress
while(True):
    link = input("Enter The Link or press (q) to Quit: ")
    if link == "q":
        print("We  Quit this code")
        break
    try:
        yt = YouTube(link,on_progress_callback=on_progress)
    
        print("Guys Lets Get Started!!!!!!!!")
        print("Title:",yt.title)
        print("View:",yt.views)
        print("Length:",yt.length)
        print("rating:",yt.rating)
        Ytube = yt.streams.get_highest_resolution()
        wt = input("Enter (y) to downlaod Given Video Or Press (n): ")
        if wt.lower() == "y":
            print("Downloading.........Please Wait")
            Ytube.download()
            print("Downloaded.........Happy!!!!!!!!!!!!!!!!!")
        elif wt.lower() == "n":
            print("Ok.....")
    except:
        print('Connection error')

