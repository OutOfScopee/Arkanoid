import pygame

def main():

    pygame.init()
    done = False

    clock = pygame.time.Clock()
    sqare_size = 80
    screen_height = 500
    screen_width = 500
    x = 100
    y = 100
    moving_speed = 5
    screen = pygame.display.set_mode((screen_height, screen_width))
    while not done:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 0 :
            y = y - moving_speed
        if pressed[pygame.K_DOWN] and y < 500 - sqare_size:
            y = y + moving_speed
        if pressed[pygame.K_RIGHT]:
            x = x + moving_speed
        if pressed[pygame.K_LEFT]:
            x = x - moving_speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (91, 44, 111), pygame.Rect(x, y, sqare_size, sqare_size))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()