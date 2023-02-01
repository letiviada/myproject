#!/usr/local/bin/python3
import pygame
from Objects import Bow, Apple, GameObject
from utils import load_sprite,same_screen,random_pos
w,h=800,600
running=True
class ShootingGame:
    def __init__(self):
        self.__init__pygame()
        self.screen=pygame.display.set_mode((w,h))
        #self.background= load_sprite("name", False)
        self.clock=pygame.time.Clock()
        self.bow=Bow((400,540))
        self.apple=[
        Apple(random_pos(self.screen)) for _ in range(10)
        ]

    def main_loop(self):
        while running:
            self.handle_input()
            self.game_logic()
            self.draw()
    def __init__pygame(self):
        pygame.init()
        pygame.display.set_caption("Shooting Game")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.K_ESCAPE:
                quit()
        key=pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.bow.rotate(clockwise=True)
        elif key[pygame.K_LEFT]:
            self.bow.rotate(clockwise=False)
        if key[pygame.K_UP]:
            self.bow.accel()
        if key[pygame.K_SPACE]:
            self.bow.stopit()

    def game_objects(self):
        return [*self.apple, self.bow]

    def game_logic(self):
        for gobj in self.game_objects():
            gobj.move(self.screen)

    def draw(self):
        self.screen.fill((135,206,250))
        #self.screen.blit(self.background, (0,0))
        for gobj in self.game_objects():
            gobj.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)

if __name__=="__main__":
    shooting_game=ShootingGame()
    shooting_game.main_loop()
