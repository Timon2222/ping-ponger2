from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('background.jpg'), (700, 500))



clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, player_y,  player_width, player_height, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (player_width, player_height))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


    def colliderect(self, sprite):
          return self.rect.colliderect(sprite.rect)
      



class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 455: 
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 455: 
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, player_image,  player_x, player_y,  player_width, player_height, player_speed):
        super().__init__(player_image,  player_x, player_y,  player_width, player_height, player_speed)
        self.speed_x = self.speed
        self.speed_y =  self.speed

    def update(self):
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1
        if self.rect.x > 650 or self.rect.x <0:
            self.speed_x *= -1
        if self.colliderect(racket1) or self.colliderect (racket2):
            self.speed_x *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
ball = Ball('Ball.png',100, 10, 70, 40, 5)
racket1 = Player("Raketka.png", 600, 200, 100, 100, 10)
racket2 = Player("Raketka2.png", 20, 200, 100, 100, 10)
game = True
finish = False
font.init()
font1 = font.SysFont('Arial', 36)
count1 = 0
count2 = 0

while game:
    if finish != True:
        window.blit(background,(0, 0))
        text_count1 = font1.render('игрок Слева:'+str(count1),1,(255, 255, 255))
        window.blit(text_count1,(10,20))
        text_count2 = font1.render('игрок Справа:'+str(count2),1,(255, 255, 255))
        window.blit(text_count2,(400,20))
        if ball.rect.x > 650: 
            count1 +=1
            ball.rect.x = 320
            ball.rect.y = 200
        if ball.rect.x <0:
            ball.rect.x = 320
            ball.rect.y = 200
            count2 +=1
        ball.update()
        ball.reset()
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False
         
    clock.tick(FPS)
    display.update()