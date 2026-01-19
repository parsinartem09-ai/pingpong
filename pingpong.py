from pygame import *
from time import sleep

win = display.set_mode((720, 480))
clock = time.Clock()

class Player():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 30, 150)
        self.speed = speed

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
    
    def move(self):
        self.hitbox.x += self.speedx
        self.hitbox.y += self.speedy
        if self.hitbox.top < 0:
            self.speedy = self.speed
        if self.hitbox.bottom > 480:
            self.speedy = -self.speed
        if self.hitbox.left < 0:
            self.speedx = self.speed
            self.hitbox.center = (360, 240)
            sleep(1)
        if self.hitbox.right > 720:
            self.speedx = -self.speed
            self.hitbox.center = (360, 240)
            sleep(1)
        for player in player_list:
            if self.hitbox.colliderect(player.hitbox):
                self.speedx *= -1


player1 = Player(50, 240, 5)
ball = Ball(360, 240, 3)
player2 = Player(670, 240, 1)
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
    display.update()
    clock.tick(200)