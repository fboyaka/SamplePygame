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
#title_button_play_extra=pygame.transform.scale_by(pygame.image.load("textures/title_button_play_extra.png"),2)

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

#totalmap=
#hitmap=

surface.blit(title_background,[0,0])
rect=pygame.Rect(0,0,75,75)
pygame.draw.rect(surface, (255,255,255),rect)

play=True
while play:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            play = False
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mousedown=1
        if ev.type == pygame.MOUSEBUTTONUP:
            mousedown=0
    mousepos=pygame.mouse.get_pos()
    #if area == -1:
        #if mousedown == 1 and rect.collidepoint(mousepos):

    pygame.display.flip()
    runtime=runtime+1
    clock.tick(60)