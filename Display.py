import pygame
import numpy

class visual_interface:
    def __init__(self):
        # 'item': [image_originale, image_resized, *x, *y, [current_w, current_h]]
        self.items = {'logo': [pygame.image.load("Visual\logo_7robot.png"),
                               pygame.image.load("Visual\logo_7robot_temp.png"), 0.6, 0.6, [600, 300]],
                      'catanim': [],
                      'electro_H1': [],
                      'electro_H2': [],
                      'electro_H3': [],
                      'electro_H4': [],
                      'electro_H5': [],}
        self.trello_dict = {}
        self.git_dict= {}
        self.temp_size = []
        self.first_size = False

    def background_anim(self):
        pass

    def image_temper(self, image, screen, size):
        pass

    def funk_display(self, screen, size):
        if self.temp_size != size:
            if not self.first_size:
                temp_logo = self.items['logo'][0]
                self.items["logo"][4][0] = int(self.items["logo"][4][0]*0.6)
                self.items["logo"][4][1] = int(self.items["logo"][4][1] * 0.6)
                temp_logo = pygame.transform.scale(self.items['logo'][0], [self.items["logo"][4][0], self.items["logo"][4][1]])
                pygame.image.save(temp_logo, "Visual\logo_7robot_temp.png")
                self.items['logo'][1] = temp_logo
                self.temp_size = size
                self.first_size = True

            else:
                temp_logo = self.items['logo'][0]
                self.items["logo"][4][0] = int(self.items["logo"][4][0] * (1920/size[0]))
                self.items["logo"][4][1] = int(self.items["logo"][4][1] * (1080/size[1]))
                temp_logo = pygame.transform.scale(self.items['logo'][0], [self.items["logo"][4][0],
                                                   self.items["logo"][4][1]])
                pygame.image.save(temp_logo, "Visual\logo_7robot_temp.png")
                self.items['logo'][1] = temp_logo
                self.temp_size = size
        else:
            screen.blit(self.items['logo'][1], (size[0]*0.6, 0))

    def trello_display(self):
        pass

    def trello_getter(self):
        pass

    def github_display(self):
        pass

    def github_getter(self):
        pass
