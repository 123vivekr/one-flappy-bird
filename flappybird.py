import pygame
from os import path

SCREEN_HEIGHT, SCREEN_WIDTH = 512, 284*2 #bg image dim: 284x512

def main():
    #init window
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("One Flappy Bird")

    # init background
    bgImg = pygame.image.load(path.join('.','assets','background.png'))
    screen.blit(bgImg, (0,0))
    screen.blit(bgImg, (284, 0))


    pygame.display.update();
    pygame.time.delay(10)

if __name__ == '__main__':
    main()