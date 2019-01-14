import random
import sys
import time
import tkinter

import pygame
from bullet import Bullet,EBullet
from alien import Alien

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.moving_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.moving_left = True
            if event.key == pygame.K_j:
                ship.fire = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.moving_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.moving_left = False

def init_alien(ai_settings,screen,aliens):
    blank_x=ai_settings.screen_width/(ai_settings.alien_row+1)-32
    blank_y=ai_settings.screen_height/2/(ai_settings.alien_line+1)-32
    for i in range(ai_settings.alien_row):
        for j in range(ai_settings.alien_line):
            new_alien = Alien(ai_settings, screen, blank_x+i*(32+blank_x) , ai_settings.state_height+blank_y+j*(32+blank_y))
            aliens.add(new_alien)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)< ai_settings.bullets_max_number:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def nextLevel(screen, ai_settings,aliens,bullets,ebullets):
    ai_settings.level+=1
    if ai_settings.level == 4:
        tkinter.messagebox.showinfo('恭喜', '你通关了！')
        sys.exit()
    myfont = pygame.font.SysFont('SimHei', 52)
    level_board = '准备进入第{level}关'.format(level=ai_settings.level)
    textImage = myfont.render(level_board, True, (0, 255, 0))
    screen_rect = screen.get_rect()
    image_rect = textImage.get_rect()
    for bullet in bullets:
        bullets.remove(bullet)
    for ebullet in ebullets:
        ebullets.remove(ebullet)
    screen.blit(textImage, (screen_rect.centerx-image_rect.centerx, screen_rect.centery-image_rect.centery))
    pygame.display.flip()
    time.sleep(3)
    ai_settings.alien_row += 1
    ai_settings.alien_line += 1
    ai_settings.alien_speed_factor += 0.8
    ai_settings.ship_speed_factor += 0.8
    ai_settings.ebullet_speed_factor += 1.0
    ai_settings.ebullets_max_number += 1
    init_alien(ai_settings, screen, aliens)

def check_kill(screen,bullets,aliens,ai_settings,ebullets):
    for bullet in bullets:
        for alien in aliens:
            if pygame.sprite.collide_rect(bullet, alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                ai_settings.enermy_number -= 1
                ai_settings.score += 100
                if ai_settings.enermy_number == 0:
                    nextLevel(screen, ai_settings,aliens,bullets,ebullets)

def check_bekill(ebullets,ship,ai_settings):
    for ebullet in ebullets:
        if pygame.sprite.collide_rect(ebullet, ship):
            ebullets.remove(ebullet)
            ai_settings.life-=1
            ship.rect.centerx = 0
            if ai_settings.life<0:
                tkinter.messagebox.showinfo('哇','你输了！')
                sys.exit()
            else:
                ship.centerx=-200

def update_aliens(aliens):
    for alien in aliens:
        pass

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings,screen,ship,bullets,aliens,ebullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.copy():
        bullet.draw_bullet()
    for ebullet in ebullets.copy():
        ebullet.draw_bullet()
    for alien in aliens:
        alien.blitme()
    myfont = pygame.font.SysFont('SimHei',36)
    Score_board='关卡：{level}  剩余敌人：{num}  分数：{score} 生命：{life}'.format(level=ai_settings.level,num=ai_settings.enermy_number,score=ai_settings.score,life=ai_settings.life)
    textImage=myfont.render(Score_board,True,(0,0,255))
    screen.blit(textImage,(0,0))
    pygame.display.flip()

def enermy_shoot(alien,ebullets,screen,ai_settings):
    if len(ebullets)< ai_settings.ebullets_max_number:
        new_ebullet = EBullet(ai_settings,screen,alien)
        ebullets.add(new_ebullet)


def ai_move(ship,aliens,ebullets,screen,ai_settings):
    for alien in aliens:
        seed = random.randint(1, 100)
        if ship.rect.centerx-alien.rect.centerx<10 and ship.rect.centerx-alien.rect.centerx>-10:
            enermy_shoot(alien, ebullets, screen, ai_settings)
        if alien.direction==2 and ship.rect.centerx-alien.rect.centerx>1:
            pass
        else:
            if seed == 1:
                alien.direction=1
        if alien.direction == 1 and ship.rect.centerx - alien.rect.centerx < -1:
            pass
        else:
            if seed ==1:
                alien.direction = 2
        if alien.rect.centerx<18:
            alien.direction = 2
        if alien.rect.centerx>ai_settings.screen_width:
            alien.direction = 1
        if alien.direction==1:
            alien.rect.centerx-=1
        else:
            alien.rect.centerx+=1


def update_ebullets(ebullets,ai_settings):
    for ebullet in ebullets.copy():
        if ebullet.rect.bottom >= ai_settings.screen_height:
            ebullets.remove(ebullet)