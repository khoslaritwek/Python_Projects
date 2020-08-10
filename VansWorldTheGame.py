import pygame as pg

    

def PlayGame():
    pg.init()
    screen1 = pg.display.set_mode((1280,720))#, pg.RESIZABLE)
    screen = pg.display.set_caption('Vans World: The Game')
    screen = pg.display.toggle_fullscreen()
    icon = pg.image.load('VansLifeIcon.png')
    pg.display.set_icon(icon)
    playerimg = pg.image.load('VAnsCarGoku.png')
    playerX = 100
    playerY = 100

    
    while True:
        closingFlag = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                closingFlag = True
                break

            screen1.fill((25,178,255))
            screen1.blit(playerimg, (playerX, playerY))
            pg.display.update()
            
        if closingFlag == True:
            break

    return


PlayGame()
