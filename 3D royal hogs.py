import pygame as pg
from Player import Player
from Ray_casting import ray_casting
import Налаштування
from WORLD_OF_CLASH_rOYALE import world_map
import sprite

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((Налаштування.WIDTH,Налаштування.HEIGHT))
        pg.display.set_caption("3D Royal Hogs")
        self.clock = pg.time.Clock()
        pg.mouse.set_visible(False)
        self.player = Player(self)
        self.Textures = {"1":pg.image.load("TEXTURES/ПОРОсяТКО.jpg")}
        self.sprites = {"mini_pekka.png":pg.image.load("sprites/mini_pekka.png").convert_alpha()}

        self.sprite_objects = [
            sprite.Sprite(self,1.5,1.5,100,self.sprites["mini_pekka.png"])
        ]

        self.enemys = [
            sprite.MiniPekka(self,1.5,1.5,100)
        ]
    def sort(self,objects):
        arr = objects
        for x in range(len(objects)-1):
            for i in range(len(objects)-1):
                if arr[i][0] < arr[i+1][0]:
                    temp = objects[i+1]
                    arr[i+1] = arr[1]
                    arr[i] = temp
        return arr
    def draw_objects(self,objects):
        for obj in objects:
            self.screen.blit(obj[2],obj[1])
    def run(self):
        while 1 :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.player.movement()
            self.screen.fill((0,0,0))
            for tile in world_map:
              rect = pg.draw.rect(self.screen,(255,255,255),(tile[0]*Налаштування.TILE,tile[1]*Налаштування.TILE,Налаштування.TILE,Налаштування.TILE))
              pg.draw.rect(self.screen,(255,255,255),rect)
            pg.draw.circle(self.screen,(255,255,255),self.player.pos,5)
            objects = ray_casting(self.screen,self.player,self.Textures)
            for sprt in self.sprite_objects:
                sprt.render(self.player,objects)
            for enemy in self.enemys:
                enemy.render(self.player,objects)
                enemy.update(self.player)
            #objects = self.sort(objects)
            self.draw_objects(objects)
            pg.display.flip()
            self.clock.tick(Налаштування.FPS)

if __name__ == "__main__":
    app = Game()
    app.run()