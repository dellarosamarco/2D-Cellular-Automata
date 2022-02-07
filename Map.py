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
        iterations,
        biomeGeneration
    ) : 
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.density = density
        self.iterations = iterations
        self.biomeGeneration = biomeGeneration

        #Generate map
        for x in range(0,self.width) : 
            for y in range(0,self.height) : 
                fillCell = random.randint(0,100) < self.density
                newTile = Tile.Tile(cellSize*x,cellSize*y,fillCell)
                self.tiles.append(newTile)

        self.tempTiles = self.tiles[:]

        #Iterations
        for n in range(0,self.iterations) :
            self.iterate()
            # self.drawMap()
            self.tiles = self.tempTiles[:]
                   
        self.drawMap()

    def iterate(self) : 
        for tile in self.tiles : 
            neighbours = self.countNeighbours(tile)
            tileIndex = self.tiles.index(tile)
            if(neighbours >= 4) :
                #tile.active = True
                self.tempTiles[tileIndex].active = True
            else : 
                #tile.active = False
                self.tempTiles[tileIndex].active = False

            self.tempTiles[tileIndex].neighbours = neighbours

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
            if(self.biomeGeneration) :
                pygame.draw.rect(DISPLAY,self.getBiome(tile),(tile.x,tile.y,self.cellSize,self.cellSize))
            else : 
                if(tile.active) :
                    pygame.draw.rect(DISPLAY,(255,255,255),(tile.x,tile.y,self.cellSize,self.cellSize))
    
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def getBiome(self,tile) : 
        if(tile.active == False) :
            return (30,30,190)

        print(tile.neighbours)

        beach = [1,2,3,4]
        grass = [5,6]
        forest = [7,8,9]

        if(tile.neighbours in beach) :
            return (120,255,0)
        elif(tile.neighbours in grass) :
            return (30,225,25)
        elif(tile.neighbours in forest) :
            return (45,255,85)
        
        return (255,255,255)
            