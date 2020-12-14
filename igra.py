from random import randrange

import pygame as pg
from pygame.math import Vector2


class Player(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.image.load('Spaceship_gay .png')
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.vel = Vector2(0, 0)

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                self.vel.x = 5
            elif event.key == pg.K_a:
                self.vel.x = -5
            elif event.key == pg.K_w:
                self.vel.y = -5
            elif event.key == pg.K_s:
                self.vel.y = 5
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d and self.vel.x > 0:
                self.vel.x = 0
            elif event.key == pg.K_a and self.vel.x < 0:
                self.vel.x = 0
            elif event.key == pg.K_w:
                self.vel.y = 0
            elif event.key == pg.K_s:
                self.vel.y = 0

    def update(self):
        # Двигает игрока.
        self.pos += self.vel
        self.rect.center = self.pos


def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    bg = pg.image.load('popa.jpg')
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    camera = Vector2(400, 300)
    player = Player((400, 300), all_sprites)

    background_rects = [pg.Rect(randrange(-3000, 3001), randrange(-3000, 3001), 20, 20)
                        for _ in range(500)]
    song = pg.mixer.Sound('Loyalty Freak Music - It feels good to be alive too.mp3')
    song.play()
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            player.handle_event(event)

        all_sprites.update()
        # Вектор, ведущий от камеры к игроку.
        heading = player.pos - camera
        # Перемещение камеры на долю длины вектора.
        camera += heading * 0.05
        # Фактическое смещение, которое мы должны добавить к позициям объектов.
        offset = -camera + Vector2(400, 300) 

        screen.blit(bg,(0,0))
        # Blit все объекты и добавить смещение к их позициям.
        for background_rect in background_rects:
            topleft = background_rect.topleft + offset
            pg.draw.rect(screen, (200, 50, 70), (topleft, background_rect.size))

        screen.blit(player.image, player.rect.topleft+offset)
        #pg.display.flip()
        clock.tick(60)
        pg.display.update()

if __name__ == '__main__':
    main()
    pg.quit()
