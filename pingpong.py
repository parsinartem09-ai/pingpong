from pygame import *
from time import sleep
from random import *

win = display.set_mode((720, 480))
clock = time.Clock()

init()

imggen = font.Font(None, 50)

class Player():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 30, 150)
        self.speed = speed
        self.score = 0
        self.score_img = imggen.render(str(self.score), True, (0, 0, 0), (255, 255, 255))

    def move(self):
        key_list = key.get_pressed()
        if key_list[K_w]:
            self.hitbox.y -= self.speed
        if key_list[K_s]:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 480:
            self.hitbox.bottom = 480
        if self.hitbox.top < 0:
            self.hitbox.top = 0
    
    def autopilotV1(self):
        self.hitbox.centery = ball.hitbox.centery
        if self.hitbox.bottom > 480:
            self.hitbox.bottom = 480
        if self.hitbox.top < 0:
            self.hitbox.top = 0

    def autopilotV2(self):
        if self.hitbox.bottom > 480:
            self.hitbox.bottom = 480
        if self.hitbox.top < 0:
            self.hitbox.top = 0
        if ball.hitbox.centery > self.hitbox.centery:
            self.hitbox.centery += self.speed
        if ball.hitbox.centery < self.hitbox.centery:
            self.hitbox.centery -= self.speed

class Ball():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 30, 30)
        self.speed = speed
        self.speedx = speed
        self.speedy = speed
        self.randomx = 1
        self.randomy = 1
    
    def move(self):
        self.hitbox.x += self.speedx * self.randomx
        self.hitbox.y += self.speedy * self.randomy
        if self.hitbox.top < 0:
            self.speedy = self.speed
        if self.hitbox.bottom > 480:
            self.speedy = -self.speed
        if self.hitbox.left < 0:
            self.speedx = self.speed
            self.hitbox.center = (360, 240)
            self.randomx = 1
            self.randomy = 1
            player2.score += 1
            player2.score_img = imggen.render(str(player2.score), True, (0, 0, 0), (255, 255, 255))
            sleep(1)
        if self.hitbox.right > 720:
            self.speedx = -self.speed
            self.hitbox.center = (360, 240)
            self.randomx = 1
            self.randomy = 1
            player1.score += 1
            player1.score_img = imggen.render(str(player1.score), True, (0, 0, 0), (255, 255, 255))
            sleep(1)
        for player in player_list:
            if self.hitbox.colliderect(player.hitbox):
                self.speedx *= -1
                self.randomx = randint(1, 5)
                self.randomy = randint(1, 5)



player1 = Player(50, 240, 5)
ball = Ball(360, 240, 1)
player2 = Player(670, 240, 2)
player_list = [player1, player2]

while True:
    win.fill((255, 255, 255))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    player1.move()
    draw.rect(win, (255, 0, 0), player1.hitbox)
    player2.autopilotV2()
    draw.rect(win, (255, 0, 0), player2.hitbox)
    ball.move()
    draw.rect(win, (0, 255, 0), ball.hitbox)
    win.blit(player1.score_img, (0, 0))
    win.blit(player2.score_img, (700, 0))
    display.update()
    clock.tick(200)