#imports
import subprocess
import time
import webbrowser
import os

vscode = 'C:\\Users\\Josh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
spotify = 'C:\\Users\\Josh\\AppData\\Roaming\\Spotify\\Spotify.exe'
discord = 'C:\\Users\\Josh\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe'
lunar = 'C:\\Users\\Josh\\AppData\\Local\\Programs\\lunarclient\\Lunar Client.exe'
teams = 'C:\\Users\\Josh\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart Teams.exe'
virtualDJ = 'C:\\Program Files\\VirtualDJ\\virtualdj.exe'
opera = '"C:\\Users\\Josh\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"'


#welcome
print("What is your name? ")
name = input(" ")
time.sleep(1)
print("Hello", name, "What do you want to do today? ")
app = input(" ")

if app == "Coding" or app == "coding" or app == "Code" or app == "code":
    time.sleep(1)
    print("getting your apps ready...")
    time.sleep(0.5)

    print("Opening VS Code...")
    time.sleep(1.5)
    subprocess.Popen(vscode)
    time.sleep(0.5)
    print("VS code is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("opening spotify...")
    time.sleep(1.5)
    subprocess.Popen(spotify)
    time.sleep(0.5)
    print("Spotify is open")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("Opening GitHub...")
    time.sleep(1.5)
    webbrowser.open('https://github.com')
    time.sleep(1)
    print("GitHub Is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("Opening StackOverflow...")
    time.sleep(1.5)
    webbrowser.open('https://stackoverflow.com')
    time.sleep(1)
    print("StackOverflow Is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("Opening W3Schools...")
    time.sleep(1.5)
    webbrowser.open('https://www.w3schools.com')
    time.sleep(1)
    print("W3Schools Is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("======================================")
    print("=========ENJOY YOUR CODING!!==========")
    print("======================================")

elif app == "School" or app == "school" or app == "School Work" or app == "School work" or app == "school work":
    time.sleep(1)
    print("getting your apps ready...")
    time.sleep(0.5)

    print("Opening Teams...")
    time.sleep(1.5)
    subprocess.Popen(teams)
    time.sleep(0.5)
    print("teams is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("opening spotify...")
    time.sleep(1.5)
    subprocess.Popen(spotify)
    time.sleep(0.5)
    print("Spotify is open")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("Opening WJEC...")
    time.sleep(1.5)
    webbrowser.open('https://www.wjec.co.uk')
    time.sleep(1)
    print("WJEC Is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)


    print("======================================")
    print("=======ENJOY YOUR SCHOOL WORK!!=======")
    print("======================================")

elif app == "Gaming" or app == "gaming" or app == "minecraft" or app == "Minecraft":
    time.sleep(1)
    print("getting your apps ready...")
    time.sleep(0.5)

    print("Opening Lunar Client...")
    time.sleep(1.5)
    subprocess.Popen(lunar)
    time.sleep(0.5)
    print("Lunar Client is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("opening spotify...")
    time.sleep(1.5)
    subprocess.Popen(spotify)
    time.sleep(0.5)
    print("Spotify is open")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)



    print("======================================")
    print("=========ENJOY YOUR Gamming!!=========")
    print("======================================")


elif app == "Chill" or app == "chill":
    time.sleep(1)
    print("getting your apps ready...")
    time.sleep(0.5)

    print("Opening Youtube...")
    time.sleep(1.5)
    webbrowser.open('https://www.youtube.com')
    time.sleep(0.5)
    print("youtube is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("opening spotify...")
    time.sleep(1.5)
    subprocess.Popen(spotify)
    time.sleep(0.5)
    print("Spotify is open")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)


    print("======================================")
    print("=========ENJOY YOUR Chilling!!========")
    print("======================================")

elif app == "dj" or app == "DJ" or app == "Djing" or app == "DJing" or app == "DJING":
    time.sleep(1)
    print("getting your apps ready...")
    time.sleep(0.5)

    print("Opening virutalDJ...")
    time.sleep(1.5)
    subprocess.Popen(virtualDJ)
    time.sleep(0.5)
    print("virtualDJ is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("opening spotify...")
    time.sleep(1.5)
    subprocess.Popen(spotify)
    time.sleep(0.5)
    print("Spotify is open")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)

    print("Opening rave dj...")
    time.sleep(1.5)
    webbrowser.open('https://rave.dj')
    time.sleep(1)
    print("rave dj  Is open!")
    time.sleep(0.5)
    print("  ")
    time.sleep(0.5)


    print("======================================")
    print("=======ENJOY YOUR SCHOOL WORK!!=======")
    print("======================================")

elif app == "Radio" or app == "radio":
    print("Hello", name,"What radio station do you want to listen to? ")
    station = input("") 

    #================================
    #=============Radio 1============
    #================================
    if station == "radio 1" or station == "Radio 1" or station == "bbc radio 1" or station == "BBC Radio 1" or station == "BBC radio 1":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.bbc.co.uk/sounds/play/live:bbc_radio_one')

    #================================
    #=============Radio 2============
    #================================
    elif station == "radio 2" or station == "Radio 2" or station == "bbc radio 2" or station == "BBC Radio 2" or station == "BBC radio 2":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.bbc.co.uk/sounds/play/live:bbc_radio_two')

    #================================
    #=============Radio 3============
    #================================
    elif station == "radio 3" or station == "Radio 3" or station == "bbc radio 3" or station == "BBC Radio 3" or station == "BBC radio 3":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.bbc.co.uk/sounds/play/live:bbc_radio_three')

    #================================
    #=============Radio 4============
    #================================
    elif station == "radio 4" or station == "Radio 4" or station == "bbc radio 4" or station == "BBC Radio 4" or station == "BBC radio 4":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.bbc.co.uk/sounds/play/live:bbc_radio_fourfm')

    #================================
    #==========Radio 5 live=========
    #================================
    elif station == "radio 5 live" or station == "Radio 5 live" or station == "bbc radio 5 live" or station == "BBC Radio 5 live" or station == "BBC radio 5 live":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.bbc.co.uk/sounds/play/live:bbc_radio_five_live')

    #================================
    #=========asian network==========
    #================================
    elif station == "Asian Network" or station == "asian Network" or station == "asian network" or station == "Asian Net Work" or station == "asian net work":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.bbc.co.uk/sounds/play/live:bbc_asian_network')

    #================================
    #==========Heart================
    #================================
    elif station == "Heart" or station == "heart":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.globalplayer.com/live/heart/uk/')

    #================================
    #=========Heart 70s==============
    #================================
    elif station == "Heart 70" or station == "Heart 70s" or station == "heart 70" or station == "heart 70s":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.globalplayer.com/live/heart70s/uk/')

    #================================
    #=========Heart 80s==============
    #================================
    elif station == "Heart 80" or station == "Heart 80s" or station == "heart 80" or station == "heart 80s":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.globalplayer.com/live/heart80s/uk/')

    #================================
    #=========Heart 90s==============
    #================================
    elif station == "Heart 90" or station == "Heart 90s" or station == "heart 90" or station == "heart 90s":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.globalplayer.com/live/heart90s/uk/')


    #================================
    #=========Heart Dance============
    #================================
    elif station == "Heart Dance" or station == "Heart dance" or station == "heart dance" or station == "heart Dance":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.globalplayer.com/live/heartdance/uk')

    #================================
    #=========Capital FM=============
    #================================
    elif station == "Capital FM" or station == "Capital Fm" or station == "capital FM" or station == "capital fm"  or station == "Capital fm":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.globalplayer.com/live/capital/uk')

    #================================
    #=========Classical FM===========
    #================================
    elif station == "Classical FM" or station == "Classical Fm" or station == "classical FM" or station == "classical fm"  or station == "classical fm":
        time.sleep(1)
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(2)
        print("Found Station!")
        webbrowser.open('https://www.globalplayer.com/live/capital/uk')

    else:
        print("Finding station")
        time.sleep(1)
        print("Finding station.")
        time.sleep(1)
        print("Finding station..")
        time.sleep(1)
        print("Finding station...")
        time.sleep(1)
        print('Sorry we cannot find radio station. We will search the web for you!')
        time.sleep(2)
        webbrowser.open("https://google.com/search?q=%s" % station)

else:
    print("Sorry we have not added that yet :/ try again")
