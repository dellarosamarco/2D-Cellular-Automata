import Tile
import pygame, sys
from pygame.locals import *
import random

class Map : 
    tiles = []

    def __init__(
        self, 
        width, 
        height, 
        cellSize,
        density,
        iterations
    ) : 
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.density = density
        self.iterations = iterations

        for x in range(0,self.width) : 
            for y in range(0,self.height) : 
                fillCell = random.randint(0,100) < self.density
                newTile = Tile.Tile(cellSize*x,cellSize*y,fillCell)
                self.tiles.append(newTile)

        self.tempTiles = self.tiles[:]


        for n in range(0,self.iterations) :
            self.iterate()
            #self.drawMap()
            self.tiles = self.tempTiles[:]
                   
        self.drawMap()

    def iterate(self) : 
        for tile in self.tiles : 
            if(self.countNeighbours(tile) >= 3) :
                #tile.active = True
                self.tempTiles[self.tiles.index(tile)].active = True
            else : 
                #tile.active = False
                self.tempTiles[self.tiles.index(tile)].active = False

    def countNeighbours(self,tile) :
        neighboursCounter = 0
        
        for x in range(-1,2) :
            for y in range(-1,2) : 
                if(tile.x + x * self.cellSize != tile.x or tile.y + y * self.cellSize != tile.y) :
                    if(self.isActive(tile.x + x * self.cellSize,tile.y + y * self.cellSize)) :
                        neighboursCounter += 1

        return neighboursCounter

    def isActive(self, x, y) :      

        if(x < 0 or y < 0 or x > self.width * self.cellSize or y > self.height * self.height) :
            return False

        for tile in self.tiles :
            if(tile.x == x and tile.y == y) :
                return tile.active

        return False


    def drawMap(self) : 
        pygame.init()

        DISPLAY=pygame.display.set_mode((800,800),0,32)
    
        DISPLAY.fill((0,0,0))

        for tile in self.tiles : 
            if(tile.active) :
                pygame.draw.rect(DISPLAY,(255,255,255),(tile.x,tile.y,self.cellSize,self.cellSize))
    
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            