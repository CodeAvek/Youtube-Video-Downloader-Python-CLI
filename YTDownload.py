
## CodeAx

 - [Telegram](https://t.me/avekgaming)
 - [instagram](https://instagram.com/codeax1?utm_medium=copy_link)
 - [Youtube](https://youtube.com/channel/UC-Q6ZcOtcx1gZ9fI5MDDt3w)


## Deployment

Import python library named pytube from terminal or cmd 

```bash
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
import pyfiglet
from pytube import YouTube
while(True):
    link = input("Enter The Link or press (q) to Quit: ")
    if link == "q":
        print("We  Quit this code")
        break
    try:
        yt = YouTube(link)
    
        print("Guys Lets Get Started!!!!!!!!")
        print("Title:",yt.title)
        print("View:",yt.views)
        print("Length:",yt.length)
        print("rating:",yt.rating)

        Ytube = yt.streams.get_highest_resolution()

        wt = input("Enter (yes) to downlaod Given Video Or Press (no): ")
        if wt.lower() == "yes":
            print("Downloading...............by CodeAx")
            Ytube.download()
            print("Downloaded.........Happy!!!!!!!!!!!!!!!!!")
        elif wt.lower() == "no":
            print("Ok.....")
    except:
        print('Connection error')
```


