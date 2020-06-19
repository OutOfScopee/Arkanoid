import pygame


class Block:
    def __init__(self, size = (30, 10), position = (100, 100), hits_to_dissaper = 1, image = None):
        self.image = image
        self.image = self.image.subsurface((513, 612, 1681 - 513, 1334 - 612))
        self.image = pygame.transform.scale(self.image,
                                             (self.image.get_rect().size[0] // 10,
                                              self.image.get_rect().size[1] // 10))
        self.size = (self.image.get_rect().size[0], self.image.get_rect().size[1])
        self.position = position
        self.hits_to_dissaper = hits_to_dissaper

    def draw(self, screen):
        if self.hits_to_dissaper > 0 :
            screen.blit(self.image, self.position)

    def check_for_hit(self, ball):

        if self.hits_to_dissaper > 0:
            if ball.center[0] > self.position[0] - ball.radius and ball.center[0] < self.position[0] \
            and ball.center[1] > self.position[1] and ball.center[1] < self.position[1] + self.size[1]:
                self.hits_to_dissaper = self.hits_to_dissaper - 1
                ball.move_vector[0] = -ball.move_vector[0]
            if ball.center[0] > self.position[0] + self.size[0] and ball.center[0] < self.position[0]  + self.size[0] + ball.radius  \
            and ball.center[1] > self.position[1] and ball.center[1] < self.position[1] + self.size[1]:
                self.hits_to_dissaper = self.hits_to_dissaper - 1
                ball.move_vector[0] = -ball.move_vector[0]
            if ball.center[0] > self.position[0] and ball.center[0] < self.position[0] + self.size[0] \
                and ball.center[1] < self.position[1] and  ball.center[1] > self.position[1] - ball.radius:
                self.hits_to_dissaper = self.hits_to_dissaper - 1
                ball.move_vector[1] = -ball.move_vector[1]
            if ball.center[0] > self.position[0] and ball.center[0] < self.position[0] + self.size[0] \
                and ball.center[1] > self.position[1] + self.size[1] and  ball.center[1] < self.position[1] + self.size[1] + ball.radius:
                self.hits_to_dissaper = self.hits_to_dissaper - 1
                ball.move_vector[1] = -ball.move_vector[1]

