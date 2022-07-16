import random #For generating random pipes
import pygame
from pygame import image
from pygame import transform
from pygame.display import set_caption
from pygame.locals import *
import sys


#GLOBALS

FPS = 60
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
GROUNDY = SCREEN_HEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}

PLAYER = 'Gallery/Sprites/bird1.png'
BACKGROUND = 'Gallery/Sprites/bg.png'
PIPE = 'Gallery/Sprites/pipe.png'


if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()    
    pygame.display.set_caption('Aaryan\'s Flappy Bird')
    GAME_SPRITES['numbers']=(
        pygame.image.load('Gallery/Sprites/0.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/1.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/2.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/3.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/4.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/5.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/6.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/7.png').convert_alpha(),
        pygame.image.load('Gallery/Sprites/8.png').convert_alpha()
        )
    GAME_SPRITES['message'] = pygame.image.load('Gallery/Sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('Gallery/Sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
        )
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Gallery/Sounds/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Gallery/Sounds/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Gallery/Sounds/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Gallery/Sounds/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('Gallery/Sounds/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert() 
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()


    def welcomeScreen():
        playerx = int(SCREEN_WIDTH/5)
        playery =int((SCREEN_HEIGHT-GAME_SPRITES['player'].get_height())/2)
        messagex = int((SCREEN_WIDTH-GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREEN_HEIGHT*0.16)
        basex = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                    return ''
                else:
                    SCREEN.blit(GAME_SPRITES['background'],(0,0))
                    SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                    SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                    SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)






    def mainGame():
        score = 0
        playerx = int(SCREEN_WIDTH/5)
        playery = int(SCREEN_WIDTH/2)
        basex = 0
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        upperPipes = [
            {'x':SCREEN_WIDTH+200,'y':newPipe1[0]['y']},
            {'x':SCREEN_WIDTH+200+(SCREEN_WIDTH/2   ),'y':newPipe1[0]['y']}
            ]
        lowerPipes = [
            {'x':SCREEN_WIDTH+200,'y':newPipe2[0]['y']},
            {'x':SCREEN_WIDTH+200+(SCREEN_WIDTH/2   ),'y':newPipe2[0]['y']}
            ]

        pipeVelX = -4

        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8
        playerFlapped = False

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()


                        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
                        if crashTest:
                            return     

                        #check for score
                        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
                        for pipe in upperPipes:
                            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                                score +=1
                                print(f"Your score is {score}") 
                                GAME_SOUNDS['point'].play()


                        if playerVelY < playerMaxVelY and not playerFlapped:
                            playerVelY += playerAccY

                        if playerFlapped:
                            playerFlapped = False            
                        playerHeight = GAME_SPRITES['player'].get_height()
                        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

                        # move pipes to the left
                        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                            upperPipe['x'] += pipeVelX
                            lowerPipe['x'] += pipeVelX

                        # Add a new pipe when the first is about to cross the leftmost part of the screen
                        if 0<upperPipes[0]['x']<5:
                            newpipe = getRandomPipe()
                            upperPipes.append(newpipe[0])
                            lowerPipes.append(newpipe[1])

                        # if the pipe is out of the screen, remove it
                        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                            upperPipes.pop(0)
                            lowerPipes.pop(0)
                        
                        # Lets blit our sprites now
                        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

                        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                        myDigits = [int(x) for x in list(str(score))]
                        width = 0
                        for digit in myDigits:
                            width += GAME_SPRITES['numbers'][digit].get_width()
                        Xoffset = (SCREEN_WIDTH - width)/2

                        for digit in myDigits:
                            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREEN_HEIGHT*0.12))
                            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
                        pygame.display.update()
                        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False

def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREEN_HEIGHT/3
    y2 = offset+random.randrange(0,int(SCREEN_HEIGHT-GAME_SPRITES['base'].get_height() - 1.2*offset))
    pipeX = SCREEN_HEIGHT+10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x':pipeX,'y':-y1},
        {'x':pipeX,'y':y2}
    ]
    return pipe


welcomeScreen() 
mainGame()    




