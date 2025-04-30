

import Налаштування
from WORLD_OF_CLASH_rOYALE import world_map
import pygame as pg
import math

class Player:
    def __init__(self,game):
        self.x, self.y = Налаштування.player_pos
        self.angle = Налаштування.player_angle
        self.speed = Налаштування.player_speed
        self.game = game
        self.sensivity = 0.04
        self.height = 0
        self.move_loCk = False
    @property
    def pos(self):
        return (self.x,self.y)
    def check_collisions(self,dx,dy):
        if ((self.x+dx)//Налаштування.TILE, (self.y+dy)//Налаштування.TILE) in world_map:
            return True
        return False
    def mouse_control(self):
        if pg.mouse.get_focused():
            differnce = pg.mouse.get_pos()[0] - Налаштування.HALF_WIDTH
            pg.mouse.set_pos((Налаштування.HALF_WIDTH, Налаштування.HALF_HEIGHT))
            self.angle += differnce*self.sensivity

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pg.key.get_pressed()
        dx,dy = 0,0
        if not self.move_loCk:
            if keys[pg.K_w]:
                dx += cos_a * self.speed
                dy += sin_a * self.speed
            if keys[pg.K_s]:
                dx -= cos_a * self.speed
                dy -= sin_a * self.speed
            if keys[pg.K_a]:
                dx += sin_a * self.speed
                dy -= cos_a * self.speed
            if keys[pg.K_d]:
                dx -= sin_a * self.speed
                dy += cos_a * self.speed
        if keys[pg.K_LEFT]:
            self.angle -= .1
        if keys[pg.K_RIGHT]:
            self.angle += .1
        if keys[pg.K_SPACE] and self.height == 0:
            self.height = 1
            dx += cos_a * self.speed*10
            dy += sin_a * self.speed*10
            self.move_loCk = True
        if self.height > 0:
            self.height -= 0.1
        if self.height <= 0:
            self.move_loCk = False
        if keys[pg.K_ESCAPE]:
            exit()
        self.mouse_control()
        if not self.check_collisions(dx,dy):
            self.x += dx
            self.y += dy