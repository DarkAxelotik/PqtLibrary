import pygame
import os
pygame.init()

def file_path(file_name):
    folder_path = os.path.abspath(__file__+"/..")
    path = os.path.join(folder_path, file_name)
    return path


WIN_WIDTH, WIN_HEIGHT = 700, 500
FPS = 60


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Bendy run")
clock = pygame.time.Clock()


img_background = pygame.transform.scale(pygame.image.load(file_path("sprite and bg\\fon.jpg.jpg")), (WIN_WIDTH, WIN_HEIGHT))
win_img = pygame.transform.scale(pygame.image.load(file_path("sprite and bg\\wsin.jpg")), (WIN_WIDTH, WIN_HEIGHT))
lose_img = pygame.transform.scale(pygame.image.load(file_path("sprite and bg\\lose.jpg")), (WIN_WIDTH, WIN_HEIGHT))

pygame.mixer.music.load(file_path("sound\\fon.wav"))
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

music_win = pygame.mixer.Sound(file_path("sound\\win.wav"))
music_lose = pygame.mixer.Sound(file_path("sound\\MUS_DeathOfAFriend.ogg.ogx"))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(GameSprite):
    def __init__(self, x, y, width, height, img, speed, min_cord, max_cord, direction):
        super().__init__(x, y, width, height, img)
        self.speed = speed
        self.min_cord = min_cord
        self.max_cord = max_cord
        self.direction = direction
    
    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "right":
                self.rect.x += self.speed
            elif self.direction == "left":
                self.rect.x -= self.speed

            if self.rect.right >= self.max_cord:
                self.direction = "left"
            if self.rect.left <=  self.min_cord:
                self.direction = "right"
        elif self.direction == "up" or self.direction == "down":


            if self.direction == "up":
                self.rect.y -= self.speed
            elif self.direction == 'down':
                self.rect.y += self.speed

            if self.rect.top <= self.min_cord:
                self.direction = "down"
            if self.rect.bottom >= self.max_cord:
                self.direction = "up"
        

class Player(GameSprite):
    def __init__(self, x, y, width, height, img):
        super(). __init__(x , y, width, height, img)
        self.speed_x = 0
        self.speed_y = 0
        self.direction = "right"
        self.image_r = self.image
        self.image_l = pygame.transform.flip(self.image, True, False)
    
    
    def shot(self):
        if self.direction == "right":
            bullet = Bullet(self.rect.right, self.rect.centery, 5, 5, file_path("sprite and bg\\stina.jpg"), 10)
            bullets.add(bullet)
        elif self.direction == "left":
            bullet = Bullet(self.rect.left, self.rect.centery, 5, 5, file_path("sprite and bg\\stina.jpg"), -10)
            bullets.add(bullet)

    def update(self):
        #рух по горизонталі
        if self.speed_x > 0 and  self.rect.right < WIN_WIDTH or self.speed_x < 0 and self.rect.left > 0:
            self.rect.x += self.speed_x
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        if self.speed_x < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)

        #рух по вертикалі
        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_y < 0:
            for wall in walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)
                
class Bullet(GameSprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__(x ,y, width, height, img)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.left >= WIN_WIDTH or self.rect.right <= 0:
            self.kill()
bullets = pygame.sprite.Group()





player = Player(30, 102, 50, 50, file_path("sprite and bg\\me2.png"))

enemys = pygame.sprite.Group()
enemy1 = Enemy(300, 150, 50, 50, file_path("sprite and bg\\King_Widow.png"), 3, 130, 300, "left")
enemys.add(enemy1)
enemy2 =Enemy(380, 150, 50, 50, file_path("sprite and bg\\King_Widow.png"), 4, 100, 400, "down")
enemys.add(enemy2)
enemy3 =Enemy(200, 150, 50, 50, file_path("sprite and bg\\King_Widow.png"), 2, 100, 300, "right")
enemys.add(enemy3)
enemy4 =Enemy(600, 150, 50, 50, file_path("sprite and bg\\King_Widow.png"), 13, 50, 500, "down")
enemys.add(enemy4)

wall1 = GameSprite(670, 0, 30, 500, file_path("sprite and bg\\stina.jpg"))
portal = GameSprite(650, 0, 30, 500, file_path("sprite and bg\\portal.jpg"))

walls = pygame.sprite.Group()
wall1 = GameSprite(93, 19, 30, 300, file_path("sprite and bg\\stina.jpg"))
walls.add(wall1)
wall2 = GameSprite(200, 190, 30, 300, file_path("sprite and bg\\stina.jpg"))
walls.add(wall2)
wall3 = GameSprite(500, 190, 30, 200, file_path("sprite and bg\\stina.jpg"))
walls.add(wall3)
wall4 = GameSprite(500, 19, 30, 200, file_path("sprite and bg\\stina2.png"))
walls.add(wall4)
wall5 = GameSprite(310, 190, 30, 200, file_path("sprite and bg\\stina.jpg"))
walls.add(wall5)
wall6 = GameSprite(310, 19, 30, 300, file_path("sprite and bg\\stina2.png"))
walls.add(wall6)
wall5 = GameSprite(310, 15, 30, 300, file_path("sprite and bg\\stina.jpg"))
walls.add(wall5)
play = True
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.direction = "right"
                player.image = player.image_r
                player.speed_x = 5
            if event.key == pygame.K_a:
                player.direction = "left"
                player.image = player.image_l
                player.speed_x = -5
            if event.key == pygame.K_s:
                player.speed_y = 5
            if event.key == pygame.K_w:
                player.speed_y = -5
            if event.key == pygame.K_f:
                player.shot()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.speed_x = 0
            if event.key == pygame.K_a:
                player.speed_x = 0
            if event.key == pygame.K_s:
                player.speed_y = 0
            if event.key == pygame.K_w:
                player.speed_y = 0


    if play ==  True:    
        window.blit(img_background, (0,0))
        player.reset()
        player.update()
        

        enemys.draw(window)
        enemys.update()

        portal.reset()
        walls.draw(window)

        bullets.draw(window)
        bullets.update()

        if pygame.sprite.collide_rect(player, portal):
            play = False
            window.blit(win_img, (0,0))
            pygame.mixer.music.stop()
            music_win.play()

        if pygame.sprite.spritecollide(player, enemys, False):
            play = False
            pygame.mixer.music.stop()
            window.blit(lose_img, (0, 0))
            music_lose.play()

        pygame.sprite.groupcollide(bullets, walls, True, False)
        pygame.sprite.groupcollide(bullets, enemys, True, True)


    clock.tick(FPS)
    pygame.display.update()