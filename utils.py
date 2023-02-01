#!/usr/local/bin/python3
import random
from pygame.math import Vector2
from pygame.image import load

def load_sprite(name, with_alpha=True):
    path=f"assets/sprites/{name}.png"
    loaded=load(path)

    if with_alpha:
        return loaded.convert_alpha()
    else:
        return loaded.convert()

def same_screen(position,surface):
    x,y=position
    w,h=surface.get_size()
    return Vector2(x%w,y%h)

def random_pos(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        0,
    )
