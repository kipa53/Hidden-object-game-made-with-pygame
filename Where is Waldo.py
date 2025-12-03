#library
import pygame
import pygame.gfxdraw
from pygame import color
from pygame.locals import *
import time
import random


pygame.display.set_caption('where is Waldo?')
Running = True
pygame.init()
width = 600
height = 400
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
death_sound = pygame.mixer.Sound("sounds/sound.wav")
end = pygame.image.load('pictures/end.jpg')
win = pygame.image.load('pictures/win.jpg')
mainmenu = pygame.image.load('pictures/start.jpg')
mapa = pygame.image.load('pictures/map.png')
enemy_image = pygame.image.load("pictures/enemy.png")
dead_played = False
x = random.randrange(10,390)
y = random.randrange(10,390)
enemy_rect = enemy_image.get_rect(topleft=(x,y))
enemy_alive = False

#promenljive
Start = True
rect_x = 10
rect_y = 10
health = 100
rect_h = 20
rect_w = health
last_dmg = 0
dmg_cooldown = 1000
color = ('green')
color1 = ('black')
game = True
enemy = 0



#funkcije
def dmg():
    global health, last_dmg, enemy
    now = pygame.time.get_ticks()  
    if now - last_dmg >= dmg_cooldown and enemy < 10:
        health -= 3.33
        last_dmg = now

def heal():
     global health
     health = 100

def dead():
    global screen, game, dead_played
    if not dead_played:
        death_sound.play()     
        dead_played = True
    screen.blit(end, (0,0))
    game = False
#game start
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

      
        if Start and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Start = False
      

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    pygame.display.flip()


    if Start:
        screen.blit(mainmenu, (0,0))
        pygame.display.flip()
        continue  
  

    screen.blit(mapa,(0,0))

    keys = pygame.key.get_pressed()
    if game == True:
        pygame.draw.rect(screen,color,(rect_x,rect_y,rect_w,rect_h))
        pygame.draw.rect(screen,color1,(rect_x,rect_y,103,rect_h),width=5)

    rect_w = health
    if health >= 50:
        color = ('green')
        
    if health <=49 and health > 25:
        color = ('yellow')
    if health < 25 and health > 0:
        color = ('red')   
    if health > 100:
        health = 100
    if health >0:
        game = True

    keys = pygame.key.get_pressed()

    if enemy_alive == False and keys[pygame.K_SPACE]:
        enemy_alive = True
        enemy = 0
        heal()

    if not enemy_alive and keys[pygame.K_SPACE]:
        x = random.randrange(10, 590)
        y = random.randrange(10, 300)
        enemy_alive = True
        enemy_image = pygame.image.load("pictures/enemy.png") 
        enemy_rect = enemy_image.get_rect(topright=(x,y)) 
        heal()

    # draw and click logic
    if enemy_alive:
        screen.blit(enemy_image, enemy_rect)
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed(5)[0]
        dmg()
        print(health)
        if mouse_click and enemy_rect.collidepoint(mouse_pos):
            enemy_alive = False
            enemy += 1
            print("enemy defeated")  
            x = random.randrange(10, 590)
            y = random.randrange(10, 590)   
            enemy_rect.topleft = (x, y) 

    if enemy >= 1:
        screen.blit(win,(0,0))
        game = False

    if health <= 0:
        print('you died')
        dead()
        
    if game == False and keys[pygame.K_SPACE]:
        game = True
        health = 100
        dead_played = False   

    if health < 0:
        health = 0