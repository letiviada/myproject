#!/usr/local/bin/python3
from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import load_sprite,same_screen

UP=Vector2(0,-1)

class GameObject:
    def __init__(self,position,sprite,velocity):
        self.position=Vector2(position)
        self.sprite=sprite
        self.radius=sprite.get_width()/2
        self.velocity=Vector2(velocity)

    def draw(self,surface):
        blit_position=self.position-Vector2(self.radius)
        surface.blit(self.sprite,blit_position)

    def move(self,surface):
        self.position=same_screen(self.position + self.velocity,surface)

    def collision(self, other):
        distance=self.position.distance_to(other.position)
        return dis
        tance<self.radius+other.radius

class Bow(GameObject):
    rot_vel=3
    acceleration=0.10
    def __init__(self,position):
        self.direction=Vector2(UP)
        super().__init__(position,load_sprite("bow"),Vector2(0))

    def rotate(self,clockwise=True):
        sign=1 if clockwise else -1
        angle=self.rot_vel*sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle=self.direction.angle_to(UP)
        rotated_surf=rotozoom(self.sprite, angle,1.0)
        rotated_surf_size=Vector2(rotated_surf.get_size())
        blit_pos=self.position-rotated_surf_size*0.5
        surface.blit(rotated_surf,blit_pos)

    def accel(self):
        self.velocity+=self.direction*self.acceleration

    def stopit(self):
        self.velocity=Vector2(0)

class Apple(GameObject):
    def __init__(self,position):
        super().__init__(position,load_sprite("apple"),(0,1))
