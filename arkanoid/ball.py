import random
from math import sqrt, cos, sin

import pygame


class Ball:
    def __init__(self, screen_width = 1920, screen_height = 1080):
        self.position = [screen_width // 2, screen_height // 2]
        self.diameter = 60
        self.radius = self.diameter // 2
        self.move_vector = [0, -6]
        self.colour = [91, 44, 111]
        self.screen_width = screen_width 
        self.screen_height = screen_height
        self.center = [self.position[0] + self.diameter / 2, self.position[1] + self.diameter / 2]
        self.image = pygame.image.load('graphics/ball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.diameter, self.diameter))

    def rotation(self, old_vector, angle):
        return old_vector[0] * cos(angle) - old_vector[1] * sin(angle), old_vector[0] * sin(angle) + old_vector[1] * cos(angle)


    def paddle_boucne(self, paddle_position, paddle_width):
        
        if self.center[0] > paddle_position[0] and self.center[0] < paddle_position[0] + paddle_width \
                and self.move_vector[1] > 0 and self.center[1] < paddle_position[1] and self.position[1] + self.diameter + \
                self.move_vector[1] >= paddle_position[1]:
            self.move_vector[1] = -self.move_vector[1]
            paddle_center = paddle_position[0] + paddle_width / 2
            #Rotation after paddle bounce coafiction 2 at the end can equel from zero to three
            angle_change = (self.center[0] - paddle_center) / paddle_width * 3
            new_move = self.rotation(self.move_vector, angle_change)
            self.move_vector[1] = new_move[1]
            self.move_vector[0] = new_move[0]
            self.colour[0] = random.randint(0, 255)
            self.colour[1] = random.randint(0, 255)
            self.colour[2] = random.randint(0, 255)
            self.move_vector = [self.move_vector[0] * 1.1, self.move_vector[1] * 1.1]

    def screen_edge_bounce(self):
        if self.position[1] < 0:
            self.move_vector[1] = (-self.move_vector[1])
        if self.position[0] < 0:
            self.move_vector[0] = (-self.move_vector[0])
        if self.position[0] > self.screen_width - self.diameter:
            self.move_vector[0] = -self.move_vector[0]
        if self.position[1] > self.screen_height - self.diameter:
            self.move_vector[1] = (-self.move_vector[1])
        return self.move_vector
    def draw(self, screen):
        screen.blit(self.image, tuple(self.position))

    def move(self):
        self.position[0] = self.position[0] + self.move_vector[0]
        self.position[1] = self.position[1] + self.move_vector[1]
        self.center = [self.position[0] + self.diameter / 2, self.position[1] + self.diameter / 2]

    def move_to_screen(self, screen_width, screen_height):
        if self.position[0] < 0:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = 0
        if self.position[0] > screen_width - self.diameter:
            self.position[0] = screen_width - self.diameter - 1
        if self.position[1] > screen_height - self.diameter:
            self.position[0] = screen_height - self.diameter - 1



