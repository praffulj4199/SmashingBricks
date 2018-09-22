# to set where the window will pop up always
x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


import pygame
import time
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 155,0)

pygame.init()
pygame.display.init()

screen_height = 600
screen_width = 800


icon = pygame.image.load('strawberry.png')
pygame.display.set_icon(icon)
display = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("SMASH THE BRICKS!")
FPS = 60
clock = pygame.time.Clock()

brick_length = 200
brick_width = 10


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 75)

def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                     pygame.quit()
                     quit()
        display.fill(white)
        message_to_screen("Welcome to", green, -150, "medium")
        message_to_screen("SMASH THE BRICKS!", green, -100, "large")
        message_to_screen("The aim is to smash the bricks :P", black, 30)
        message_to_screen("Try landing on the platform", black, 70)        
        message_to_screen("If you run into edges, you lose", black, 110)
        message_to_screen("Press C to continue, P to pause or Q to quit", black, 180)

        pygame.display.update()
        clock.tick(15)
        
def score(score):
     text = smallfont.render("Score: "+str(score), True, black)
     display.blit(text, [0,0])
     
def pause():
     paused = True
     message_to_screen("Paused", black, -100, size ="large")
     message_to_screen("Press C to Continue or Q to quit", black,25, size ="small")
     pygame.display.update()
     while paused:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                         paused = False

                    elif event.key == pygame.K_q:
                         pygame.quit()
                         quit()
               

              
               clock.tick(5)
def text_objects(text, color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface,textSurface.get_rect()

def message_to_screen(msg,color, y_displace =0,size = "small"):
    textSurface , textRect = text_objects(msg,color,size)
    textRect.center = (screen_width/2), (screen_height/2) + y_displace
    display.blit(textSurface,textRect)

def randBrick():
     randBrickX = round(random.randrange(0, screen_width-brick_length))
     randBrickY = round(random.randrange(0, screen_height / 2 -brick_width ))
     return randBrickX, randBrickY

def brickColour():
        brick_R = round(random.randrange(0,256))
        brick_G = round(random.randrange(0,256))
        brick_B = round(random.randrange(0,256))
        return brick_R,brick_G,brick_B

def gameLoop():
            gameOver = False
            gameExit = False
            
            randBrickX,randBrickY = randBrick()
            brick_R,brick_G,brick_B = brickColour()
            platform_length = 100
            platform_width = 20
            platformx = int((screen_width - platform_length)  / 2)
            playformy = int(screen_height - platform_width - 5)
            speed = 0

            ball_rad = 7
            ballx = int(screen_width / 2)
            bally = int(screen_height - platform_width - ball_rad - 5)
            ballx_change = 10
            bally_change = -10

            scor = 0
            
            while not gameExit:

                    
                     
                    if gameOver == True:
                         message_to_screen("Game Over ", red,y_displace=  -20,size = "large")
                         message_to_screen("Press c to continue or q to quit", black, y_displace= 50)
                         pygame.display.update()

                         
                    while gameOver == True:
                            
                            for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                            gameExit = True
                                            gameOver = False 

                                    if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_q:
                                                    gameExit = True
                                                    gameOver = False
                                            if event.key == pygame.K_c:
                                                    gameLoop()


                    display.fill((255,255,255))
                    pygame.draw.rect(display,(brick_R,brick_G,brick_B),[randBrickX,randBrickY,brick_length,brick_width])
                    
                                                 
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    gameExit = True
                                    pygame.display.quit()
                                    pygame.quit()
                                    quit()

                            if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_LEFT:
                                            speed = -15

                                    if event.key == pygame.K_RIGHT:
                                            speed = 15
                            
                                    if event.key == pygame.K_p:
                                        pause()
                            if event.type == pygame.KEYUP:
                                speed = 0
                    if bally + ball_rad > screen_height - 5:
                            gameOver = True
                            print("rip")

                    if ballx + ball_rad > platformx and ballx - ball_rad < platformx + platform_length and screen_height - platform_width - 5 < bally + ball_rad < screen_height - 5:
                            bally_change *= -1

                    if ballx + ball_rad > screen_width - 5 or ballx - ball_rad < 5:
                            ballx_change *= -1

                    if bally - ball_rad < 5:
                            bally_change *= -1

                    if platformx < 5:
                            platformx += 3
                            speed = 0

                    if platformx > screen_width - platform_length - 5:
                            platformx -= 3
                            speed = 0

                    score(scor)
                    if ballx + ball_rad > randBrickX and ballx - ball_rad < randBrickX + brick_length and bally + ball_rad > randBrickY and bally - ball_rad < randBrickY + brick_width:
                            randBrickX,randBrickY = randBrick()
                            brick_R,brick_G,brick_B = brickColour()
                            bally_change *= -1
                            scor += 1
                                   
                    platformx += speed
                    ballx += ballx_change
                    bally += bally_change
                                                         
                                    
                    pygame.draw.rect(display,(0,0,0),[platformx,playformy,platform_length,platform_width])
                    pygame.draw.circle(display,(0,0,0),[ballx,bally],ball_rad)
                    pygame.display.update()
 
                    clock.tick(40)
            pygame.quit()   
            quit()

game_intro()
gameLoop()


