import random

import pygame as pg
from pygame.examples.grid import TILE_SIZE

import Налаштування
from WORLD_OF_CLASH_rOYALE import world_map,text_map

def ray_casting(sc,player,TEXTURES):
    cur_angle = player.angle-Налаштування.HALF_FOV
    xo,yo = player.pos
    objects = []
    for ray in range(Налаштування.NUM_OF_RAYS):
        cos_a = Налаштування.math.cos(cur_angle)
        sin_a = Налаштування.math.sin(cur_angle)

        depth = 0
        step = Налаштування.TILE

        while depth < Налаштування.MAX_DEPTH:
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            pg.draw.line(sc,Налаштування.WHITE,player.pos,(x,y),5)
            if (x // Налаштування.TILE, y // Налаштування.TILE) in world_map:
                if step < 2 :
                    depth *= Налаштування.math.cos(player.angle-cur_angle)
                    proj_height = min(Налаштування.PROJ_COEF/(depth+0.0001), Налаштування.HEIGHT)

                    offset = ((x/Налаштування.TILE-int(x/Налаштування.TILE))+(y/Налаштування.TILE-int(y/Налаштування.TILE)))/2
                    #color1 = 255*(1-(depth/Налаштування.MAX_DEPTH))
                    #color2 = random.randint(9, 255)
                    #c3 = random.randint(9, 255)
                    #pg.draw.rect(sc,(color1,color2,c3),(Налаштування.SCALE*ray,Налаштування.HALF_HEIGHT-(proj_height/2), Налаштування.SCALE,proj_height))

                    texture = text_map[int(y//Налаштування.TILE)][int(x//Налаштування.TILE)]
                    txtr = TEXTURES[texture]
                    wall_column = txtr.subsurface(offset*100,0,txtr.get_width()//Налаштування.TILE,txtr.get_height())
                    wall_column = pg.transform.scale(wall_column,(Налаштування.SCALE,abs(proj_height)))




                    #sc.blit(wall_column,(ray*Налаштування.SCALE, Налаштування.HALF_HEIGHT-proj_height/2))
                    objects.append([depth,(ray*Налаштування.SCALE,(Налаштування.HALF_HEIGHT-proj_height//2)+player.height*proj_height),wall_column])
                    break


                else:
                    depth -= step
                    step /= 2
            depth += step
        cur_angle += Налаштування.DELTA_ANGLE
    return objects