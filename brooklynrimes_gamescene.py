# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:33:11 2024

@author: Brooklyn
"""
import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("tacobckgrnd.png")
        self.sprites = []
        
def main():
    game = Game()
    game.start()
    
if __name__ =="__main__":
    main() 