import pygame,sys,random
import pygame.locals as local
import pygame.event as event

pygame.init()

icv = pygame.image.load('Izc.jpg')
win = pygame.display.set_mode((1000,700))
pygame.display.set_icon(icv)
pygame.display.set_caption("important bal")

class ups:
    def up(self):
        for x in range(1000):
            self.ghor = pygame.Rect(x,0,16,16)
            pygame.draw.rect(win,(200,200,200),self.ghor)
    def down(self):
        for x in range(1000):
            self.ghor2 = pygame.Rect(x,684,16,16)
            pygame.draw.rect(win,(200,200,200),self.ghor2)

id = ups() 
get_x = 1.1
get_y = 1.1       

fontT = pygame.font.Font('COPRGTL.ttf',30) 
fontGO = pygame.font.Font('COPRGTL.ttf',90)
fontgo = pygame.font.Font('COPRGTL.ttf',120)
fontR = pygame.font.Font('COPRGTL.ttf',50) 
sp = pygame.time.Clock()


canclick = False
clicked = False
doleft = True
doright = True
class basebal:
    def dose(self):
        global doleft,doright
        doleft = True
        doright = True
    def move(self):
        self.bal = pygame.Rect(500,600,16,16)
    def side(self,x,y):
        self.bal = pygame.Rect(x,y,16,16)
    def color(self):
        self.Red = random.randint(0,255)
        self.Green = random.randint(0,255)
        self.Blue = random.randint(0,255)
    def collid(self):
        
        global get_x,get_y,doleft,doright
        if self.bal.colliderect(p1.player) :
            if doleft:
                get_x *= -1
                doleft = False
                doright = True
                
        if self.bal.colliderect(p2.player2):
             print('bang')
             if doright:
                get_x *= -1
                doleft = True
                doright = False
                print('bang2')
            
            
class timeofgame:
    def stime(self):
        self.time = 30000
    def show(self):
        time = fontT.render(f'{self.time}',True,(255,255,255))
        win.blit(time,(20,20))
    def at(self):
        self.time -= 1
    def outtime(self):
        if self.time <= 0:
            pygame.mixer.music.load('End.mp3')
            pygame.mixer.music.play(1,1.2)
            global get_x,get_y,canclick
            time = fontGO.render(f'Game over',True,(255,255,255),(0,0,0))
            win.blit(time,(235,320))
            time = fontR.render(f'Refresh',True,(255,255,255),(255,0,0))
            win.blit(time,(390,500))
            canclick = True
            self.x_pos = 390
            self.y_pos = 500
            self.xt_pos = 440
            self.yt_pos = 550
            get_x = 0
            get_y = 0
            
            
            
class tech:
    def cheks(self):
        self.chek = 0
        self.chek2 = 0
    def number1(self):
        global fontT,win
        
        tgoal = fontgo.render(f'{self.chek}',True,(255,255,255))
        win.blit(tgoal,(330,20))
        
    def number2(self):
        global fontT,win
        
        tgoal = fontgo.render(f'{self.chek2}',True,(255,255,255))
        win.blit(tgoal,(515,20))
    

tog = timeofgame()
tog.stime()

tech = tech()
tech.cheks()
        

class Player1:
    def step(self):
        self.step = 250
        self.addstep = 1
    def Step(self):
        self.step = 250
        self.addstep = 1
    def up(self):
        
        if self.step <= 16:
            self.addstep = 0
        else:
            self.addstep = 1
        self.step -= self.addstep
            
    def down(self):
        
        if self.step+100 >= 670:
            self.addstep = 0
        else:
            self.addstep = 1
        self.step += self.addstep
    def update(self):
        self.player = pygame.Rect(20,self.step,15,110)
        self.playerGu = pygame.Rect(20,self.step,15,5)
        self.playerGd = pygame.Rect(20,self.step+110,15,5)

        
class Player2:
    def step(self):
        self.step = 100
        self.addstep = 1
    def Step(self):
        self.step = 100
        self.addstep = 1
    def up(self):
        
        if self.step <= 16:
            self.addstep = 0
        else:
            self.addstep = 1
        self.step -= self.addstep
            
    def down(self):
        
        if self.step+100 >= 670:
            self.addstep = 0
        else:
            self.addstep = 1
        self.step += self.addstep
    def update(self):
        self.player2 = pygame.Rect(970,self.step,15,110)
        self.playerGu2 = pygame.Rect(970,self.step,15,5)
        self.playerGd2 = pygame.Rect(970,self.step+110,15,5)
    
            
p1 = Player1()
p1.step()

p2 = Player2()
p2.step()

bal = basebal()
bal.move()
bal.color()
x = 500
y = 600

plkeyup = False
plkeydown = False

plkeyup_2 = False
plkeydown_2 = False


while True:
    win.fill((0,0,0))
    
    
    posm = pygame.mouse.get_pos()
    pygame.draw.line(win,(255,255,255),(500,16),(500,684),4)
    tech.number1()
    tech.number2()
    for ev in event.get():
        if ev.type == local.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            clicked = True
        else:
            clicked = False
        if ev.type == local.KEYDOWN:
            if ev.key == pygame.K_w:
                plkeyup = True
            if ev.key == pygame.K_s:
                plkeydown = True
                
        if ev.type == local.KEYUP:
            if ev.key == pygame.K_w:
                plkeyup = False
            if ev.key == pygame.K_s:
                plkeydown = False
                
        
        if ev.type == local.KEYDOWN:
            if ev.key == pygame.K_UP:
                plkeyup_2 = True
            if ev.key == pygame.K_DOWN:
                plkeydown_2 = True
                
        if ev.type == local.KEYUP:
            if ev.key == pygame.K_UP:
                plkeyup_2 = False
            if ev.key == pygame.K_DOWN:
                plkeydown_2 = False
        
        
    if plkeyup:
        p1.up()
    if plkeydown:
        p1.down()
    if plkeyup_2:
        p2.up()
    if plkeydown_2:
        p2.down()
        
        
    if canclick:
        if clicked:
            if posm[0] >= tog.x_pos and posm[0] <= tog.x_pos+220 and posm[1] >= tog.y_pos and posm[1] <= tog.y_pos+80:
                print('called')
                
                bal.move
                x -= x
                y -= y
                x += 500
                y += 600
                get_x = 1.1
                get_y = 1.1
                tog.stime()
                tech.chek -= tech.chek
                tech.chek2 -= tech.chek2
                bal.dose()
                tech.cheks()
                p1.Step()
                p2.Step()
                
            
    id.up()
    id.down()
    bal.color()
    pygame.draw.rect(win,(bal.Red,bal.Green,bal.Blue),bal.bal)
    bal.side(x,y)
    if y <= 16:
        get_y = get_y * -1
    if y >= 670:
        get_y = get_y * -1
    if x <= 4:
        pygame.mixer.music.load('Goal.mp3')
        pygame.mixer.music.play(1,1.1)
        bal.move()
        x = 500
        y = 600
        bal.side(x,y)
        bal.dose()
        tech.chek2 += 1
        p1.step = 100
        
    if x >= 980:
        pygame.mixer.music.load('Goal.mp3')
        pygame.mixer.music.play(1,1.1)
        bal.move()
        x = 500
        y = 600
        bal.side(x,y)
        bal.dose()
        p2.step = 100
        tech.chek += 1
        

    y -= get_y
    x += get_x
    tog.show()
    tog.outtime()
    tog.at()
    
    p1.update()
    p2.update()
    
    pygame.draw.rect(win,(255,255,255),p1.player)
    pygame.draw.rect(win,(200,0,200),p1.playerGu)
    pygame.draw.rect(win,(200,0,200),p1.playerGd)
    
    pygame.draw.rect(win,(255,255,255),p2.player2)
    pygame.draw.rect(win,(200,0,200),p2.playerGu2)
    pygame.draw.rect(win,(200,0,200),p2.playerGd2)
    bal.collid()
    pygame.display.update()