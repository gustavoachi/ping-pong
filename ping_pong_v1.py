from pygame import *

# Variables iniciales

# Escena del juego:
back = (200, 255, 255)  # Color de fondo
win_width = 600  # Ancho de la ventana
win_height = 500  # Alto de la ventana
window = display.set_mode((win_width, win_height))
window.fill(back)

# Banderas responsables del estado del juego
game = True
finish = False
clock = time.Clock()
FPS = 60

imagen_raqueta = 'racket.png'
imagen_pelota = 'tenis_ball.png'

# Clase principal para sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
         
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Clase heredera del sprite del jugador (controlada por flechas)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

# Crear las raquetas y la pelota
racket1 = Player(imagen_raqueta, 30, 200, 4, 50, 150)
racket2 = Player(imagen_raqueta, 520, 200, 4, 50, 150)
ball = GameSprite(imagen_pelota, 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('JUGADOR 1 PERDISTE!', True, (180, 0, 0))
lose2 = font.render('JUGADOR 2 PERDISTE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.fill(back)

        racket1.update_r()
        racket1.reset()
        racket2.update_l()
        racket2.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        display.update()
        clock.tick(FPS)