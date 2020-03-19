import pygame as pg
import random as r
pg.init()
pg.mixer.init()
pop = pg.mixer.Sound("pop.wav")
blip = pg.mixer.Sound("blip.wav")
blap = pg.mixer.Sound("blap.wav")
pic = pg.image.load("hullmyts.png")
star = pg.image.load("star.png")
cstar = pg.image.load("cyanstar.png")
starc1 = pg.image.load("starclump1.png")
pg.font
screen = pg.display.set_mode((0,0), pg.RESIZABLE)
screenw = screen.get_width()
screenh = screen.get_height()
pg.display.set_caption("Star Eater")
do = True
dist = 5
up = True
down = True
left = True
right = True
mup = False
mdown = False
mleft = False
mright = False
timer = pg.time.Clock()
time = 600
tick = 0
starseaten = 0
lifes = 5
font = pg.font.SysFont("Times", 24)
dfont = pg.font.SysFont("Times", 32)
pfont = pg.font.SysFont("Times", 50)
pause = False
gameover = False
player = pg.sprite.GroupSingle()
potatoes = pg.sprite.Group()
stars = pg.sprite.Group()
c1stars = pg.sprite.Group()
mgstars = pg.sprite.Group()
oggeees = 9999999999999
starsn = 111
tstars = starsn
c1starsn = 0
mstarsn = 0
moggeee = False
mstars = False
compress = False
vjrf = 0
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self, mup, mdown, mleft, mright):
        if self.rect.y <= 0:
            up = False
        else:
            up = True
        if self.rect.y >= screenh-100:
            down = False
        else:
            down = True
        if self.rect.x <= 0:
            left = False
        else:
            left = True
        if self.rect.x >= screenw-124:
            right = False
        else:
            right = True
        if mup and up:
            self.rect.y -= dist 
        if mdown and down:
            self.rect.y += dist
        if mleft and left:
            self.rect.x -= dist
        if mright and right:
            self.rect.x += dist
class Star(pg.sprite.Sprite):
    def __init__(self, x, y, xvel, yvel, img=star):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xvel = xvel
        self.yvel = yvel
    def update(self,newspeed = False):
        if newspeed:
            self.xvel = r.randint(-10,10)
            self.yvel = r.randint(-10,10)
        if self.rect.x <= 10 or self.rect.x >= screenw-90:
            self.xvel = -self.xvel
        if self.rect.y <= 10 or self.rect.y >= screenh-30:
            self.yvel = -self.yvel
        self.rect.x += self.xvel
        self.rect.y += self.yvel
hullmyts = Player(screenw/2,screenh/2)
player.add(hullmyts)
stars.add(Star(r.randint(10,screenw-30),r.randint(10,screenh-30),0,0))
while do:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            do = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                mup = True
            elif event.key == pg.K_DOWN:
                mdown = True
            elif event.key == pg.K_LEFT:
                mleft = True
            elif event.key == pg.K_RIGHT:
                mright = True
            elif event.key == pg.K_p:
                pause = True
            elif event.key == pg.K_r:
                starseaten = 0
                oggeees = 0
                potatoeseaten = 0
                lifes = 5
                tick = 0
                time = 600
                stimer = False
                player.empty()
                stars.empty()
                hullmyts = Player(screenw/2,screenh/2)
                player.add(hullmyts)
                stars.add(Star(r.randint(10,screenw-30),r.randint(10,screenh-30),0,0))
            elif event.key == pg.K_o:
                moggeee = True
            elif event.key == pg.K_s:
                mstars = True
            elif event.key == pg.K_h and tstars >= 50:
                vjrf += vjrfg
                starsn = 1
                tstars = 1
                stars.empty()
                c1stars.empty()
                c1starsn = 0
                starseaten = 0
                oggeees = 0
            elif event.key == pg.K_m and tstars >= 100 and vjrf >= 100:
                mstarsn += min(starsn//100,vjrf//100)
                starsn = 1
                tstars = 0
                stars.empty()
                starseaten = 0
                oggeees = 0
                vjrf = 0
                c1stars.empty()
                c1starsn = 0
            elif event.key == pg.K_c:
                compress = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                mup = False
            elif event.key == pg.K_DOWN:
                mdown = False
            elif event.key == pg.K_LEFT:
                mleft = False
            elif event.key == pg.K_RIGHT:
                mright = False
            elif event.key == pg.K_o:
                moggeee = False
            elif event.key == pg.K_s:
                mstars = False
            elif event.key == pg.K_c:
                compress = False
    if moggeee and starseaten >= 5:
        starseaten -= 5
        oggeees += 1
    if mstars and oggeees >= 5:
        oggeees -= 5
        starsn += 1
    if compress and oggeees >= 100 and starsn >= 5:
        oggeees -= 100
        starsn -= 5
        c1starsn += 1
        c1stars.add(Star(r.randint(10,screenw-30),r.randint(10,screenh-30),
                                 r.randint(-10,10),r.randint(-10,10),starc1))
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pause = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause = False
        pd = "PAUSED"
        ptext = dfont.render(pd, True, (127,127,127))
        ptext_rect = ptext.get_rect()
        ptext_rect.centerx = screen.get_rect().centerx
        ptext_rect.y = 50
        screen.blit(ptext,ptext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
    if lifes <= 0:
        blap.play()
        uded = "GAME OVER"
        dtext = dfont.render(uded, True, (255,0,0))
        dtext_rect = dtext.get_rect()
        dtext_rect.centerx = screen.get_rect().centerx
        dtext_rect.y = 30
        screen.blit(dtext,dtext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
        gameover = True
    while gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    gameover = False
                    starseaten = 0
                    oggeees = 0
                    potatoeseaten = 0
                    lifes = 5
                    tick = 0
                    time = 0
                    player.empty()
                    stars.empty()
                    hullmyts = Player(screenw/2,screenh/2)
                    player.add(hullmyts)
                    stars.add(Star(r.randint(10,screenw-30),
                                   r.randint(10,screenh-30),0,0))
    screen.fill((0,0,0))
    score = ("Klols: " + str(round(starseaten,2)) +" Oggeees: " + str(oggeees) +
             " Stars: " + str(starsn) + " Vjrf: " + str(vjrf) +
             " Mega Stars: " + str(len(mgstars)))
    text = font.render(score, True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text,text_rect)
    if tstars < 50:
        vjrfg = 0
    else:
        vjrfg = tstars-49
    info = ("O to make oggeees (5 klols). " +
            "S to make stars (5 oggeees). " +
            " H to prestige, works only when 50 or more stars. gives " +
            str(vjrfg) + " vjrf points.")
    itext = font.render(info, True, (255,255,255))
    itext_rect = itext.get_rect()
    itext_rect.centerx = screen.get_rect().centerx
    itext_rect.y = 50
    screen.blit(itext,itext_rect)
    info2 = ("M to level 2 prestige, gives 1 mega star. You need 100 stars and vjrf")
    iitext = font.render(info2, True, (255,255,255))
    iitext_rect = iitext.get_rect()
    iitext_rect.centerx = screen.get_rect().centerx
    iitext_rect.y = 90
    screen.blit(iitext,iitext_rect)
    player.update(mup,mdown, mleft, mright)
    player.draw(screen)
    stars.update()
    c1stars.draw(screen)
    c1stars.update()
    stars.draw(screen)
    mgstars.update()
    mgstars.draw(screen)
    col = pg.sprite.spritecollide(hullmyts,stars,False)
    if len(col) > 0:
        starseaten += 1 + (vjrf/100)
        stars.remove(col)
        tick = 0
        time = 600
        pop.play()
    mcol = pg.sprite.spritecollide(hullmyts,mgstars,False)
    if len(mcol) > 0:
        starseaten += 100 + vjrf
        mgstars.remove(mcol)
        tick = 0
        blip.play()
    c1col = pg.sprite.spritecollide(hullmyts,c1stars,False)
    if len(c1col) > 0:
        starseaten += 5 + (vjrf/20)
        c1stars.remove(c1col)
        pop.play()
    if len(stars) < starsn:
        stars.add(Star(r.randint(20,screenw-100),r.randint(20,screenh-30),
                       r.randint(-10,10),r.randint(-10,10)))
    if len(mgstars) < mstarsn:
        mgstars.add(Star(r.randint(20,screenw-100),r.randint(20,screenh-30),
                       r.randint(-10,10),r.randint(-10,10),cstar))
    if c1starsn > len(c1stars):
        c1stars.add(Star(r.randint(10,screenw-30),r.randint(10,screenh-30),
                         r.randint(-10,10),r.randint(-10,10),starc1))
    pg.display.update()
    timer.tick(60)

pg.quit()
