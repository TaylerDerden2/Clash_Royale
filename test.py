import pygame as pg

pg.font.init()
screen = pg.display.set_mode((500,400), pg.FULLSCREEN)

pg.display.set_caption("Pgame")

clock = pg.time.Clock()


x, y = 50,50
spd=5
rad = 15

font = pg.font.SysFont("calibri", 50,False,False)
image = pg.image.load("Royal_Hogs_3.webp").convert_alpha()

img = image.subsurface(0,0,20,image.get_height())

image = pg.transform.scale(image,(300,300))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill((255,255,255))
    pg.draw.rect(screen,(0,255,0), (50,50,50,50))
    screen.fill((255,255,255))

    keys = pg.key.get_pressed()
    if keys[pg.K_0]:
        pg.draw.rect(screen, (0, 255, 0), (150, 50, 50, 50))
    if keys[pg.K_UP]:
       y-=spd
    if keys[pg.K_DOWN]:
       y+=spd
    if keys[pg.K_LEFT]:
       x-=spd
    if keys[pg.K_RIGHT]:
       x+=spd
    if keys[pg.K_UP]:
       y-=spd
    if keys[pg.K_ESCAPE]:
        exit()

    if x-rad < 0:
        x += spd
    if x+rad > screen.get_width():
        x -= spd

    if y-rad < 0:
        y += spd
    if y+rad > screen.get_height():
        y -= spd

    pg.draw.circle(screen,(0,0,0),(x,y), rad)

    text = font.render("Korolevskiy Kabanchik",False,(255,36,0))
    screen.blit(text,(50,50))
    screen.blit(image,(100,100))

    pg.display.flip()
    clock.tick(60)
