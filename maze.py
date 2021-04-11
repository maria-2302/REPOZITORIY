#создай игру "Лабиринт"!
from pygame import*

okno = display.set_mode((700,500))
bkgd = transform.scale(image.load('background.jpg'),(700,500))
gm = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

class sprit(sprite.Sprite):
    def __init__(self, imimage, x, y, sspeed):
        super().__init__()
        self.image = transform.scale(image.load(imimage),(65,65))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))

class igrok(sprit):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]:
            self.rect.x -=1
        if keys_pressed[K_d]:
            self.rect.x +=1
        if keys_pressed[K_w]:
            self.rect.y -=1
        if keys_pressed[K_s]:
            self.rect.y +=1

hero = igrok('hero.png', 100,380,1)

class Enemy(sprit):
    def update(self):
        if self.rect.x <= 400:
            self.direction = 'right'
        if self.rect.x >= 700 - 100:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class wall(sprit):
    def __init__(self,wall_x,wall_y,wall_w,wall_h,color1,color2,color3):
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.wall_h = wall_h
        self.wall_w = wall_w
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3	
        self.image = Surface((self.wall_w, self.wall_h))
        self.rect = self.image.get_rect()
        self.rect.x = self.wall_x
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect.y = self.wall_y
    def draw(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))

        




zlodey1 = Enemy('cyborg.png', 100,370,3)
zlodey2 = Enemy('cyborg.png', 100,270,4)
zlodey3 = Enemy('cyborg.png', 100,170,2)

stena = wall(200,230,200,10,13, 59, 17)

font.init()
font = font.Font(None, 70)
los = font.render('you lose', True, (200,200,0))
gs = font.render('you win',True, (200,200,0))

while gm:
    okno.blit(bkgd,(0,0))
    hero.selff()
    zlodey1.selff()
    zlodey2.selff()
    zlodey3.selff()
    for i in event.get():
        if i.type == QUIT:
            gm = False
    hero.update()
    hero.selff()
    zlodey1.update()
    zlodey1.selff()
    zlodey2.update()
    zlodey2.selff()
    zlodey3.update()
    zlodey3.selff()
    stena.draw()
    if sprite.collide_rect(zlodey1, hero):
        game = False
    if sprite.collide_rect(zlodey2, hero):
        game = False
    if sprite.collide_rect(zlodey3, hero):
        game = False
    if sprite.collide_rect (hero, zlodey1):
        hero.rect.x = 100
        hero.rect.y = 120
    if sprite.collide_rect (hero, zlodey2):
        hero.rect.x = 100
        hero.rect.y = 120
    if sprite.collide_rect (hero, zlodey3):
        hero.rect.x = 100
        hero.rect.y = 120
    display.update()
    