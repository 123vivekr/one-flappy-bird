import pygame
import os

SCREEN_HEIGHT, SCREEN_WIDTH = 512, 284*2 #bg image dim: 284x512

class Bird:
    
    def __init__(x, y, wd):
        """wd: wing_down image"""


def load_image():
    img = {}
    files = (os.listdir(os.path.join('.', 'assets')))
    files.remove('background.png')
    for f in files:
        img[f[:-4]] = pygame.image.load(os.path.join('.','assets', f))
    return img

def main():
    #init window
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("One Flappy Bird")

    # init background
    bgImg = pygame.image.load(os.path.join('.','assets','background.png'))
    screen.blit(bgImg, (0,0))
    screen.blit(bgImg, (284, 0))

    # cache all images
    image = load_image()

    pygame.display.update();
    pygame.time.delay(10)

if __name__ == '__main__':
    main()