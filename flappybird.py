import pygame
import os, sys

SCREEN_HEIGHT, SCREEN_WIDTH = 512, 284*2 #bg image dim: 284x512

class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y, img):
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.imgup, self.imgdown = img
        self.imgup_mask, self.imgdown_mask = pygame.mask.from_surface(self.imgup), pygame.mask.from_surface(self.imgdown)

    def display(self, screen):
        screen.blit(self.imgdown, (self.x, self.y))

def load_image():
    img = {}
    files = (os.listdir(os.path.join('.', 'assets')))
    files.remove('background.png')
    for f in files:
        i = pygame.image.load(os.path.join('.','assets', f))
        i.convert_alpha()
        img[f[:-4]] = i
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

    #initialise Bird
    birdy = Bird(0, SCREEN_HEIGHT/2, (image['bird_wing_up'], image['bird_wing_down']))

    birdy.display(screen)

    pygame.display.update();
    pygame.time.delay(10)
    sys.exit()

if __name__ == '__main__':
    main()
