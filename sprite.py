from pickle import FALSE

import pygame as pg
import Налаштування
from WORLD_OF_CLASH_rOYALE import world_map
import math
from Налаштування import *
class Sprite:
    def __init__(self,game,x,y,scale,image):
        self.x = x * Налаштування.TILE
        self.y = y * Налаштування.TILE
        self.scale = scale
        self.image = image
        self.w = image.get_width()
        self.h = image.get_height()
        self.sc = game.screen
    def render(self,player,objects):
        dx = self.x - player.x
        dy = self.y - player.y
        theta = math.atan2(dy, dx)
        delta = theta - player.angle
        if dx > 0 and player.angle > math.pi:
            delta += math.tau
        delta_rays = delta / DELTA_ANGLE
        x = (NUM_OF_RAYS / 2 + delta_rays) * SCALE
        dist = math.hypot(dx, dy)
        norm_dist = dist * math.cos(delta)
        if -self.w / 2 < x < (WIDTH - self.w / 2) and norm_dist > 0.5:
            proj = SCREEN_DIST / norm_dist * self.scale
            proj_width = proj * (self.w / self.h)
            proj_height = proj
            y = HALF_HEIGHT - max(proj_height, 0.0001) / 2 + 0.0
            # pg.draw.rect(self.sc, self.colour, (x, y, proj_width, proj_height))
            img = pg.transform.scale(self.image, (proj_width, proj_height))
            # self.sc.blit(img, (x, y))
            objects.append((dist, (x, y+player.height*proj_height), img))
class MiniPekka(Sprite):
    def __init__(self,game,x,y,scale):
        super().__init__(game,x,y,scale,game.sprites["mini_pekka.png"])
    def check_collisions(self,dx,dy):
        if (self.x+dx//TILE,self.y+dy//TILE):
            return True
        return False
    def update(self,player):
        h = True
        for x,y in world_map:
            rect = pg.Rect(x,y,TILE,TILE)
            if rect.clipline((self.x,self.y,player.x,player.y)):
                h = FALSE
                break
        dx = self.x-player.x
        dy=self.y-player.y
        dist = math.hypot(dx,dy)
        if h and dist > 5:
            dx,dy = 0,0
            if self.x > player.x:
                dx =-5
            if self.y > player.y:
                dy =-5
            if self.x < player.x:
                dx = 5
            if self.y < player.y:
                dy = 5
            if not self.check_collisions(dx,dy):
                self.x +=dx
                self.y +=dx