# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:29:36 2021

@author: sadio_aya5cf2
"""
import pygame
from annexe import Game

pygame.init() #initialisation des modules de python pour les charger au niveau du programme

#modifier le titre
pygame.display.set_caption("Kaizoku Escape")
black_color = (0,0, 0)
window_res = (600, 600)
window_surface = pygame.display.set_mode(window_res)


background = pygame.image.load('assets/wano1.jpg')
play = pygame.image.load('assets/button.png')
play = pygame.transform.scale( play, (300, 100))
play_rect = play.get_rect()
play_rect.x = 150 #math.ceil(window_surface.get_width()/2)
play_rect.y = 270#math.ceil(window_surface.get_height()/2) 

ban = pygame.image.load('assets/logo2.png')
ban = pygame.transform.scale(ban, (128, 128))
ban_rect = ban.get_rect()
ban_rect.x = 236 #math.ceil(window_surface.get_width()/2)
ban_rect.y = 150
#wall
#def wall():
wall_x = [([0, 60], [120, 60]), ([180, 60], [360, 60]), ([420, 60], [540, 60]), 
            ([60, 120], [180, 120]), ([240, 120], [480, 120]), ([120, 180], [540, 180]), 
            ([60, 300], [200, 300]), ([60, 480], [420, 480]), 
            ([120, 240], [200, 240]), ([540, 240], [600, 240]), ([420, 240], [480, 240]), ([240, 240], [350, 240]),
            ([240, 350], [350, 350]), ([240, 240], [240, 350]), ([350, 240], [350, 260]), ([350, 330], [350, 350]),
             ([60, 420], [120, 420]), ([480, 420], [540, 420]), 
            ([240, 420], [360, 420]), ([0, 540], [60, 540] ), 
            ([120,540], [200, 540]), ([300, 540], [600, 540]), ([60, 300], [200, 300] )]
    
wall_y = [([180, 0], [180, 60]), ([420, 0], [420, 60]), ([120, 60], [120, 120]), ([360, 60], [360, 120]), ([540, 60], [540, 180]),
          ([540, 60], [540, 120]), ([540, 60], [540, 120]), ([60, 120], [60, 300]), ([200, 240], [200, 300]), 
          ([540, 240], [540, 420]), ([420, 240], [420, 480]), ([480, 240], [480, 360]), ([60, 420], [60, 480]), 
          ([60, 540], [60, 600]), ([200, 540], [200, 600]), ([120, 300], [120, 340]), ([120, 390], [120, 420])]       
        
game = Game()
pygame.display.flip()

launched = True
while launched:
    #appliquer l'arrière plan
    window_surface.blit(background, (0,0))
    if game.is_playing:
        game.maj(window_surface, wall_x, wall_y, background, play, play_rect, ban, ban_rect)
    else: 
        window_surface.blit(play, play_rect)
        window_surface.blit(ban, ban_rect)
  
    #fermeture du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            pygame.quit()
            print('End of the game')
        # commencer le jeur
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                game.is_playing = True
        
    pygame.display.flip()