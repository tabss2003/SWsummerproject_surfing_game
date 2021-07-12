import pygame
import pygame as pg

BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)

def runGame():
    global gamepad,clock

    crashed =False
    while not crashed:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True

        gamepad.fill(WHITE)
        pg.display.update()
        clock.tick(60)

    pg.quit()

def initGame():
    global gamepad,clock

    pygame.init()
    gamepad=pg.display.set_mode((400,300))
    pg.display.set_caption('test')

    clock = pg.time.Clock()
    runGame()

initGame()
