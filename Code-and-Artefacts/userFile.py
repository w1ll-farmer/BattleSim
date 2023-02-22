from time import sleep #used to allow users to read in time
from AI import fainted #importing modules from other files
from damageCalc import damageCalc
from AI import accuracyCheck
from theEnd import endCheck
import pygame #globalised constants
global window
global black
global white
global red
global grey
global green
#sets colours
green = [0,255,0]
grey = [132,132,132]
red = [255,0,0]
white = [255,255,255]
black = [0,0,0]
from pygame.locals import *
window=pygame.display.set_mode((1200,800))
framesPerSec=pygame.time.Clock()
FPS=30

class Trainer: #Copied from main file
    def __init__(self,userImage,introImage,x,y,name):
        self.name=name
        super().__init__()
        self.userImage=pygame.image.load(userImage)
        self.introImage=pygame.image.load(introImage)
        self.rect = self.userImage.get_rect(center = (x,y))
    def drawUser(self, surface):
        surface.blit(self.userImage,self.rect)
    def drawIntro(self, surface):
        surface.blit(self.introImage, self.rect)
    def move(self,surface,x,y):
        self.rect=self.introImage.get_rect(center = (x,y))
class Background: #copied from main file
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
class Button: #Same as box but takes on an image instead of a colour
    def __init__(self,image,x,y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = (x,y))
    def move(self,window,x,y): #moves Button
        self.rect=self.image.get_rect(center=(x,y))
    def draw(self,window): #displays Button
        window.blit(self.image,self.rect)
class Box:
    def __init__(self, height, width, centre,border,colour):
        self.font = pygame.font.SysFont('Calibri',20)
        if border == 2:
            self.rect = pygame.draw.rect(window,colour,pygame.Rect(centre[0],centre[1],height,width),border)
        else:
            self.rect = pygame.draw.rect(window,colour,pygame.Rect(centre[0],centre[1],height,width))
    def addText(self,window,text):
        window.blit(self.font.render(text,True,red),self.rect)
def user(userPok,userOutPok,opOutPok,opMove,opAcc,opPok,userTrainer,opTrainer):
    #OPPONENT HEALTH
    opHealthPerCent = opOutPok.hp/opOutPok.maxHP #for width of health bar
    opHealthBox=Box(250,100,(950,0),1,grey) #Creates opponent box
    border = Box(251,101,(950,0),2,black) #creates the border
    opHealthBox.addText(window," "+opOutPok.name+" lvl"+str(opOutPok.level)+" HP: "+str(int(opOutPok.hp)))
    #^^Adds name, level and HP to health box
    opHealthBar = Box(200*opHealthPerCent,20,(975,50),1,green) #creates health bar
    border=Box(201,20,(975,50),2,black) #creates border around health bar
                                        #so the user can see % of health
    #USER HEALTH - adapted from above
    userHealthPerCent = userOutPok.hp / userOutPok.maxHP #for width of health bar
    userHealthBox=Box(250,100,(0,600),1,grey)
    border = Box(251,101,(0,600),2,black)
    userHealthBox.addText(window," "+userOutPok.name + " lvl" + str(userOutPok.level)+" HP: "+str(int(userOutPok.hp)))
    userHealthBar = Box(200*userHealthPerCent, 20, (25, 650), 1, green)
    border = Box(201, 20, (25, 650), 2, black)
    #MAKING BUTTONS
    fight = Button('fightbutton.png', 1130,500) #Creates fight button
    fight.draw(window) #Displays fight button
    pygame.display.update() #updates display
    pkmn = Button('pkmn.png',1160,535) #Creates pokemon button
    pkmn.draw(window) #displays it
    pygame.display.update() #updates display
    bag= Button('bagIMG.png',1170,561) #Creates bag button
    bag.draw(window) #displays it
    pygame.display.update() #updates display
    narrativeBox = Box(500, 500, (400, 585), 1, white) #creates narrative box
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black) #creates border
                                                            #around it
    narrativeBox.addText(window,"What will you do?") #adds text to narrative box
    pygame.display.update() #updates display
    framesPerSec.tick(30)
    choice='switch' #pre-defines choice to 'switch'
    clicked=False #Boolean as either clicked or not clicked
    while not clicked: #loops until a button has been clicked
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN: #if mouse clicked detected
                pos=pygame.mouse.get_pos() #Gets position of mouse
                if fight.rect.collidepoint(pos): #if fight button clicked
                    choice = 'fight' #Sets choice to fight for later
                    clicked=True #breaks out of loop
                    #No ELSE statement as game waits until input received
                if bag.rect.collidepoint(pos):
                    if userPok[0].hp == userPok[0].maxHP and userPok[1].hp == userPok[1].maxHP and userPok[2].hp == userPok[2].maxHP and userPok[3].hp == userPok[3].maxHP and userPok[4].hp == userPok[4].maxHP and userPok[5].hp == userPok[5].maxHP:
                        #^^If item cannot be validly applied
                        narrativeBox = Box(500, 500, (400, 585), 1, white)
                        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
                        narrativeBox.addText(window,' No items can be applied')
                    else:
                        #Sets choice to bag and clicked to true to break out of loop
                        choice = 'bag'
                        clicked=True
                if pkmn.rect.collidepoint(pos): #if pokemon button clicked
                    if pkmnValid(userPok,userOutPok) is True: #if valid
                        clicked=True #break out of loop
                    else:
                        narrativeBox = Box(500, 500, (400, 585), 1, white)
                        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
                        narrativeBox.addText(window, ' You have no more battlers left')
                        #^^Output that no more battlers are remaining to switch to
        pygame.display.update()
    if choice == 'fight': #battle sequence
        narrativeBox = Box(500, 500, (400, 585), 1, white)
        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
        narrativeBox.addText(window, ' What move will you choose?')
        #^Outputs to narrative box
        pygame.display.update()
        #Creation of a button for each move
        move1button = Box(172, 40, (1044, 450), 1, black)
        move1buttonborder = Box(172,40,(1042,450),2,white)
        move1button.addText(window,userOutPok.move1)
        #Next move
        move2button = Box(172, 40, (1044, 490), 1, black)
        move2buttonborder = Box(172, 40, (1042, 490), 2, white)
        move2button.addText(window, userOutPok.move2)
        pygame.display.update()
        #Next move
        move3button = Box(172, 40, (1043, 530), 1, black)
        move3buttonborder = Box(172, 40, (1042, 530), 2, white)
        move3button.addText(window, userOutPok.move3)
        pygame.display.update()
        #Next move
        move4button = Box(172, 40, (1043, 570), 1, black)
        move4buttonborder = Box(172, 40, (1042, 570), 2, white)
        move4button.addText(window, userOutPok.move4)
        pygame.display.update()
        framesPerSec.tick(30)
        clicked=False
        userMove=userOutPok.move4 #define userMove
        while not clicked: #keep running until user clicks
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.QUIT()
                if event.type == MOUSEBUTTONDOWN: #When click detected
                    pos=pygame.mouse.get_pos() #get coords of click
                    if move1button.rect.collidepoint(pos):
                        userMove=userOutPok.move1 #set move to move1
                        clicked=True
                    if move2button.rect.collidepoint(pos):
                        userMove=userOutPok.move2 #move to move2
                        clicked=True
                    if move3button.rect.collidepoint(pos):
                        userMove=userOutPok.move3 #move to move3
                        clicked=True
                    if move4button.rect.collidepoint(pos):
                        clicked=True #move to move 4
                                 #this is default bcs of pre-define
        userDamage,crit,moveAcc=damageCalc(opOutPok, userOutPok, userMove) #calcs damage
        opOutPok,userOutPok=moveOrder(opOutPok,opMove,opAcc,userOutPok,userDamage,userMove,crit,moveAcc)
        #^Determines order
    elif choice == 'bag': #If bag clicked
        userPok = useBag(userPok,userTrainer,opTrainer,opOutPok,userOutPok) #returns info about pokemon
        userOutPok = opInflict(opOutPok, opMove, opAcc, userOutPok) #opponent inflicts damage
    else: #If pokemon button clicked
        userOutPok = switchUser(userOutPok,userPok,userTrainer,opTrainer,opOutPok) #allows user to switch pokemon
        userOutPok=opInflict(opOutPok,opMove,opAcc,userOutPok) #opponent inflicts damage


    if fainted(userOutPok) == True: #if current battler fainted
        if endCheck(opPok,userPok)[1] != 6: #check if any left
            userOutPok=switchUser(userOutPok,userPok,userTrainer,opTrainer,opOutPok)
            #user MUST switch as battler is fainted
    return userPok,userOutPok,opOutPok #returns the current battler

def useBag(userPok, userTrainer,opTrainer,opOutPok,userOutPok): #BAG FUNCTION
    possibleItems=['Max Potion','Super Potion','Revive','Hyper Potion'] #available items
    #Creation of item 1 Box
    item1 = Box(172, 40, (1043, 570), 1, black)
    item1border = Box(172, 40, (1042, 570), 2, white)
    item1Text=possibleItems[3]
    item1.addText(window, item1Text)

    pygame.display.update()
    #Creation of item 2 Box
    item2 = Box(172, 40, (1043, 530), 1, black)
    item2border = Box(172, 40, (1042, 530), 2, white)
    item2Text=possibleItems[2]
    item2.addText(window, item2Text)
    pygame.display.update()
    #Creation of item 3 Box
    item3 = Box(172, 40, (1043, 490), 1, black)
    item3border = Box(172, 40, (1042, 490), 2, white)
    item3Text=possibleItems[1]
    item3.addText(window, item3Text)
    pygame.display.update()
    #Creation of item 4 Box
    item4 = Box(172, 40, (1043, 450), 1, black)
    item4border = Box(172, 40, (1042, 450), 2, white)
    item4Text=possibleItems[0]
    item4.addText(window, item4Text)
    pygame.display.update()
    clicked=False
    chosenItem=item4Text
    while not clicked: #Until a Box is clicked
        narrativeBox = Box(500, 500, (400, 585), 1, white)
        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
        narrativeBox.addText(window,"Which item do you want to apply?")
        pygame.display.update() #update display
        for event in pygame.event.get():
            if event.type == QUIT: #close window if exit button clicked
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN: #detects mouse click
                pos = pygame.mouse.get_pos() #gets coords of click
                if item1.rect.collidepoint(pos): #if item1 is clicked
                    if potionValid(userPok) is True: #if can be validly applied
                        chosenItem=item1Text
                        clicked=True
                    else: #displays message saying this is invalid
                        narrativeBox = Box(500, 500, (400, 585), 1, white)
                        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
                        narrativeBox.addText(window, "This item cannot be applied to any of your pokemon")

                if item2.rect.collidepoint(pos):
                    if reviveValid(userPok) is True:
                        chosenItem=item2Text
                        clicked=True
                    else:
                        narrativeBox = Box(500, 500, (400, 585), 1, white)
                        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
                        narrativeBox.addText(window, "This item cannot be applied to any of your pokemon")

                if item3.rect.collidepoint(pos):
                    if potionValid(userPok) is True:
                        chosenItem=item3Text
                        clicked=True
                    else:
                        narrativeBox = Box(500, 500, (400, 585), 1, white)
                        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
                        narrativeBox.addText(window, "This item cannot be applied to any of your pokemon")

                if item4.rect.collidepoint(pos):
                    if potionValid(userPok) is True:
                        clicked=True #pre-defined as item 4
                    else:
                        narrativeBox = Box(500, 500, (400, 585), 1, white)
                        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
                        narrativeBox.addText(window, "This item cannot be applied to any of your pokemon")

        pygame.display.update()
        sleep(1) #slight pause
    #RESET BACKGROUND
    background=Background('battlescene.png')
    background.render()
    narrativeBox = Box(500, 500, (400, 585), 1, white)
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
    opTrainer.move(window, 900, 300)
    opTrainer.drawIntro(window)
    opOutPok.drawOp(window, 900, 250)
    userTrainer.move(window, 450, 550)
    userTrainer.drawUser(window)  # corrected
    userOutPok.drawUser(window, 500, 500)
    pygame.display.update()

    narrativeBox.addText(window, "What pokemon do you want to apply this item to?")
    # prompts the user to select which pokemon they want to use the item on
    pygame.display.update()
    validPokemon=[]
    if chosenItem==item1Text or chosenItem ==item3Text or chosenItem == item4Text:
        #^^if potion
        for i in range(0,len(userPok)): #all pokemon
            if userPok[i].hp < userPok[i].maxHP and fainted(userPok[i]) is False:
                validPokemon.append(userPok[i]) #adds to list if valid
    else: #if revive
        for i in range(0,len(userPok)):
            if fainted(userPok[i]) is True: #if fainted (and therefore valid)
                validPokemon.append(userPok[i])
    boxes = ['','' ,'' ,'' ,'' ,'' ] #empty list of set length be changed in loop
    displayedBoxes=[] #stores which boxes are stored
    displayedBoxesObj=[] #stores the object that each box maps to
    for i in range(0,len(validPokemon)): #displays a box for each valid pokemon
        boxes[i] = Box(172,40, (1043,410+(i*40)),1,black)
        itemBorder = Box(172, 40, (1042, 410+(i*40)), 2, white)
        boxes[i].addText(window,validPokemon[i].name) #adds name of battler to box
        displayedBoxes.append(boxes[i]) #adds displayed box to the list
        displayedBoxesObj.append(validPokemon[i]) #adds object that maps to
                                                  #displayed box
        pygame.display.update()
    clicked=False
    while not clicked: #loops until clicked
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() #quits if exit button pressed
            if event.type == MOUSEBUTTONDOWN: #if mouse clicked
                pos=pygame.mouse.get_pos() #gets coords of mouse click
                for i in range(0,len(displayedBoxes)): #if box clicked
                    if displayedBoxes[i].rect.collidepoint(pos):
                        chosenPokemon=displayedBoxesObj[i] #set chosen to clicked
                        clicked=True #breaks
    narrativeBox = Box(500, 500, (400, 585), 1, white)
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
    narrativeBox.addText(window, 'You chose to apply '+chosenItem+' to '+chosenPokemon.name)
    #^^Outputs which item was chosen and which pokemon it was applied to
    pygame.display.update() #updates display
    if chosenItem == 'Super Potion': #applies effect of super potion
        if chosenPokemon.maxHP <= chosenPokemon.hp + 50:
            chosenPokemon.hp=chosenPokemon.maxHP
        else:
            chosenPokemon.hp+=50
    elif chosenItem == 'Max Potion': #applies effect of max potion
        chosenPokemon.hp = chosenPokemon.maxHP
    elif chosenItem == 'Hyper Potion': #applies effect of hyper potion
        if chosenPokemon.maxHP <= chosenPokemon.hp + 120:
            chosenPokemon.hp=chosenPokemon.maxHP
        else:
            chosenPokemon.hp+=120
    else:
        chosenPokemon.hp = chosenPokemon.maxHP//2 #sets fainted pokemon HP to half
    sleep(1.5) #brief pause
    narrativeBox = Box(500, 500, (400, 585), 1, white)
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
    narrativeBox.addText(window, 'Your '+chosenPokemon.name+' now has '+str(int(chosenPokemon.hp))+' HP')
    #^^Outputs new HP of pokemon who had item applied to them
    pygame.display.update()
    return userPok #returns updated attributes of user's battlers


def moveOrder(opOutPok,opMove,opAcc,userOutPok,userDamage,userMove,crit,userAcc):
    priorityMoves=['quick attack','extreme speed'] #for priority checking

    pygame.display.update()
    if priorityCheck(userMove,opMove,priorityMoves,opOutPok.spd,userOutPok.spd):
        #^^checks which battler goes first
        opOutPok=userInflict(userOutPok,userDamage,userMove,userAcc,opOutPok,crit)
        #^^Inflicts damage upon opponent
        if fainted(opOutPok)==False: #see if the user can choose a move
            sleep(1)
            userOutPok=opInflict(opOutPok,opMove,opAcc,userOutPok)
            #^^opponent inflicts damage
    else:
        userOutPok=opInflict(opOutPok,opMove,opAcc,userOutPok) #effectively the same as above but inverted
        if fainted(userOutPok)==False: #If not fainted, use a move
            sleep(1)
            opOutPok=userInflict(userOutPok,userDamage,userMove,userAcc,opOutPok,crit)

    return opOutPok,userOutPok #returns updated attributes for current battlers

def switchUser(userOutPok,userPok,userTrainer,opTrainer,opOutPok):
    # RESET BACKGROUND
    background = Background('battlescene.png')
    background.render()
    narrativeBox = Box(500, 500, (400, 585), 1, white)
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
    opTrainer.move(window, 900, 300)
    opTrainer.drawIntro(window)
    opOutPok.drawOp(window, 900, 250)
    userTrainer.move(window, 450, 550)
    userTrainer.drawUser(window)  # corrected
    userOutPok.drawUser(window, 500, 500)
    pygame.display.update()

    unfainted=[]
    names=[] #to differentiate
    for i in userPok:
        if i.hp > 0 and i.name!=userOutPok.name: #modified
            unfainted.append(i)
        if i.name !=userOutPok.name: #added to differentiate
            names.append(i.name) #added
    narrativeBox.addText(window, 'Who do you want to switch in?')
    boxes=[] #Keeps track of which pokemon's name have been displayed
    boxObj=[] #stores pokemon that each box maps to
    for i in range(0,len(unfainted)):
        boxes.append(Box(172, 40, (1043, 410 + (i * 40)), 1, black))
        #Creates a box for each pokemon that can be switched to
        itemBorder = Box(172, 40, (1042, 410 + (i * 40)), 2, white)
        #^Creates border for each box
        boxes[i].addText(window, unfainted[i].name)
        #^Adds pokemon's name to each box
        boxObj.append(unfainted[i]) #assigns battler that is mapped to box
        pygame.display.update()
    chosenPokemon='' #Creates a variable to store pokemon that is to be switched to
    clicked=False
    while not clicked:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN: #If click detected
                pos=pygame.mouse.get_pos() #gets position of click
                for i in range(0,len(boxes)): #if box clicked
                    if boxes[i].rect.collidepoint(pos):
                        chosenPokemon=boxObj[i] #assign pokemon of box to chosen
                        clicked=True
    narrativeBox = Box(500, 500, (400, 585), 1, white)
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
    narrativeBox.addText(window, 'You sent out '+chosenPokemon.name)
    #^^Outputs which pokemon has been sent out
    pygame.display.update()
    sleep(0.5) #slight pause
    userOutPok=chosenPokemon #updates userOutPok
    # RESET BACKGROUND
    background = Background('battlescene.png')
    background.render()
    narrativeBox = Box(500, 500, (400, 585), 1, white)
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
    narrativeBox.addText(window,"You sent out "+userOutPok.name)
    opTrainer.move(window, 900, 300)
    opTrainer.drawIntro(window)
    opOutPok.drawOp(window, 900, 250)
    userTrainer.move(window, 450, 550)
    userTrainer.drawUser(window)  # corrected
    userOutPok.drawUser(window, 500, 500)
    pygame.display.update()
    sleep(1)
    return userOutPok #returns new battler


def userInflict(userOutPok,userDamage,userMove,userAcc,opOutPok,crit): #inflicts damage on opp
    narrativeBox = Box(500, 500, (400, 585), 1, white)  # redraw
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)  # border
    narrativeBox.addText(window, userOutPok.name.upper() + ' used ' + userMove)
    #^^narrate
    pygame.display.update()
    sleep(1.5) #slight pause
    if accuracyCheck(userAcc) == False: #if attack hits target
        narrativeBox = Box(500, 500, (400, 585), 1, white)
        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
        narrativeBox.addText(window, 'It did ' + str(userDamage) + ' damage!')
        pygame.display.update() #Outputs damage
        sleep(1) #slight pause
        if crit == True: #if a critical hit, output message saying so
            narrativeBox = Box(500, 500, (400, 585), 1, white)
            narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
            narrativeBox.addText(window, "It's a critical hit!")
            pygame.display.update()
        opOutPok.hp -= userDamage #subtracts inflicted damage from health
        if opOutPok.hp < 0:
            opOutPok.hp = 0 #sets HP to zero if less than zero for output of HP box
        opHealthPerCent = opOutPok.hp / opOutPok.maxHP
        opHealthBox = Box(250, 100, (950, 0), 1, grey)
        border = Box(251, 101, (950, 0), 2, black)
        opHealthBox.addText(window," " + opOutPok.name + " lvl" + str(opOutPok.level) + " HP: " + str(int(opOutPok.hp)))
        opHealthBar = Box(200 * opHealthPerCent, 20, (975, 50), 1, green)
        border = Box(201, 20, (975, 50), 2, black)
        pygame.display.update()
    else:
        narrativeBox = Box(500, 500, (400, 585), 1, white)
        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
        narrativeBox.addText(window, "The attack missed!")
        pygame.display.update()
    sleep(1)
    return opOutPok #returns updated attributes of current opponent battler

def opInflict(opOutPok,opMove,opAcc,userOutPok): #inflicts damage on user
    narrativeBox = Box(500, 500, (400, 585), 1, white) #redraw
    narrativeBoxBorder = Box(500, 500, (400, 585), 2, black) #border
    narrativeBox.addText(window,opOutPok.name.upper()+' used '+opMove) #narrate
    pygame.display.update()
    sleep(1.5)

    opDamage,opCrit,opAcc=damageCalc(userOutPok,opOutPok,opMove) #gets op's damage
    if accuracyCheck(opAcc)==False: #if hits target
        narrativeBox = Box(500, 500, (400, 585), 1, white)
        narrativeBoxBorder = Box(500,500, (400,585), 2, black)
        narrativeBox.addText(window,'It did '+str(opDamage)+' damage!')
        #^^Output damage
        pygame.display.update()
        sleep(1)
        if opCrit==True: #if critical hit
            narrativeBox = Box(500, 500, (400, 585), 1, white)
            narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
            narrativeBox.addText(window, "It's a critical hit!")
            #^^Inform user why there was an abnormally high amount of damage
            pygame.display.update()
        userOutPok.hp -= opDamage#subtract damage from HP
        if userOutPok.hp < 0: #set HP to 0 for output purposes
            userOutPok.hp = 0 #if its less than 0
        if opOutPok.hp < 0:
            opOutPok.hp = 0
        userHealthPerCent = userOutPok.hp / userOutPok.maxHP #for display in HP bar
        userHealthBox = Box(250, 100, (0, 600), 1, grey)
        border = Box(251, 101, (0, 600), 2, black)
        #output level, name and HP of pokemon
        userHealthBox.addText(window, " " + userOutPok.name + " lvl" + str(userOutPok.level) + " HP: " + str(int(userOutPok.hp)))
        userHealthBar = Box(200 * userHealthPerCent, 20, (25, 650), 1, green)
        border = Box(201, 20, (25, 650), 2, black) #HP border
        pygame.display.update()
        sleep(1)
        if fainted(userOutPok): #if user battler fainted, tell user
            narrativeBox = Box(500, 500, (400, 585), 1, white)
            narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
            narrativeBox.addText(window, userOutPok.name+" fainted!")
            sleep(0.5)
    else:
        narrativeBox = Box(500, 500, (400, 585), 1, white)
        narrativeBoxBorder = Box(500, 500, (400, 585), 2, black)
        narrativeBox.addText(window, "The attack missed!") #so the user knows why they
                                                            #did no damage
    pygame.display.update()
    sleep(1)
    return userOutPok #returns new attributes of user battler

def priorityCheck(userMove,opMove,priorityMoves,opSpeed,userSpeed):
    #^^speed determiner
    userPriority=False
    opPriority=False
    if userMove.lower() in priorityMoves:
        userPriority=True #user goes first
    if opMove.lower() in priorityMoves:
        opPriority=True #opponent goes first
    if userPriority==True and opPriority==False:
        return True #user goes first
    elif userPriority ==False and opPriority==True:
        return False #opponent goes first
    elif userSpeed > opSpeed: #if both have priority, neither have
        return True #user faster so goes first
    else:
        return False #opponent faster so goes first


def potionValid(userPok):
    valid=False #initially set to False
    for i in range(0,len(userPok)): #runs through all user pokemon
        if userPok[i].hp < userPok[i].maxHP and fainted(userPok[i]) is False: #checks potion can be applied
            valid=True #sets valid to True as potion can be applied
    return valid #boolean as can only be valid or invalid

def reviveValid(userPok):
    valid=False # initially set to False
    for i in range(0,len(userPok)): #runs through all user pokemon
        if fainted(userPok[i]) is True: #Checks pokemon can be revived
            valid = True #sets valid to true as revive can be applied
    return valid #boolean as can only be valid or invalid

def pkmnValid(userPok,userOutPok):
    valid=False #default false
    for i in range(0,len(userPok)):
        if fainted(userPok[i]) is False and userPok[i] != userOutPok:#validity check
           valid=True #if valid, set boolean to true so can be swapped
    return valid
