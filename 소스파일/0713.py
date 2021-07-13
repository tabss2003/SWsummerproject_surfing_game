import pygame
import pygame as pg

BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
pad_width= 500
pad_height=700
background_height =700

def back(background,x,y):
    global gamepad
    gamepad.blit(background,(x,y))

def surfer(x,y):
    global gamepad,surf
    gamepad.blit(surf,(x,y))

def runGame():
    global gamepad,clock,surf,background1,background2

    x= pad_width * 0.05
    y= pad_height *0.8
    x_change =0
    y_change =0

    background1_y = 0
    background2_y = -background_height
    
    crashed =False
    while not crashed:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change =-5
                elif event.key == pygame.K_DOWN:
                    y_change= 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change =0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change =0
        x+=x_change
        y+=y_change

        gamepad.fill(WHITE)

        background1_y +=2 #
        background2_y +=2

        if background1_y == +background_height:
            background1_y =-background_height
            
        if background2_y == +background_height:
            background2_y =-background_height
            
        back(background1,0,background1_y)
        back(background2,0,background2_y)

        
        surfer(x,y)
        pg.display.update()
        clock.tick(60)

    pg.quit()
    quit()

def initGame():
    global gamepad,clock,surf,background1,background2

    pygame.init()
    gamepad=pg.display.set_mode((pad_width,pad_height))
    pg.display.set_caption('surfing game')

    background1 =pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/water.jpg')
    background1= pg.transform.scale(background1,(500,700))
    background2 = background1.copy()


    surf = pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/surf.png')
    surf = pg.transform.scale(surf,(150,150))
    #surf = pg.transform.rotate(surf,180)
    
    
    clock = pg.time.Clock()
    runGame()

initGame()
