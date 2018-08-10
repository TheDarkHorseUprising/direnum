#imports
import requests
#banner
print('''________  .__                                               
\\______ \\ |__|______  ____  __ __  _____      ______ ___.__.
 |    |  \\|  \\_  __ \\/    \\|  |  \\/     \\     \\____ <   |  |
 |    `   \\  ||  | \\/   |  \\  |  /  Y Y  \\    |  |_> >___  |
/_______  /__||__|  |___|  /____/|__|_|  / /\\ |   __// ____|
        \\/               \\/            \\/  \\/ |__|   \\/''')
#input
url=input("url: ")
ext=input("ext (\"/\" for dir): ")
wlist=input("wordlist: ")

#get lines
wlistlines=open(wlist,"r").readlines()
#loop
for i in range(0, len(wlistlines)):
    enum=wlistlines[i].replace("\n","")
    r=requests.get(url+"/"+enum+ext)

    #if not 404
    if r.status_code != 404:
        print(url+"/"+enum+ext+" - "+str(r.status_code))
    
