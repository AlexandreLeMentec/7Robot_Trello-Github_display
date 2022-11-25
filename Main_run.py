import pygame
import numpy
import time
from Display import visual_interface

class Execute:
    def __init__(self, screen):
        self.fullscreen = False
        self.screenmax = False
        self.running = True
        self.screen_size = [500, 500]
        self.screen = screen
        self.test_image = pygame.image.load('Visual\Thomas.png')
        self.time = time.monotonic()
        self.interface = visual_interface()

    def display(self):
        pygame.display.flip()
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, self.screen_size[0], self.screen_size[1]))
        self.time = time.time()
        self.screen_size = pygame.display.get_window_size()
        self.interface.funk_display(self.screen, self.screen_size)
        #self.screen.blit(self.test_image, (self.screen_size[0]/2 - 249 / 2 + self.screen_size[0]/4 *
        #                                   numpy.cos(self.time), self.screen_size[1]/2 - 100) +
        #                                   self.screen_size[1]/4 * numpy.sin(self.time))

    def commands(self):
        for event in pygame.event.get():
            if event.type == pygame.WINDOWMAXIMIZED:
                self.fullscreen = True
            if event.type == pygame.WINDOWSIZECHANGED:
                self.fullscreen = False
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.fullscreen:
                        pygame.display.set_mode(self.screen_size, pygame.FULLSCREEN)
                        self.screenmax = True
                    if self.screenmax:
                        self.screenmax = False
                        pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)


    def run(self):
        while self.running:
            self.commands()
            self.display()


pygame.init()
screen1 = pygame.display.set_mode((1000, 500), pygame.RESIZABLE, pygame.SCALED)
execute = Execute(screen1)
execute.run()
