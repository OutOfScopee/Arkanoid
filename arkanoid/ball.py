import random

import pygame


class Ball:
    def __init__(self, screen_width = 1920, screen_height = 1080):
        self.position = [screen_width // 2, screen_height // 2]
        self.diameter = 60
        self.radius = self.diameter // 2
        self.move_vector = [8, 4]
        self.colour = [91, 44, 111]
        self.screen_width = screen_width 
        self.screen_height = screen_height
        self.center = [self.position[0] + self.diameter / 2, self.position[1] + self.diameter / 2]
        self.image = pygame.image.load('../graphics/ball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.diameter, self.diameter))

    def paddle_boucne(self, paddle_position, paddle_width):
        
        if self.center[0] > paddle_position[0] and self.center[0] < paddle_position[0] + paddle_width \
                and self.move_vector[1] > 0 and self.center[1] < paddle_position[1] and self.position[1] + self.diameter + \
                self.move_vector[1] >= paddle_position[1]:
            self.move_vector[1] = -self.move_vector[1]
            self.colour[0] = random.randint(0, 255)
            self.colour[1] = random.randint(0, 255)
            self.colour[2] = random.randint(0, 255)

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

