## A simulated 3D plane with pygame

##---------Import necessary stuff---------**
import pygame
import math
import time
import random
import sys
##---------Set this to something fun---------**
#Screen height and width
SW = 1000
SH = 800
horisontalSteps = 2
verticalSteps = 99
speed = 2
##-------------------------------------------**

#Function for getting corresponding y value of x
def get_y_val(x, SH):
    mid = SH/2
    y = x + pow(x-mid,2)*0.5
    return(y)

#Define a screen
screen = pygame.display.set_mode((SW, SH))

#Set the frame count to 160 per second
pygame.time.Clock().tick(160)

#Create a list for the horizontal lines
def init_hor_lines(SW, SH, hor_step):
    horLineList = []
    hor_x = SH/2
    ySteps = 0
    while ySteps < SH:
        ySteps = get_y_val(hor_x, SH)
        horLineList.append(hor_x)
        hor_x += hor_step
    return(horLineList)

def get_LP(x):
    mitten = SW/2
    lowerPoint= x + 100000*math.sin(math.radians((x-mitten)/mitten))
    return(lowerPoint)

#Creating a list for the vertical lines
xList = []
for i in range(0,50):
    spread = SW/50*i
    xList.append(spread)

def init_house(SW,SH):
    houseList = []
    for x in range(-100,SW+100, 50+random.randint(0, 30)):
        pos = x
        width = random.randint(10,50)
        height = - random.randint(20,80)
        houseInst = [pos, width, height]
        houseList.append(houseInst)
    return(houseList)
##---------Init---------**
#Create a list for the horisontal lines and set up start
horLineList = init_hor_lines(SW, SH, horisontalSteps)
#Create a list of houses
houseList1 = init_house(SW, SH)
houseList2 = init_house(SW, SH)
houseList3 = init_house(SW, SH)
#For the polygon
x1 = -10
x2 = 10
#A constant for the sun
sun = 0.0001

##---------Starting a display loop---------**
while __name__=="__main__":
    #Render a black background
    screen.fill((int(sun*50),int(sun*50),int(sun*150)))
    #Draw a sun
    if sun < 1:
        sun += 0.0001
    pygame.draw.circle(screen, (int(sun*200),int(sun*200),int(sun*10)),(int(SW/2),int(SH/4)+int((SH/2)*(1-sun))), 100)
    pygame.draw.circle(screen, (255, 255, 255),(int(SW/2),int(SH/4)+int((SH/2)*(1-sun))), 100, 1)
    #Cover the ground with a filled rectangle
    pygame.draw.rect(screen, (int(sun*20),int(sun*60),int(sun*20)),(0,SH/2,SW, SH))
    #Draw some houses
    for h in houseList1:
        pygame.draw.rect(screen,(int(sun*200),int(sun*200),int(sun*200)),(h[0], SH/2, h[1], h[2]))
        pygame.draw.rect(screen,(int(sun*255),int(sun*255),int(sun*255)),(h[0], SH/2, h[1], h[2]),1)
    for h in houseList2:
        pygame.draw.rect(screen,(int(sun*160),int(sun*160),int(sun*160)),(h[0], SH/2, h[1], h[2]))
        pygame.draw.rect(screen,(int(sun*255),int(sun*255),int(sun*255)),(h[0], SH/2, h[1], h[2]),1)
    for h in houseList3:
        pygame.draw.rect(screen,(int(sun*50),int(sun*50),int(sun*50)),(h[0], SH/2, h[1], h[2]))
        pygame.draw.rect(screen,(int(sun*255),int(sun*255),int(sun*255)),(h[0], SH/2, h[1], h[2]),1)
    #Draw the vertical lines
    ##Start with the horizon
    pygame.draw.line(screen, (255,255,255),(0,SH/2),(SW,SH/2),1)
    #Draw the horizotal lines
    for line in horLineList:
        pygame.draw.line(screen, (255,255,255),(0,get_y_val(line, SH)),(SW,get_y_val(line, SH)),1)
    #Draw the horizontal lines
    for i in range(0,len(xList)):
        pygame.draw.line(screen,(255,255,255),(xList[i],SH/2),(get_LP(xList[i]),SH),1)
    #Draw a polygon
    x1 += 0.05*speed
    x2 += 0.05*speed
    pygame.draw.polygon(screen,(0,0,0),((x1,SH/2),(get_LP(x1),SH),(get_LP(x2),SH),(x2,SH/2)))
    pygame.draw.polygon(screen,(255,255,255),((x1,SH/2),(get_LP(x1),SH),(get_LP(x2),SH),(x2,SH/2)),1)
    #Flip the screen
    pygame.display.flip()
    
    #Add one to all instances of horLine
    for i in range(0,len(xList)):
        xList[i] += 0.05*speed
        if xList[i] > SW:
            del xList[i]
        if xList[0] >= SW/50:
            xList.insert(0,0)
    #Add one to all instances of the houselists
    for i in range(0,len(houseList1)):
        houseList1[i][0]+=0.03*speed
        if houseList1[i][0] > SW+100:
            houseList1[i][0] = -100
    for i in range(0,len(houseList2)):
        houseList2[i][0]+=0.04*speed
        if houseList2[i][0] > SW+100:
            houseList2[i][0] = -100
    for i in range(0,len(houseList3)):
        houseList3[i][0]+=0.05*speed
        if houseList3[i][0] > SW+100:
            houseList3[i][0] = -100
    
    #keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Escape will quit the program
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
