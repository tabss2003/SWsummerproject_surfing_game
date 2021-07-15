import pygame
import pygame as pg
import random

BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
pad_width= 500
pad_height=700
background_height =700

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))


def runGame():
    global gamepad,clock,surf,background1,background2
    global waves,trashs,Gettrach

    #
    isPickuptrash = False
    Gettrash_count=0
    #

    x= pad_width * 0.05
    y= pad_height *0.8
    x_change =0
    y_change =0

    background1_y = 0
    background2_y = -background_height

    wave_x=random.randrange(0,pad_width)
    wave_y=-pad_height
    random.shuffle(waves)
    wave=waves[0]

    trash_x=random.randrange(0,pad_width)
    trash_y=pad_height
    random.shuffle(trashs)
    trash=trashs[0]
    

    
    
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
                    
                elif event.key == pg.K_SPACE:
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change =0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change =0
        x+=x_change
        y+=y_change

        gamepad.fill(WHITE)

        background1_y +=2 
        background2_y +=2

        wave_y +=5
        if wave_y>=pad_height:
            wave_y=-pad_height
            wave_x=random.randrange(0,pad_width)
            random.shuffle(waves)
            wave=waves[0]
        if wave == None:
            wave_y+=5
        else:
            wave_y+=3

        if trash == None:
            trash_y+=7
        else:
            trash_y+=5
            
        if trash_y>=pad_height:
            trash_y=-pad_height
            trash_x=random.randrange(0,pad_width)
            random.shuffle(trashs)
            trash=trashs[0]
            
        if background1_y == +background_height:
            background1_y =-background_height
            
        if background2_y == +background_height:
            background2_y =-background_height
            
        drawObject(background1,0,background1_y)
        drawObject(background2,0,background2_y)
        #drawObject(wave,wave_x,wave_y)

        if trash !=None:
            drawObject(trash,trash_x,trash_y)
        if wave !=None:
            drawObject(wave,wave_x,wave_y)
        drawObject(surf,x,y)
        
        pg.display.update()
        clock.tick(60)

    pg.quit()
    quit()

def initGame():
    global gamepad,clock,surf,background1,background2
    global waves,trashs

    trashs=[]
    waves=[]
    
    pygame.init()
    gamepad=pg.display.set_mode((pad_width,pad_height))
    pg.display.set_caption('surfing game')

    background1 =pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/water.jpg')
    background1= pg.transform.scale(background1,(500,700))
    background2 = background1.copy()

    wave=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave.png')
    wave=pg.transform.scale(wave,(80,80))
    wave= pg.transform.rotate(wave,-90)
    waves.append(wave)
    wave2=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave2.png')
    wave2=pg.transform.scale(wave2,(80,80))
    waves.append(wave2)
    wave3=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave3.png')
    wave3=pg.transform.scale(wave3,(80,80))
    waves.append(wave3)
    wave4=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave4.png')
    wave4=pg.transform.scale(wave4,(80,80))
    waves.append(wave4)
    wave5=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave5.png')
    wave5=pg.transform.scale(wave5,(80,80))
    waves.append(wave5)

    trash1=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash1.png')
    trash1=pg.transform.scale(trash1,(80,80))
    trashs.append(trash1)
    trash2=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash2.png')
    trash2=pg.transform.scale(trash2,(80,80))
    trashs.append(trash2)
    trash3=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash3.png')
    trash3=pg.transform.scale(trash3,(80,80))
    trashs.append(trash3)
    trash4=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash4.png')
    trash4=pg.transform.scale(trash4,(80,80))
    trashs.append(trash4)
    trash5=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash5.png')
    trash5=pg.transform.scale(trash5,(80,80))
    trashs.append(trash5)
    trash6=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash6.png')
    trash6=pg.transform.scale(trash6,(80,80))
    trashs.append(trash6)
    trash7=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash7.png')
    trash7=pg.transform.scale(trash7,(80,80))
    trashs.append(trash7)

    for i in range(7):
        trashs.append(None)
    for j in range(5):
        waves.append(None)
    
    surf = pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/surf.png')
    surf = pg.transform.scale(surf,(150,150))
    #surf = pg.transform.rotate(surf,180)

    
    clock = pg.time.Clock()
    runGame()

initGame()
