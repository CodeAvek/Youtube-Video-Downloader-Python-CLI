'''Write this Code in file with .py extension'''
#Just Copy Link of any Youtube Video Input......
#IF Output is Showing Error Than -Go To Terminal And Just type "pip install pytube" it will Install Pytube module 


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
