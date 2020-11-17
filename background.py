import pygame
from random import randint
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((800, 600))

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

dx = 1
dy = -1

speedx = 5
speedy = 5

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
        self.image.fill(white)
        self.rect = self.image.get_rect()


pong = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(pong)


def redraw():
    win.fill(black)
    all_sprites.draw(win)
    pygame.display.update()


score_val = 0
scorefont = pygame.font.Font('freesansbold.ttf', 64)


def show_score():
    score = scorefont.render("test", True, (255, 255, 255))
    win.blit(score, (400, 300))


run = True


while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pong.rect.x += speedx * dx
    pong.rect.y += speedy * dy

    #checks if hit corner

    if pong.rect.x >= 750 and pong.rect.y >= 550:
        score_val += 1
        print(score_val)
    if pong.rect.x >= 750 and pong.rect.y <= 0:
        score_val += 1
        print(score_val)
    if pong.rect.x <= 0 and pong.rect.y <= 0:
        score_val += 1
        print(score_val)
    if pong.rect.x <= 0 and pong.rect.y >= 550:
        score_val += 1
        print(score_val)


    #checks if hit side

    if pong.rect.x >= 750:
        dx = -1
        if randint(0, 10) == 4:
            dy *= -1
        speedx = randint(2, 4)
        speedy = randint(2, 3)
    if pong.rect.x <= 0:
        dx = 1
        if randint(0, 10) == 4:
            dy *= -1
        speedx = randint(2, 4)
        speedy = randint(2, 3)
    if pong.rect.y >= 550:
        dy = -1
        if randint(0, 10) == 4:
            dx *= -1
        speedx = randint(2, 4)
        speedy = randint(2, 3)
    if pong.rect.y <= 0:
        dy = 1
        if randint(0, 10) == 4:
            dx *= -1
        speedx = randint(2, 4)
        speedy = randint(2, 3)
    redraw()
    show_score()


