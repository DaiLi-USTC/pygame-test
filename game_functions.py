import sys
import tkinter

import pygame
from bullet import Bullet
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

def check_kill(aliens,bullets,ai_settings):
    for bullet in bullets:
        for alien in aliens:
            if pygame.sprite.collide_rect(bullet, alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                ai_settings.enermy_number -= 1
                ai_settings.score += 100
                if ai_settings.enermy_number == 0:
                    tkinter.messagebox.showinfo('恭喜','打人完毕！')
                    sys.exit()

def update_aliens(aliens):
    for alien in aliens:
        pass

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings,screen,ship,bullets,aliens):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.copy():
        bullet.draw_bullet()
    for alien in aliens:
        alien.blitme()
    myfont = pygame.font.SysFont('SimHei',48)
    Score_board='剩余敌人：{num}  分数：{score}'.format(num=ai_settings.enermy_number,score=ai_settings.score)
    textImage=myfont.render(Score_board,True,(0,0,255))
    screen.blit(textImage,(0,0))
    pygame.display.flip()