import math
import pygame
import sys

pygame.init()

clock = pygame.time.Clock()
surface = pygame.display.set_mode((640,360))

none_floor=""
hazard_floor=pygame.transform.scale_by(pygame.image.load("textures/hazard_floor.png"),2)
mountain_rock_floor=pygame.transform.scale_by(pygame.image.load("textures/mountain_rock_Floor.png"),2)
snow_floor=pygame.transform.scale_by(pygame.image.load("textures/snow_Floor.png"),2)
ice_floor=pygame.transform.scale_by(pygame.image.load("textures/ice_Floor.png"),2)
title_background=pygame.transform.scale(pygame.image.load("textures/title_background.png"),[640,360])
#player_down_idle_extra=pygame.image.load("textures/player_down_idle_extra.png")
#player_down_left_extra=pygame.image.load("textures/player_down_left_extra.png")
#player_down_right_extra=pygame.image.load("textures/player_down_right_extra.png")
#player_left_idle_extra=pygame.image.load("textures/player_left_idle_extra.png")
#player_left_left_extra=pygame.image.load("textures/player_left_left_extra.png")
#player_left_right_extra=pygame.image.load("textures/player_left_right_extra.png")
#player_up_idle_extra=pygame.image.load("textures/player_up_idle_extra.png")
#player_up_left_extra=pygame.image.load("textures/player_up_left_extra.png")
#player_up_right_extra=pygame.image.load("textures/player_up_right_extra.png")
#player_right_idle_extra=pygame.image.load("textures/player_right_idle_extra.png")
#player_right_left_extra=pygame.image.load("textures/player_right_left_extra.png")
#player_right_right_extra=pygame.image.load("textures/player_right_right_extra.png")
title_button_play_extra=pygame.transform.scale_by(pygame.image.load("textures/title_button_play_extra.png"),2)
title_button_new_game_extra=pygame.transform.scale_by(pygame.image.load("textures/title_button_new_game_extra.png"),2)
title_button_quit_extra=pygame.transform.scale_by(pygame.image.load("textures/title_button_quit_extra.png"),2)
title_button_load_extra=pygame.transform.scale_by(pygame.image.load("textures/title_button_load_extra.png"),2)

playerxtrue=0
playerxshown=0
playerytrue=0
playeryshown=0
#playerframe=(pygame.image.load("textures/player_down_idle_extra.png")
movementallowed=0
playerdirection=0
timewhentextboxstart=-1
mousedown=0
runtime=0
area=-1
timewhenquiteffectstart=-1
fadeoverlayeffectstrength=0
timewhenplayeffectstart = -1
thetaforplayeffect=0

#[[x,y,z,id,layername,texture],[]]
totalmap=[[380,170,0,0,"extra",title_button_play_extra],[380,270,0,1,"extra",title_button_quit_extra],[-280,170,0,2,"extra",title_button_load_extra],[-280,170,0,3,"extra",title_button_new_game_extra]]
#[[id,[data]],[]]
#objdata=
#hitmap=

playbuttonrect=title_button_play_extra.get_rect()
quitbuttonrect=title_button_quit_extra.get_rect()
loadbuttonrect=title_button_load_extra.get_rect()
newgamebuttonrect=title_button_new_game_extra.get_rect()

s = pygame.Surface((640,360), pygame.SRCALPHA)
s_alpha = 0




play=True
while play:
    surface.blit(title_background,[0,0])
    skimloc=0
    while not totalmap[skimloc][3]==0:
        skimloc+=1
    playbuttonrect.topleft=(totalmap[skimloc][0],totalmap[skimloc][1])
    surface.blit(title_button_play_extra,playbuttonrect.topleft)
    skimloc=0
    while not totalmap[skimloc][3]==1:
        skimloc+=1
    # quitbuttonrect.topleft=(totalmap[skimloc][0],totalmap[skimloc][1])
    surface.blit(title_button_quit_extra,quitbuttonrect.topleft)
    skimloc=0
    while not totalmap[skimloc][3]==2:
        skimloc+=1
    quitbuttonrect.topleft=(totalmap[skimloc][0],totalmap[skimloc][1])
    surface.blit(title_button_load_extra,loadbuttonrect.topleft)
    skimloc=0
    while not totalmap[skimloc][3]==3:
        skimloc+=1
    quitbuttonrect.topleft=(totalmap[skimloc][0],totalmap[skimloc][1])
    surface.blit(title_button_new_game_extra,newgamebuttonrect.topleft)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            play = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mousedown=1
        if ev.type == pygame.MOUSEBUTTONUP:
            mousedown=0
            if area == -1:
                if quitbuttonrect.collidepoint(mousepos):
                    timewhenquiteffectstart=runtime
                elif playbuttonrect.collidepoint(mousepos):
                    timewhenplayeffectstart=runtime
    if not timewhenquiteffectstart==-1 or fadeoverlayeffectstrength==100:
        fadeoverlayeffectstrength=(runtime-timewhenquiteffectstart)/(60/100)
        s_alpha = fadeoverlayeffectstrength * 2.55
        s.fill((0,0,0,s_alpha))
        surface.blit(s, (0,0))
    if fadeoverlayeffectstrength==100:
        s_alpha = fadeoverlayeffectstrength
        s.fill((0,0,0,s_alpha))
        surface.blit(s, (0,0))
        play=False
    if not (timewhenplayeffectstart==-1 or runtime-timewhenplayeffectstart >= 181):
        playbuttonrect.topleft=(380+thetaforplayeffect,playbuttonrect.topleft[1])
        print(playbuttonrect.topleft)
        skimloc=0
        while not totalmap[skimloc][3]==0:
            skimloc+=1
        totalmap[skimloc][0]=(380+10*thetaforplayeffect)
        skimloc=0
        thetaforplayeffect+=1
    mousepos=pygame.mouse.get_pos()
    pygame.display.flip()
    runtime=runtime+1
    clock.tick(60)