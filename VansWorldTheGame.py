import pygame as pg
import os
import numpy as np
import random
import re 

def PlayerSwapn(modelToLoad, xLoc, yLoc, screen1):
    assetList = os.listdir('assets-player')
    searchString = '.*'+modelToLoad+'.*'
    
    for mem in assetList:
        if re.search(searchString ,mem):
            path = os.path.join('assets-player',mem)
            img = pg.image.load(path)
            screen1.blit(img, (xLoc, yLoc))
            print ('here')
            

    
def loadAssests():
    assetList = os.listdir('assets-block')
    assets = []

    for mem in assetList:
        path = os.path.join('assets-block', mem)
        print(path)
        img = pg.image.load(path)
        assets.append(img)

    return assets

    
def IntialSenceSetup(screen1):
    assets =  loadAssests()

    yPos = 0
    while yPos < 160:
        xPos = 0
        while xPos < 1280 :
            img = random.choice(assets)
            screen1.blit(img, (xPos, yPos))
            xPos = xPos + 80 
        yPos = yPos + 20
    

def PlayGame():
    pg.init()
    screen1 = pg.display.set_mode((1280,720))
    screen = pg.display.set_caption('Vans World: The Game')
    screen = pg.display.toggle_fullscreen()
    icon = pg.image.load('VansLifeIcon.png')
    pg.display.set_icon(icon)

    #sets up intial player environment
    IntialSenceSetup(screen1)
    
    # swapn player charactere
    PlayerSwapn('mega', 0, 650, screen1)
    
    while True:
        closingFlag = False
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                pg.quit()
                closingFlag = True
                break

                        
            pg.display.update()
            
        if closingFlag == True:
            break

    return


PlayGame()
