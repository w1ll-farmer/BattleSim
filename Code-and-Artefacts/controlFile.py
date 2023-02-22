import random #importing external modules used in program
import pygame
from time import sleep
from pygame.locals import *
#Importing modules coded in other files:
from userFile import user
from AI import fainted
from AI import switch
from AI import artificial
from superEffective import superEffective
from ineffective import ineffective
from affect import affect
from damageCalc import damageCalc
from theEnd import endCheck
from theEnd import gameOver
#globalised constants
global FPS
global framesPerSec
global black
global white
global window
global SCREEN_WIDTH
global SCREEN_HEIGHT
global red
#PYGAME - ignore for now
pygame.init()
red=[255,0,0] #creates Red
FPS=30 #sets FPS
framesPerSec=pygame.time.Clock()
black=[0,0,0] #creates black
white=[255,255,255] #creates white
window=pygame.display.set_mode((1200,800)) #create a 1200x800 window
pygame.display.set_caption('Battle Simulator') #titles the window
window.fill(black) #fills window with black
SCREEN_WIDTH,SCREEN_HEIGHT = pygame.display.get_surface().get_size()
#^^sets screen width and height
#END OF PYGAME
class Pokemon: #constructor and class creation
    def __init__(self,name,spAtk,atk,defence,spDef,spd,hp,move1,movetype1,movepower1,moveaccuracy1,movephys1,move2,movetype2,movepower2,moveaccuracy2,movephys2,move3,movetype3,movepower3,moveaccuracy3,movephys3,move4,movetype4,movepower4,moveaccuracy4,movephys4,type1,type2,level,userImage,opImage):
        self.level=level
        self.name=name
        self.spAtk=((2*spAtk*level)/100)+5
        self.atk=((2*atk*level)/100)+5
        self.spDef=((2*spDef*level)/100)+5
        self.defence=((2*defence*level)/100)+5
        self.spd=((2*spd*level)/100)+5
        self.hp = (2*(hp*level)/100)+level+10
        self.maxHP=self.hp
        self.move1=move1
        self.movetype1=movetype1
        self.movepower1=movepower1
        self.moveaccuracy1=moveaccuracy1 #forgot to add in original prototype
        self.movephys1=movephys1 #forgot to add in original prototype
        self.move2 = move2
        self.movetype2 = movetype2
        self.movepower2 = movepower2
        self.moveaccuracy2 = moveaccuracy2 #forgot to add in original prototype
        self.movephys2 = movephys2  # forgot to add in original prototype
        self.move3 = move3 #was originally a repeat of move2
        self.movetype3 = movetype3
        self.movepower3 = movepower3
        self.moveaccuracy3 = moveaccuracy3 #forgot to add in original prototype
        self.movephys3 = movephys3  # forgot to add in original prototype
        self.move4 = move4
        self.movetype4 = movetype4
        self.movepower4 = movepower4
        self.moveaccuracy4 = moveaccuracy4 #forgot to add in original prototype
        self.movephys4 = movephys4  # forgot to add in original prototype
        self.type1=type1
        self.type2=type2
        self.userImage=pygame.image.load(userImage) #User image
        self.opImage=pygame.image.load(opImage) #User image

    def drawUser(self, surface,x,y): #Draws User Sprite
        surface.blit(self.userImage,(x,y))
    def drawOp(self,surface,x,y): #Draws Opponent Sprite
        surface.blit(self.opImage,(x,y))

class Trainer: #creates the trainer
    def __init__(self,userImage,introImage,x,y,name):
        self.name=name #sets their name
        super().__init__()
        self.userImage=pygame.image.load(userImage) #loads their user sprite
        self.introImage=pygame.image.load(introImage) #loads their intro sprite
        self.rect = self.userImage.get_rect(center = (x,y)) #creates a rectangle
        #around them so they can be clicked
    def drawUser(self, surface): #draws user sprite
        surface.blit(self.userImage,self.rect)
    def drawIntro(self, surface): #draws opponent/intro sprite
        surface.blit(self.introImage, self.rect)
    def move(self,surface,x,y): #moves them
        self.rect=self.introImage.get_rect(center = (x,y))

class Background: #creates a background
    def __init__(self,backgroundImage):
        super().__init__()
        self.backgroundImage=pygame.image.load(backgroundImage)
        #^^ sets background to passed in image
        self.backgroundRect=self.backgroundImage.get_rect()
        #^^ creates a rectangle around it  for co-ordinates
        self.backgroundX1 = 0 #sets X co-ordinates
        self.backgroundX2 = 0

        self.backgroundY1 = 0 #sets Y co-ordinates
        self.backgroundY2 = -self.backgroundRect.height
    def render(self): #Renders in the background
        window.blit(self.backgroundImage, (self.backgroundX1, self.backgroundY1))
        window.blit(self.backgroundImage, (self.backgroundX2, self.backgroundY2))
    def update(self,backgroundImage): #Updates the background image
        self.backgroundImage = pygame.image.load(backgroundImage)
        self.backgroundRect = self.backgroundImage.get_rect()
class Box: #Creates the class for boxes
    def __init__(self, height, width, centre,border,colour):
        self.font = pygame.font.SysFont('Calibri',20) #Sets font size and type
        if border == 2: #if a border to a box
            self.rect = pygame.draw.rect(window,colour,pygame.Rect(centre[0],centre[1],height,width),border)
        else: #if an actual box
            self.rect = pygame.draw.rect(window,colour,pygame.Rect(centre[0],centre[1],height,width))
    def addText(self,window,text): #adds text to the box
        window.blit(self.font.render(text,True,red),self.rect)
backgroundImage='resizedblackscreen.jpeg' #sets background image
background=Background(backgroundImage) #instantiates background object
#instantiating Red's Pokemon
mewtwo=Pokemon('Mewtwo',154,110,90,90,130,106,'Psystrike','Psychic',100,100,'special','Aura Sphere','Fighting',85,101,'special','Shadow Ball','Ghost',80,100,'special','Earthquake','Ground',100,100,'physical','Psychic','empty',100,'userMewtwo.png','AIMewtwo.png')
snorlax=Pokemon('Snorlax',65,110,65,110,30,160,'Body Slam','Normal',85,100,'physical','High Horsepower','Ground',90,90,'physical','Hammer Arm','Fighting',100,85,'physical','Giga Impact','Normal',150,50,'physical','Normal','empty',100,'userSnorlax.png','AISnorlax.png')
pikachu=Pokemon('Pikachu',100,110,40,55,90,35,'Thunderbolt','Electric',95,100,'special','Iron Tail','Steel',100,75,'physical','Quick Attack','Normal',40,100,'physical','Volt Tackle','Electric',120,87.5,'physical','Electric','empty',100,'userPikachu.png','AIPikachu.png')
charizard=Pokemon('Charizard',109,84,78,85,100,78,'Flare Blitz','Fire',120,75,'physical','Air Slash','Flying',75,95,'special','Dragon Claw','Dragon',80,100,'physical','Dual Wingbeat','Flying',80,90,'physical','Fire','Flying',100,'userCharizard.png','AICharizard.png')
blastoise=Pokemon('Blastoise',85,83,100,105,78,79,'Surf','Water',95,100,'special','Ice Beam','Ice',95,100,'special','Flash Cannon','Steel',80,100,'special','Aura Sphere','Fighting',85,100,'special','Water','empty',100,'userBlastoise.png','AIBlastoise.png')
venusaur=Pokemon('Venusaur',100,82,83,100,80,80,'Petal Blizzard','Grass',90,100,'physical','Double Edge','Normal',120,87.5,'physical','Sludge Bomb','Poison',90,100,'special','Earth Power','Ground',90,100,'special','Grass','Poison',100,'userVenusaur.png','AIVenusaur.png')
redX,redY = 500,300
blueX,blueY = 750,300
red=Trainer('userRed.png','resizedIntroRed.png',redX,redY,'Red') #Instantiating Red
#Instantiating Blue's Pokemon
machamp=Pokemon('Machamp',65,130,80,85,55,90,'Cross Chop','Fighting',100,80,'physical','Dual Chop','Dragon',80,90,'physical','Strength','Normal',80,100,'physical','Knock Off','Dark',80,100,'physical','Fighting','empty',100,'userMachamp.png','AIMachamp.png')
pidgeot=Pokemon('Pidgeot',70,80,75,70,101,83,'Hurricane','Flying',110,70,'special','Quick Attack','Normal',40,100,'physical','Double Edge','Normal',120,87.5,'physical','Steel Wing','Steel',70,100,'physical','Flying','Normal',100,'userPidgeot.png','AIPidgeot.png')
exeggutor=Pokemon('Exeggutor',125,95,85,65,55,95,'Wood Hammer','Grass',120,80,'physical','Extrasensory','Psychic',80,100,'special','Stomp','Normal',65,100,'physical','Grassy Glide','Grass',70,100,'physical','Grass','Psychic',100,'userExeggutor.png','AIExeggutor.png')
gyarados=Pokemon('Gyarados',60,125,79,100,81,95,'Aqua Tail','Water',90,90,'physical','Earthquake','Ground',100,100,'physical','Bounce','Flying',85,85,'physical','Crunch','Dark',80,100,'physical','Water','Flying',100,'userGyarados.png','AIGyarados.png')
rhydon=Pokemon('Rhydon',45,130,120,45,40,105,'Earthquake','Ground',100,100,'physical','Stone Edge','Rock',100,80,'physical','Rock Slide','Rock',75,90,'physical','Megahorn','Bug',120,85,'physical','Rock','Ground',100,'userRhydon.png','AIRhydon.png')
arcanine=Pokemon('Arcanine',100,110,80,80,95,90,'Flare Blitz','Fire',120,75,'physical','Outrage','Dragon',120,75,'physical','Extreme Speed','Normal',80,100,'physical','Flamethrower','Fire',95,100,'special','Fire','empty',100,'userArcanine.png','AIArcanine.png')

blue=Trainer('userBlue.png','IntroBlue.png',blueX,blueY,'Blue')
redPok=[pikachu,mewtwo,snorlax,charizard,blastoise,venusaur] #making it easier for rest of program
bluePok=[pidgeot,machamp,exeggutor,gyarados,rhydon,arcanine] #making it easier for rest of program

def trainerSelect(redPok,bluePok,red,blue): #the user selects the trainer
    clicked=False
    while not clicked: #loops until a trainer is clicked
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() #Quits game if exit button pressed
            if event.type == MOUSEBUTTONDOWN: #if mouse click registered
                pos=pygame.mouse.get_pos() #get position of mouse click
                if blue.rect.collidepoint(pos): #if it collides with blue
                    trainer='Blue'
                    clicked=True
                if red.rect.collidepoint(pos): #if it collides with red
                    trainer='Red'
                    clicked=True

    print("You have chosen Trainer",trainer) #confirmation
    opTrainer=red #For use of display
    userTrainer=blue
    if trainer=='Red':
        userPok=redPok #will make it easier to use later on in program
        opPok=bluePok
        opTrainer=blue
        userTrainer=red
    else:
        userPok=bluePok #will make it easier to use later in program
        opPok=redPok #No need to assign opTrainer or userTrainer as pre-defined

    pygame.display.update() #updates display
    framesPerSec.tick(FPS)
    background.render() #hide the unwanted
    userTrainer.move(window, 600, 300) #moves users trainer to desired location
    userTrainer.drawIntro(window) #Draws the user's trainer
    for i in range(0,len(userPok)):
        userPok[i].drawOp(window,100*i, 100*i) #Displays team diagonally
    pygame.display.update() #updates display
    framesPerSec.tick(30)
    return userTrainer,opTrainer, opPok,userPok
#DIFFICULTY SETTINGS

#Display trainers

red.drawIntro(window) #Draws the trainers
blue.drawIntro(window)
#Display Red's team
mewtwo.drawOp(window, 400, 400)
snorlax.drawOp(window, 400, 300)
pikachu.drawOp(window, 400, 200)
charizard.drawOp(window, 300, 400)
venusaur.drawOp(window, 300, 300)
blastoise.drawOp(window, 300, 200)
#Display Blue's team
machamp.drawOp(window, 850, 400)
pidgeot.drawOp(window, 850, 300)
exeggutor.drawOp(window, 850, 200)
gyarados.drawOp(window, 950, 400)
rhydon.drawOp(window, 950, 300)
arcanine.drawOp(window, 950, 200)
initiallyRunning=True
while initiallyRunning: #Runs until all necessary variables to proper loop have
                        #been created
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()
    framesPerSec.tick(30)

    userTrainer,opTrainer,opPok,userPok=trainerSelect(redPok,bluePok,red,blue) #allows user to choose trainer
    sleep(2)
    opFaintCount,userFaintCount=0,0 #No pokemon have fainted yet
    opMove,opAcc,opOutPok=artificial(opPok[0],opPok,userPok[0]) #gets the AI to make a decision
    background.update('battlescene.png') #new background image
    background.render() #renders new background image
    opTrainer.move(window, 900,300) #moves to new location
    opTrainer.drawIntro(window) #displays
    opPok[0].drawOp(window, 900,250)
    userTrainer.move(window, 450, 550)
    userTrainer.drawUser(window) #corrected
    userPok[0].drawUser(window, 500,500)
    pygame.display.update()
    framesPerSec.tick(30)
    userPok,userOutPok,opOutPok=user(userPok,userPok[0],opOutPok,opMove,opAcc,opPok,userTrainer,opTrainer) #gets user to make decision
    initiallyRunning=False #ends loop



while userFaintCount < 6 and opFaintCount < 6:
    # RESET BACKGROUND
    background = Background('battlescene.png')
    background.render()
    narrativeBox = Box(500, 500, (400, 585), 1, white)
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
    opTrainer.move(window, 900, 300)
    opTrainer.drawIntro(window)
    #opOutPok.drawOp(window, 900, 250)
    userTrainer.move(window, 450, 550)
    userTrainer.drawUser(window)  # corrected
    userOutPok.drawUser(window, 500, 500)
    pygame.display.update()
    opMove,opAcc,opOutPok=artificial(opOutPok,opPok,userOutPok) #AI makes decision first to ensure the user's
    #decision has no influence (i.e. if the user switches battler)
    userPok,userOutPok,opOutPok=user(userPok,userOutPok,opOutPok,opMove,opAcc,opPok,userTrainer,opTrainer) #user makes decision
    opFaintCount,userFaintCount=endCheck(opPok,userPok) #check how many battlers
                                                        #have fainted
    pygame.display.update()
    framesPerSec.tick(FPS)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()


gameOver(userFaintCount,background) #Ends the game
