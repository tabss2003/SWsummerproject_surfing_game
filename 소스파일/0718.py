import pygame
import pygame as pg
import random
from time import sleep


WHITE= (255,255,255)
RED=(255,0,0)
BLACK =(0,0,0)



pad_width= 1024
pad_height=512
background_width=1024
surf_width =90
surf_height =55

trash_width =110
trash_height =67

wave1_width=80
wave1_height=80
wave2_width=80
wave2_height=80
wave3_width=80
wave3_height=80
wave4_width=80
wave4_height=80

def distanceScore(count):
    global gamepad

    font = pg.font.SysFont(None,25)
    text = font.render(str(count)+' M',True,WHITE)
    gamepad.blit(text,(0,35))

def drawScore(count):
    global gamepad

    font = pg.font.SysFont(None,25)
    text = font.render('trash pass: '+str(count),True,WHITE)
    gamepad.blit(text,(0,0))

def LIFEScore(count):
    global gamepad

    font = pg.font.SysFont(None,25)
    text = font.render('LIFE: '+str(count),True,WHITE)
    gamepad.blit(text,(0,20))

def gameover():
    global gamepad
    dispMessage('GAME OVER')
    
def textObj(text,font):
    textSurface = font.render(text,True, RED)
    return textSurface,textSurface.get_rect()

def dispMessage(text):
    global gamepad

    largeText = pg.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect =textObj(text,largeText)
    TextRect.center=((pad_width/2),(pad_height/2))
    gamepad.blit(TextSurf,TextRect)
    pg.display.update()
    sleep(2)
    runGame()
def crash():
    global gamepad,LIFE
    LIFE-=1
   # dispMessage('Crashed!')
    

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))


def runGame():
    global gamepad,clock,surf,background1,background2,LIFE
    global waves,trash,bullet,boom

    isShottrash = False
    boom_count =0
    LIFE = 3
    trash_pass = 0
    distance=0
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
        distance+=5
        background2_x -=2
        


        if background1_x == -background_width:
            background1_x =background_width
            #distance+=10
            
        if background2_x == -background_width:
            background2_x =background_width
            #distance+=10

        drawObject(background1,background1_x,0)
        drawObject(background2,background2_x,0)

        drawScore(trash_pass)
        LIFEScore(LIFE)
        distanceScore(distance)

        if trash_pass >= 5: # 5개이상 지나칠 경우 gameover
            gameover()
        
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
            trash_pass+=1 #쓰레기 그냥 지나갈경우
            trash_x = pad_width
            trash_y=random.randrange(0,pad_height)

        if wave[1] == None:
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

        if x + surf_width> trash_x: 
            if(y>trash_y and y< trash_y +trash_height)or (y+surf_height > trash_y and y+ surf_height<trash_y+trash_height):
                crash() #라이프 -1 어떻게 ? 조건을 바꿔보자 
                

        if wave[1]!=None:
            if wave[0] == 0:
                wave_width = wave1_width
                wave_height = wave1_height
            elif wave[0] ==1:
                wave_width=wave2_width
                wave_height=wave2_height
            elif wave[0] ==2:
                wave_width=wave3_width
                wave_height=wave3_height
            elif wave[0] ==3:
                wave_width=wave4_width
                wave_height=wave4_height
            if x+ surf_width > wave_x:
                if(y>wave_y and y< wave_y+wave_height)or (y+surf_height>wave_y and y+surf_height<wave_y+wave_height):
                    crash()
                    
                    
        drawObject(surf,x,y)

        if len(bullet_xy)!=0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)
                
        if not isShottrash:
            drawObject(trash,trash_x,trash_y)
        else:
            drawObject(boom,trash_x,trash_y)
            boom_count+=1 
            if boom_count>5:
                trash_x=pad_width
                trash_y=random.randrange(0,pad_height-trash_height)
                isShottrash=False

        if wave[1] !=None:
            drawObject(wave[1],wave_x,wave_y)


        pg.display.update()
        clock.tick(60)

    pg.quit()
    quit()

def initGame():
    global gamepad,clock,surf,background1,background2
    global waves,trash,bullet,boom


    waves=[]

    
    pygame.init()
    gamepad=pg.display.set_mode((pad_width,pad_height))
    pg.display.set_caption('surfing game')

    background1 =pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/water.jpg')
    background1= pg.transform.scale(background1,(1024,512))
    background2 = background1.copy()

    wave1=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave.png')
    wave1=pg.transform.scale(wave1,(80,80))
    wave2=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave2.png')
    wave2=pg.transform.scale(wave2,(80,80))
    wave3=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave3.png')
    wave3=pg.transform.scale(wave3,(80,80))
    wave4=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/wave4.png')
    wave4=pg.transform.scale(wave4,(80,80))
    
    waves.append((0,wave1))
    waves.append((1,wave2))
    waves.append((2,wave3))
    waves.append((3,wave4))
    
    boom= pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/boom.png')

    trash=pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/trash1.png')
    trash=pg.transform.scale(trash,(80,80))


    for i in range(5):
        waves.append((i+2,None))

    surf = pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/surf.png')
    surf = pg.transform.scale(surf,(150,150))
    surf = pg.transform.rotate(surf,-90)

    bullet = pg.image.load('C:/Users/tabss/OneDrive/문서/GitHub/SWsummerproject_surfing_game/image/bullet.png')
    #bullet = pg.transform.rotate(bullet,180)
    clock = pg.time.Clock()
    runGame()

initGame()
