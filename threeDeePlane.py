## A simulated 3D plane with pygame

#Import pygame and math
import pygame
import math
import time
import random
import sys

### Start the program

#-----------Set this to something fun----------------#
#Screen height and width
screenWidth = 800
screenHeight = 600
#----------------------------------------------------#

#Function for getting corresponding y value of x
def get_y_val(x):
    mid = screenHeight/2
    y = x + pow(x-mid,2)*0.5
    return(y)

#Define a screen
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Set the frame count to 60 per second
pygame.time.Clock().tick(60)

#Create a list for the horizontal lines
global horLineList
horLineList = []
x = screenHeight/2
ySteps = 0
while ySteps < screenHeight:
    ySteps = get_y_val(x)
    horLineList.append(x)
    x += 2

def get_lowerPoint(x):
    mitten = screenWidth/2
    lowerPoint= x + 100000*math.sin(math.radians((x-mitten)/mitten))
    return(lowerPoint)

#Creating a list for the vertical lines
xList = []
for i in range(0,50):
    spread = screenWidth/50*i
    xList.append(spread)

#Creating a rectangle in correct perspective
    

#Starting a display loop
while __name__=="__main__":
    #Render a black background
    screen.fill((0,0,0))
    #Draw the vertical lines
    ##Start with the horizon
    pygame.draw.line(screen, (255,255,255),(0,screenHeight/2),(screenWidth,screenHeight/2),1)
    #Draw the horizotal lines
    for line in horLineList:
        pygame.draw.line(screen, (255,255,255),(0,get_y_val(line)),(screenWidth,get_y_val(line)),1)
    #Draw the horizontal lines
    for i in range(0,len(xList)):
        pygame.draw.line(screen,(255,255,255),(xList[i],screenHeight/2),(get_lowerPoint(xList[i]),screenHeight),1)
    #Flip the screen
    pygame.display.flip()
    #Add one to all instances of horLine
##    for i in range(0,len(horLineList)):
##        horLineList[i] += 0.005
##        if get_y_val(horLineList[i]) > screenHeight:
##            del horLineList[i]
##        if horLineList[0] >= 302:
##            horLineList.insert(0,screenHeight/2)

    #Add one to all instances of horLine
    for i in range(0,len(xList)):
        xList[i] += 0.05
        if xList[i] > screenWidth:
            del xList[i]
        if xList[0] >= screenWidth/50:
            xList.insert(0,0)
        

    #keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Escape will quit the program
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
