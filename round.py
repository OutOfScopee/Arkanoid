import pygame

from arkanoid import ball
from arkanoid.ball import Ball
from arkanoid.block import Block


class Round:
    def __init__(self, number, screen_width = 1920, screen_height = 1080, background_path = "graphics/background1.jpg" ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.round_number = number
        self.round_finished = False
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.background = pygame.image.load(background_path).convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.block_image = pygame.image.load("graphics/block.png").convert_alpha()
        self.ball = Ball()
        self.blocks = []
        for line in range(1):
            for column in range(1):
                self.blocks.append(Block(position=(column * 150 + 360, line * 80 + 100), image= self.block_image))

    def draw(self, screen, x, y, retlange_width):
        for block in self.blocks:
            block.draw(screen)

        screen.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))
        for block in self.blocks:
            block.draw(screen)
        self.ball.screen_edge_bounce()
        self.ball.paddle_boucne((x, y), retlange_width)
        for block in self.blocks:
            block.check_for_hit(self.ball)
        if not self.round_finished:
            self.ball.move()
        # ball.move_to_screen(screen_width, screen_height)
        self.round_finished = True
        for block in self.blocks:
            if block.hits_to_dissaper > 0:
                self.round_finished = False

        self.ball.draw(screen)
        textsurface = self.myfont.render(str(self.round_number), False, (0, 0, 0))
        screen.blit(textsurface, (500, 500))

