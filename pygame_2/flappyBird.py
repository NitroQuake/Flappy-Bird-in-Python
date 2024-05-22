import pygame
    #change python versions to work
import random
import math

pygame.init()

window_w = 1024
window_h = 768

#outline
screen = pygame.display.set_mode((window_w, window_h))
background = pygame.image.load("background.png").convert_alpha()
    #.convert_alpha() reduces lag caused by images

game = "Begin"

#GameOver
game_over = pygame.image.load("ded.png").convert_alpha()

def game_over_text():
        #renders the over_text and inside of "render" is the text, antialias (just put True), and color
    screen.blit(game_over, (window_w/2-250, window_h/2-250))

#Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
    #inside of "Font" is type of font and size of font, you can also add other fonts by downloading it from "DaFont" and putting it in the projects folder

textX = 10
testY = 10
    #cordinates for where our font would appear

def show_score(x, y):

    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
        #renders the text and inside of "render" is the text, antialias (just put True), and color
    screen.blit(score, (x, y)) 
        #draws the score on the screen to (10, 10)

#flappy bird
flappyBird = pygame.image.load("NitroQuake.png").convert_alpha()
flappyBird_1 = pygame.transform.scale(flappyBird, (40, 40))

flappyBird_X = 250
flappyBird_Y = 384
flappyBirdDown = 0.5
gravity = 0.025

#the random position of the columns 
column_change = random.randint(-170, 210)
column_change2 = random.randint(-170, 210)
column_change3 = random.randint(-170, 210)

#column up
columnUp = pygame.image.load("column_up.png").convert_alpha()
column_ux = 900
column_ux2 = 1200
column_ux3 = 1500
column_uy = 405 + column_change
column_uy2 = 405 + column_change2
column_uy3 = 405 + column_change3
column_ux_change = -1
    #make sure that the value is a multiple of 250 so the command could work

def colup(x, y):
    screen.blit(columnUp, (x, y))

#column down
columnDown = pygame.image.load("column_down.png").convert_alpha()
column_dx = 900
column_dx2 = 1200
column_dx3 = 1500
column_dy = -50 + column_change
column_dy2 = -50 + column_change2
column_dy3 = -50 + column_change3
column_dx_change = -1
    #make sure that the value is a multiple of 250 so the command could work

def coldown(x, y):
    screen.blit(columnDown, (x, y))

running = True
while running:

    screen.blit(background, (0,0))

    p1 = pygame.draw.rect(screen, (0,255,0), [flappyBird_X, flappyBird_Y, 40, 40], 5)

    screen.blit(flappyBird_1, (flappyBird_X, flappyBird_Y))

    obs1 = pygame.draw.rect(screen, (0,255,0), [column_ux, column_uy, 94, 600], 1)
        #surface(where it is drawn), color, location and size, borderline
    obs2 = pygame.draw.rect(screen, (0,255,0), [column_ux2, column_uy2, 94, 600], 1)
    obs3 = pygame.draw.rect(screen, (0,255,0), [column_ux3, column_uy3, 94, 600], 1)
    obs4 = pygame.draw.rect(screen, (0,255,0), [column_dx, column_dy - 300, 94, 600], 1)
    obs5 = pygame.draw.rect(screen, (0,255,0), [column_dx2, column_dy2 - 300, 94, 600], 1)
    obs6 = pygame.draw.rect(screen, (0,255,0), [column_dx3, column_dy3 - 300, 94, 600], 1)

    colup(column_ux, column_uy)
    colup(column_ux2, column_uy2)
    colup(column_ux3, column_uy3)
    coldown(column_dx, column_dy)
    coldown(column_dx2, column_dy2)
    coldown(column_dx3, column_dy3)

    if game is "Start":
        flappyBirdDown += gravity
            #gravity
        flappyBird_Y += flappyBirdDown
            #makes the flappybird fly down
        column_ux += column_ux_change
        column_ux2 += column_ux_change
        column_ux3 += column_ux_change
        column_dx += column_dx_change  
        column_dx2 += column_dx_change  
        column_dx3 += column_dx_change  
            #makes the columns move left

    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #resets score
            if game == "Stop" or game == "Begin":
                game = "Start"
                score_value = 0
            if event.key == pygame.K_SPACE:
                flappyBirdDown = -2
    
    #border collision and change of column position
    if column_dx and column_ux <= 0:
        column_ux = 900
        column_dx = 900
        columnChange = random.randint(-170, 210)
        column_uy = 405 + columnChange
        column_dy = -50 + columnChange
    if column_dx2 and column_ux2 <= 0:
        column_ux2 = 900
        column_dx2 = 900
        columnChange2 = random.randint(-170, 210)
        column_uy2 = 405 + columnChange2
        column_dy2 = -50 + columnChange2
    if column_dx3 and column_ux3 <= 0:
        column_ux3 = 900
        column_dx3 = 900
        columnChange3 = random.randint(-170, 210)
        column_uy3 = 405 + columnChange3
        column_dy3 = -50 + columnChange3
    
    #collision of flappybird with obstacle 
    if pygame.Rect.colliderect(p1, obs1) or pygame.Rect.colliderect(p1, obs2) or pygame.Rect.colliderect(p1, obs3) or pygame.Rect.colliderect(p1, obs4) or pygame.Rect.colliderect(p1, obs5) or pygame.Rect.colliderect(p1, obs6) or flappyBird_Y > 664 or flappyBird_Y < 0:
        game = "Stop"
            #figure out a way to make it so the score stays until you press space
        flappyBird_X = 250
        flappyBird_Y = 384
        column_dx = 900
        column_dx2 = 1200
        column_dx3 = 1500
        column_dy = -50 + column_change
        column_dy2 = -50 + column_change2
        column_dy3 = -50 + column_change3
        column_ux = 900
        column_ux2 = 1200
        column_ux3 = 1500
        column_uy = 405 + column_change
        column_uy2 = 405 + column_change2
        column_uy3 = 405 + column_change3
        pygame.time.delay(1000)
    if game == "Stop":
        game_over_text()

    
    #Score
    if column_dx == 250 or column_dx2 == 250 or column_dx3 == 250:
        score_value += 1
    
    show_score(textX, testY)
        #shows the score
    
    pygame.display.update()
            
        

        

        
