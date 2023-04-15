from pygame import*

game=True
clock= time.Clock()

okno = display.set_mode(700,600)

fon = transform.scale(image.load('background.jpg'), ((750, 750), FULLSCREEN)

class GameSprite(sprite.Sprite):
    def __init__(self, pikt, x,y):
        super().__init__()
        self.image = transform.scale(image.load(pikt), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x,self.rect.y))

class igrok(GameSprite):
    def  control(self):
        self.ris()
        self.lastx = self.rect.x
        self.lasty = self.rect.y
        kn = key.get_pressed()
        if kn[K_LEFT]:
            self.rect.x -= 5
        if kn[K_RIGHT]:
            self.rect.x += 5
        if kn[K_DOWN]:
            self.rect.y += 5
        if kn[K_UP]:
            self.rect.y -= 5
boba = igrok('free-png.ru-61.png', 50,50)                      
                      
class Wall(sprite.Sprite):
    def __init__(self, x,y,shir,vis):
        super().__init__()
        self.image = Surface((shir,vis))
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x,self.rect.y))
Wallgroup = [
]

while game:
    for i in event.get():
        if i .type == QUIT:
            game  = False
    if i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                game = False
    okno.blit(fon, (0,0))
                      
    display.update()
    clock.tick(60)   














