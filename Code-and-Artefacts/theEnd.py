from AI import fainted
from time import sleep
import pygame
from pygame.locals import *
global black
global window
global white
global red
white=[255,255,255] #sets constant white to colour white
window=pygame.display.set_mode((1200,800)) #creates pygame window
black=[0,0,0] #sets constant black to colour black
red=[255,0,0] #sets constant red to colour red
class Box:
    def __init__(self, height, width, centre,border,colour):
        self.font = pygame.font.SysFont('Calibri',20)
        if border == 2:
            self.rect = pygame.draw.rect(window,colour,pygame.Rect(centre[0],centre[1],height,width),border)
        else:
            self.rect = pygame.draw.rect(window,colour,pygame.Rect(centre[0],centre[1],height,width))
    def addText(self,window,text):
        window.blit(self.font.render(text,True,red),self.rect)
class Background:
    def __init__(self,backgroundImage):
        super().__init__()
        self.backgroundImage=pygame.image.load(backgroundImage)
        self.backgroundRect=self.backgroundImage.get_rect()

        self.backgroundX1 = 0
        self.backgroundX2 = 0

        self.backgroundY1 = 0
        self.backgroundY2 = -self.backgroundRect.height
    def render(self):
        window.blit(self.backgroundImage, (self.backgroundX1, self.backgroundY1))
        window.blit(self.backgroundImage, (self.backgroundX2, self.backgroundY2))
    def update(self,backgroundImage):
        self.backgroundImage = pygame.image.load(backgroundImage)
        self.backgroundRect = self.backgroundImage.get_rect()

def endCheck(opPok,userPok):
    opFaintCount=int(0) #sets the number of fainted battlers
    userFaintCount=int(0) #to 0 for both teams
    for x in range(0,6):
        if fainted(opPok[x]) == True:
            opFaintCount += 1 #calculates number of fainted
        if fainted(userPok[x]) == True:
            userFaintCount += 1
    return opFaintCount,userFaintCount #returns the value to
                                    #be the condition of the while loop
                                    #that stops the game

def gameOver(userFaintCount,background):
    window.fill(black) #fill screen with black
    #update background
    background.update('resizedblackscreen.jpeg')
    background.render()
    #output message
    message = Box(400, 400, (550, 350), 1, black)
    message.addText(window, 'GAME OVER')
    #new message dependent on result
    newMessage = Box(400, 400, (475, 400), 1, black)
    if userFaintCount < 6:
        #if user wins
        newMessage.addText(window, 'Congratulations for beating the opponent!')
    else: #if user loses
        newMessage.addText(window, 'Unlucky! The opponent bested you!')
    while True: #loops until user quits
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit() #game ends

