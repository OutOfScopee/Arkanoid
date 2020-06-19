import random
import time

import pygame
from round import Round


def main():
    pygame.init()

    done = False
    fps_counter = 0
    game_speed = 60
    display_scale = 1
    clock = pygame.time.Clock()
    retlange_height = 50
    retlange_width = 500
    screen_height = 1080//display_scale
    screen_width = 1920//display_scale
    screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((400, 400), pygame.HWSURFACE | pygame.DOUBLEBUF)
    x = 100
    y = screen_height//10*9
    moving_speed = 15
    round_finished = False
    paddle_power = 0
    print(1)

    # pygame.display.set_caption("Arkanoid Wiktorii")
    icon = pygame.image.load('graphics/background.jpg').convert_alpha()
    # pygame.display.set_icon(icon)

    start_time = time.time()
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    # print(start_time)
    pygame.font.init()
    stage = Round(1)
    print(2)
    while not done:
        print(3)
        fps_counter += 1
        pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP] and y > 0 :
        #     y = y - moving_speed
        # if pressed[pygame.K_DOWN] and y < 500 - retlange_height:
        #     y = y + moving_speed
        if pressed[pygame.K_RIGHT] and x < screen_width - retlange_width :
            x = x + moving_speed * paddle_power // 100
            if paddle_power < 100:
                paddle_power = paddle_power + 4
        if pressed[pygame.K_LEFT] and x > 0 :
            x = x - moving_speed * paddle_power // 100
            if paddle_power < 100:
                paddle_power = paddle_power + 4
        if not pressed [pygame.K_RIGHT] and not pressed [pygame.K_LEFT]:
            paddle_power = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True


       # pygame.draw.rect(object, (object_colour), pygame.Rect(x, y, object_width, object_height))
        #pygame.draw.rect(screen, (91, 44, 111), pygame.Rect(x, y, retlange_width, retlange_height))
        stage.draw(screen, x, y, retlange_width)
        pygame.draw.polygon(screen, (91, 44, 111), [[x, y + retlange_height], [x + retlange_width, y + retlange_height], [x + retlange_width // 2, y]])
        fps_per_sec = fps_counter / (time.time() - start_time)


        textsurface = myfont.render(str(round(fps_per_sec)), False, (0, 0, 0))
        screen.blit(textsurface, (20, 20))
        if stage.round_finished:
            textsurface = myfont.render("Level 1 finished", False, (0, 0, 0))
            screen.blit(textsurface, (500, 500))
            time.sleep(1)
            stage = Round(2)
        #pygame.draw.rect(screen, tuple(ball_colour), pygame.Rect(ball_position[0], ball_position[1], ball_diameter, ball_diameter))

        pygame.display.flip()
        clock.tick(120)



if __name__ == '__main__':
    main()