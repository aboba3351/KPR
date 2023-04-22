from pygame import*

game=True
clock= time.Clock()

okno = display.set_mode((700,600), FULLSCREEN)

fon = transform.scale(image.load('градус 228.png'), (750, 750))

class GameSprite(sprite.Sprite):
    def __init__(self, pikt, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(pikt), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direct="verh"
    def rot_center(self,image, rect, angle):
        rot_image = transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        self.image = rot_image
        return rot_image,rot_rect
    def ris(self):
        if self.direct=="verh":
            self.image = transform.scale(image.load('утёнок джек 228.png'),(100,100)) 
        elif self.direct == "vniz":
            self.image = transform.scale(image.load('Down.png'),(100,100))
        elif self.direct == "pravo":
            self.image = transform.scale(image.load('right.png'),(100,100))
        elif self.direct == "levo":
                self.image = transform.scale(image.load('left.png'),(100,100))


            
        okno.blit(self.image, (self.rect.x,self.rect.y))

class igrok(GameSprite):
    def  control(self):
        self.ris()
        self.lastx = self.rect.x
        self.lasty = self.rect.y
        kn = key.get_pressed()
        if kn[K_LEFT]:
            #igrok.image = transform.scale(image.load('left.png'),(100,100))    
            self.rect.x -= 5
            self.direct="levo"
        if kn[K_RIGHT]:
            #igrok.image =   transform.scale(image.load('right.png'),(100,100))  
            self.rect.x += 5
            self.direct="pravo"
        if kn[K_DOWN]:
            #igrok.image = transform.scale(image.load('Down.png'),(100,100))
            self.direct="vniz"
            self.rect.y += 5
        if kn[K_UP]:  
            #igrok.image = transform.scale(image.load('утёнок джек 228.png'),(100,100)) 
            self.rect.y -= 5
            self.direct = "verh"
YTKA = igrok('утёнок джек 228.png',50,50, 100,100)                      
                    
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

class Monster(GameSprite):
    def patrul_h(self,x1,x2):
        self.ris()
        if self.rect.x < x1:
            self.napr = 'pravo'
        if self.rect.x > x2:
            self.napr = 'levo'
        if self.napr == 'pravo':
            self.rect.x +=3
        else:
            self.rect.x -=3
m1 = Monster('monsty.jpg', 9, 270)

while game:
    for i in event.get():
        if i .type == QUIT:
            game  = False
        if i.type == KEYDOWN:
                if i.key == K_ESCAPE:
                    game = False
    okno.blit(fon, (0,0))
    YTKA.control()
                      
    display.update()
    clock.tick(60)  

