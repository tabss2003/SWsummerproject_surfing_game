import pygame
import pygame as pg
import random
from time import sleep


WHITE= (255,255,255)
pad_width= 1024
pad_height=512
background_width=1024
wave_width = 110
surf_width =90
surf_height =55

trash_width =110
trash_height =67


def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))


def runGame():
    global gamepad,clock,surf,background1,background2
    global waves,trashs,bullet,boom

    isShottrash = False
    boom_count =0
    
    bullet_xy=[]

    x= pad_width * 0.05
    y= pad_height *0.8
    x_change =0
    y_change =0

    background1_x = 0
    background2_x = background_width

    wave_x=pad_width
    wave_y=random.randrange(0,pad_height)
    random.shuffle(waves)
    wave=waves[0]

    trash_x=pad_width
    trash_y=random.randrange(0,pad_height)
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
                    bullet_x = x+surf_width
                    bullet_y = y+surf_height
                    bullet_xy.append([bullet_x,bullet_y])
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change =0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change =0

        gamepad.fill(WHITE)

        background1_x -=2 
        background2_x -=2


        if background1_x == -background_width:
            background1_x =background_width
            
        if background2_x == -background_width:
            background2_x =background_width

        drawObject(background1,background1_x,0)
        drawObject(background2,background2_x,0)
        
        x+=x_change
        y+=y_change

        if y <0:
            y=0
        elif y>pad_height - surf_height:
            y= pad_height - surf_height

        if x<0:
            x=0
        elif x>pad_width - surf_width:
            y= pad_width - surf_width            
        
        trash_x -=5
        if trash_x<=0:
            trash_x = pad_width
            trash_y=random.randrange(0,pad_height)

        if wave == None:
            wave_x -=5
        else:
            wave_x -=7

        if wave_x <=0:
            wave_x = pad_width
            wave_y =random.randrange(0,pad_height)
            random.shuffle(waves)
            wave=waves[0]
            
        
        if len(bullet_xy)!=0:
            for i,bxy in enumerate(bullet_xy):
                bxy[0] +=5
                bullet_xy[i][0] = bxy[0]

                if bxy[0] >trash_x:
                    if bxy[1] >trash_y and bxy[1] <trash_y+trash_height:
                        bullet_xy.remove(bxy)
                        isShottrash =True
                        
                if bxy[0] >= pad_width:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
                    
        drawObject(surf,x,y)

        if len(bullet_xy)!=0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)
                
        if not isShottrash:
            num=random.choice(trashs)
            drawObject(num,trash_x,trash_y)
            break
        else:
            drawObject(boom,trash_x,trash_y)
            boom_count+=1
            if boom_count>5:
                trash_x=pad_width
                trash_y=random.randrange(0,pad_height-trash_height)
                isShottrash=False

        if wave !=None:
            drawObject(wave,wave_x,wave_y)


        pg.display.update()
        clock.tick(60)

    pg.quit()
    quit()

def initGame():
    global gamepad,clock,surf,background1,background2
    global waves,trashs,bullet,boom


    waves=[]
    trashs=[]

    
    pygame.init()
    gamepad=pg.display.set_mode((pad_width,pad_height))
    pg.display.set_caption('surfing game')

    background1 =pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/water.jpg')
    background1= pg.transform.scale(background1,(1024,512))
    background2 = background1.copy()

    wave=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave.png')
    wave=pg.transform.scale(wave,(80,80))
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
    
    boom= pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/boom.png')

    trash=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash1.png')
    trash=pg.transform.scale(trash,(80,80))
    trashs.append(trash)
    trash2=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash2.png')
    trash2=pg.transform.scale(trash2,(80,80))
    trashs.append(trash2)
    trash3=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash3.png')
    trash3=pg.transform.scale(trash3,(80,80))
    trashs.append(trash3)

    for i in range(6):
        waves.append(None)

    surf = pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/surf.png')
    surf = pg.transform.scale(surf,(150,150))
    surf = pg.transform.rotate(surf,-90)

    bullet = pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/bullet.png')
    #bullet = pg.transform.rotate(bullet,180)
    clock = pg.time.Clock()
    runGame()

initGame()
