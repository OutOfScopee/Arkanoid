import random
import time

import pygame

#def object(object_position, object_width, object_height, object_colour):
from arkanoid.ball import Ball
from arkanoid.block import Block



def main():
    pygame.init()

    done = False
    fps_counter = 0
    game_speed = 60
    display_scale = 1
    clock = pygame.time.Clock()
    retlange_height = 50
    retlange_width = 300
    screen_height = 1080//display_scale
    screen_width = 1920//display_scale
    screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((screen_height, screen_width), pygame.HWSURFACE | pygame.DOUBLEBUF)
    x = 100
    y = screen_height//10*9
    moving_speed = 15
    ball = Ball()

    block_image = pygame.image.load("../graphics/block.png").convert_alpha()


    blocks = []
    for line in range(5):
        for column in range(8):
            blocks.append(Block(position = (column * 150 + 360, line * 80 + 100), image = block_image))


    background = pygame.image.load("../graphics/background1.jpg").convert_alpha()
    background = pygame.transform.scale(background, (screen_width, screen_height))
    pygame.display.set_caption("Arkanoid Wiktorii")
    icon = pygame.image.load('../graphics/background.jpg').convert_alpha()
    pygame.display.set_icon(icon)

    start_time = time.time()
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    # print(start_time)
    while not done:
        fps_counter += 1
        pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP] and y > 0 :
        #     y = y - moving_speed
        # if pressed[pygame.K_DOWN] and y < 500 - retlange_height:
        #     y = y + moving_speed
        if pressed[pygame.K_RIGHT] and x < screen_width - retlange_width :
            x = x + moving_speed
        if pressed[pygame.K_LEFT] and x > 0 :
            x = x - moving_speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True


        ball.screen_edge_bounce()
        ball.paddle_boucne((x, y), retlange_width)
        for block in blocks:
            block.check_for_hit(ball)
        ball.move()
       # pygame.draw.rect(object, (object_colour), pygame.Rect(x, y, object_width, object_height))
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for block in blocks:
            block.draw(screen)
        pygame.draw.rect(screen, (91, 44, 111), pygame.Rect(x, y, retlange_width, retlange_height))
        ball.draw(screen)
        fps_per_sec = fps_counter / (time.time() - start_time)
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.

        textsurface = myfont.render(str(round(fps_per_sec)), False, (0, 0, 0))
        #pygame.draw.rect(screen, tuple(ball_colour), pygame.Rect(ball_position[0], ball_position[1], ball_diameter, ball_diameter))
        screen.blit(textsurface, (20, 20))
        pygame.display.flip()
        clock.tick(120)



if __name__ == '__main__':
    main()