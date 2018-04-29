import pygame
import os

SCREEN_HEIGHT, SCREEN_WIDTH = 512, 284*2 #bg image dim: 284x512

class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y, img):
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.imgup, self.imgdown = img
        self.imgup_mask, self.imgdown_mask = pygame.mask.from_surface(self.imgup), pygame.mask.from_surface(self.imgdown)

    def display(self, screen):
        screen.blit(self.imgdown, (self.x, self.y))

class Pipe(pygame.sprite.Sprite):

    def init(self, img):
        super(Bird, self).__init__()
        self.imgbody, self.imgend = img
        self.imgbody_mask, self.imgdown_mask = pygame.mask.from_surface(self.imgbody), pygame.mask.from_surface(self.imgend)

def load_image():
    return {f[:-4]: pygame.image.load(os.path.join('.','assets', f)).convert_alpha() for f in os.listdir(os.path.join('.', 'assets'))}

def main():
    #init window
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("One Flappy Bird")

    # cache all images
    image = load_image()

    # init background
    screen.blit(image['background'], (0,0))
    screen.blit(image['background'], (284, 0))
    ground_scale = pygame.transform.scale(image['ground'], (int(SCREEN_WIDTH), int(SCREEN_HEIGHT/5)))
    screen.blit(ground_scale, (0, SCREEN_HEIGHT-90))

    #initialise Bird
    birdy = Bird(0, SCREEN_HEIGHT/2, (image['bird_wing_up'], image['bird_wing_down']))

    birdy.display(screen)

    pygame.display.update();
    pygame.time.delay(1000)

if __name__ == '__main__':
    main()
