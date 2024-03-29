# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:18:27 2024

@author: Brooklyn
"""

import pygame, random, simpleGE

class Taco(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("taco1.png")
        self.setSize(100, 100)
        self.reset()
    
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(1, 8)
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        


class Cart(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("tacocart2.png")
        self.setSize(250, 250)
        self.position = (190, 350)
        self.moveSpeed = 10
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill((18, 22, 41))
        self.setImage("tacobckgrnd.PNG")
        
        self.sndTaco = simpleGE.Sound("crunch.wav")
        
        self.cart = Cart(self)
        self.taco = []
        for i in range(20):
            self.taco.append(Taco(self))
        
        self.sprites = [self.cart, self.taco]
    
    def process(self):
        for Taco in self.taco:
            if self.cart.collidesWith(Taco):
                self.sndTaco.play()
                Taco.reset()
            
def main():
    pygame.display.set_caption("Cinco de Taco!")
    game = Game()
    game.start()

if __name__ == "__main__":
    main()