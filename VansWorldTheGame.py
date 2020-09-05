import pygame as pg
import os
import numpy as np
import random
import re
import time

def delay(count):
    count = count * 100
    i = 0
    while i < count:
        i =  i + 1


def Attack(xPos, yPos, screen1):
    screen1.fill((0,0,0), rect=(xPos,0,xPos + 5,170))
    

def PlayerMovement(xPos, yPos, xInc, yInc, screen1, model):
    screen1.fill((0,0,0), rect=(4,600,1278,688))
    if xPos + xInc <= 1280:
        xPos = xPos + xInc
    if yPos + yInc <= 720:
        yPos = yPos + yInc

    
    PlayerSwapn(model, xPos, yPos, screen1)
    return xPos, yPos


def PlayerSwapn(modelToLoad, xLoc, yLoc, screen1):
    assetList = os.listdir('assets-player')
    searchString = '.*'+modelToLoad+'.*'
    
    for mem in assetList:
        if re.search(searchString ,mem):
            path = os.path.join('assets-player',mem)
            img = pg.image.load(path)
            screen1.blit(img, (xLoc, yLoc))
            

    
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
    
    
    xPos = 0
    yPos = 650
    # swapn player charactere
    PlayerSwapn('mega', xPos, yPos, screen1)
    
    while True:
        closingFlag = False
        for event in pg.event.get():
            print(event)
            xInc = 0
            yInc = 0
            
            if event.type == pg.QUIT:
                pg.quit()
                closingFlag = True
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == ord('a'):
                    xInc = -15
                if event.key == pg.K_RIGHT or event.key == ord('d'):
                    xInc = +15 
        
            
            if event.type == pg.MOUSEBUTTONUP:
                Attack(xPos, yPos, screen1)
            xPos, yPos = PlayerMovement(xPos, yPos, xInc, yInc, screen1, 'mega')
            pg.display.update()
            
        if closingFlag == True:
            break

    return


PlayGame()
