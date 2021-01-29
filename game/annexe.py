# -*- coding: utf-8 -*-

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        super().__init__()
        # self.health = 100
        # self.attack = 10
        self.speed= 1
        self.image = pygame.image.load('assets/chopper.png')
        # rect_form = pygame.Rect(0, 0, 10, 10)
        # self.image = pygame.draw.rect(window_surface, black_color, rect_form)
        self.cote = self.image.get_rect()
        self.hitbox = (self.cote.x, self.cote.y, 64, 64)
        
        self.but = pygame.image.load('assets/luffy.png')
        self.but_cote = self.but.get_rect()
        self.but_cote.y = 550
        self.but_cote.x = 550
        self.but_hitbox = (self.cote.x, self.cote.y, 64, 64)
        
        
    def dep_droite(self):
        self.cote.x += 1
        
    def dep_gauche(self):
        self.cote.x -= 1
        
    def dep_haut(self):
        self.cote.y -= 1
        
    def dep_bas(self): 
        self.cote.y += 1
        
    def but(self):
        self.but = pygame.image.load('assets/chopper.png')
        self.but.cote = self.image.get_rect()
        self.but.but.y = 600
        self.but.but.x = 600
        self.but.hitbox = (self.cote.x, self.cote.y, 64, 64)
    
        
        
class Game :
    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.pressed = {}
        
    # def end(self):
    #     if self.a:
    #        self.is_playing = False
        
    def maj(self, window_surface, wall_x, wall_y, background, play, play_rect, ban, ban_rect):
        #appliquer le joueur
        window_surface.blit(self.player.image, self.player.cote)
        window_surface.blit(self.player.but, self.player.but_cote)
        
        for i in wall_x:
    #for j in i:
            pygame.draw.line(background, (0,0, 0), i[0], i[1], 3)
        for i in wall_y:
    #for j in i:
            pygame.draw.line(background, (0,0, 0), i[0], i[1], 3)
     
        
        hitbox = (self.player.cote.x+12, self.player.cote.y+10, 25, 40)
        hitbox_but = (self.player.but_cote.x+12, self.player.but_cote.y+10, 25, 40)
        
        # chopper = pygame.Rect(window_surface, (255, 255, 255), hitbox, 1)
        # luffy = pygame.Rect(window_surface, (255, 255, 255), hitbox_but, 1)
        
        cho = pygame.draw.rect(window_surface, (255, 255, 255), hitbox, 1)
        lu = pygame.draw.rect(window_surface, (255, 255, 255), hitbox_but, 1)
        
        #collision line
        top= self.player.cote.top
        left = self.player.cote.left
        for i in wall_x:
            clip_x = cho.clipline((i[0], i[1]))
            if clip_x:
                if self.pressed.get(pygame.K_DOWN):
                    self.player.dep_haut() 
                elif self.pressed.get(pygame.K_UP):
                    self.player.dep_bas() 
                    self.player.dep_haut()
                    #print("clip_hb")
                    
                if i[0][1] - top <= 12:
                    self.player.dep_bas() 
        for i in wall_y:
            clip_y = cho.clipline((i[0], i[1]))
            
            if clip_y:
                if self.pressed.get(pygame.K_RIGHT):
                    self.player.dep_gauche()   
                   
                if self.pressed.get(pygame.K_LEFT):
                    self.player.dep_droite() 
                    self.player.dep_gauche()  
                if i[0][0] - left <= 12:
                    self.player.dep_droite() 
                
       
        if self.pressed.get(pygame.K_DOWN) and self.player.cote.y <= 550:
            self.player.dep_bas()
        if self.pressed.get(pygame.K_UP) and self.player.cote.y > 0:
            self.player.dep_haut()
        if self.pressed.get(pygame.K_LEFT) and self.player.cote.x > 0:
            self.player.dep_gauche()
        if self.pressed.get(pygame.K_RIGHT) and self.player.cote.x <= 550 :
            self.player.dep_droite()
            
        
        if cho.colliderect(lu):
            self.is_playing = False 
            launched = False
            pygame.quit()
   