#Healthy Programmer
#Drink Water - 350 ml per 48 mins
#Eyes per - 30 mins
#Physical Activity - 45 mins
#No need to handle clash as it occurs after specified time period (at 12 hrs)

import pygame
import datetime
pygame.mixer.init()
start_time = datetime.datetime.now()
start_min = start_time.strftime("%M")

def give_dateandtime():
    x = datetime.datetime.now()
    return x.strftime("%c")

def drink_water():
    pygame.mixer.music.load("water.mp3")
    pygame.mixer.music.play(-1)
    Val = True
    while (Val):
        playback_stop = input("Enter keyword to stop music playback: ")
        required = playback_stop.capitalize()
        if required == "Drank":
            time = give_dateandtime()
            pygame.mixer.music.stop()
            Val = False
            return time
        else:
            print("Wrong Keyword.\n")

def eyes():
    pygame.mixer.music.load("eyes.mp3")
    pygame.mixer.music.play(-1)
    Val = True
    while (Val):
        playback_stop =input("Enter keyword to stop music playback: ")
        required = playback_stop.capitalize()
        if required == "Eydone":
            time = give_dateandtime()
            pygame.mixer.music.stop()
            Val = False
            return time
        else:
            print("Wrong keyword.\n")

def physical_activity():
    pygame.mixer.music.load("physical.mp3")
    pygame.mixer.music.play(-1)
    Val = True
    while (Val):
        playback_stop = input("Enter keyword to stop music playback: ")
        required = playback_stop.capitalize()
        if required == "Exdone":
            time = give_dateandtime()
            pygame.mixer.music.stop()
            Val = False
            return time
        else:
            print("Wrong keyword.\n")

f = open("Log.txt", "a")
end_time = start_time.strftime("%H")
while (int(end_time)<17):
    start_time = datetime.datetime.now()
    req_min = int(start_time.strftime("%S"))
    if req_min / 48 == 1:
        req_time = drink_water()
        f.writelines(["[", req_time, "] ", "Drank 350 ml water\n"])
        print("Information Logged")
    elif req_min / 30 == 1 or req_min == 0:
        req_time = eyes()
        f.writelines(["[", req_time, "] ", "Eye Exercise Done\n"])
        print("Information Logged")
    elif req_min / 45 == 1:
        req_time = physical_activity()
        f.writelines(["[", req_time, "] ", "Physical Activity Done\n"])
        print("Information Logged")
    end_time = start_time.strftime("%H")

f.close()
pygame.mixer.quit()