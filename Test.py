import pygame
import numpy

pygame.init()
screen1 = pygame.display.set_mode((1000, 500), pygame.RESIZABLE, pygame.SCALED)
running = True
screenmax = False
fullscreen = False
logo = pygame.image.load('Visual\logo_7robot.png')
logo_temp = pygame.image.load('Visual\logo_7robot_temp.png')
while running:
    logo_temp = pygame.image.load('Visual\logo_7robot_temp.png')
    ##
    screen_size = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.WINDOWMAXIMIZED:
            fullscreen = True
        if event.type == pygame.WINDOWSIZECHANGED:
            fullscreen = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if fullscreen:
                    pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
                    screenmax = True
                if screenmax:
                    screenmax = False
                    pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    ##
    pygame.draw.rect(screen1, (0, 0, 0), pygame.Rect(0, 0, screen_size[0], screen_size[1]))
    logo_temp = pygame.transform.scale(logo_temp, [int(screen_size[0]*0.75), int(screen_size[1]*0.75)])
    screen1.blit(logo_temp, (0, 0))
    pygame.display.flip()

