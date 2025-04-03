from pygame import *
window_color = (204, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')


clock = time.Clock()
FPS = 60
game = True
finish = False
speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (130, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (130, 0, 0))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed  


        

ball = GameSprite('ball.png', 330, 220, 1, 70, 50)
r1 = Player('racket.png', 20, 150, 5, 20, 200)
r2 = Player('racket.png', 660, 150, 5, 20, 200)
 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(window_color)
        ball.reset()
        r1.reset()
        r2.reset()
        r1.update_l()
        r2.update_r()
        if ball.rect.y <= 0:
            speed_y *= -1
        if ball.rect.y >= 445:
            speed_y *= -1
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
            speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 630:
        finish = True
        window.blit(lose2, (200, 200))
        
        

    display.update()
    clock. tick(FPS)
