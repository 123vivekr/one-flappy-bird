import pygame
import os
from random import randint
from math import pi, cos, sin, radians
from pygame.locals import *

SCREEN_HEIGHT, SCREEN_WIDTH = 512, 284*2 #bg image dim: 284x512
UP_ARROW, SPACE = 273, 32 #keyboard mapping

class Bird(pygame.sprite.Sprite):

    WIDTH = HEIGHT = 32

    def __init__(self, x, y, img):
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.imgup, self.imgdown = img
        self.imgup_mask, self.imgdown_mask = pygame.mask.from_surface(self.imgup), pygame.mask.from_surface(self.imgdown)

    def display(self, screen):
        screen.blit(self.imgdown, (self.x, self.y))

    def fall(self):
        for i in range(0, 5):
            self.y += i
            pygame.display.update()

    def jump(self):
        for i in range(60, 0, -30):
            self.y -= i
            pygame.display.update()
            

class Pipe(pygame.sprite.Sprite):

    WIDTH = 80
    PIECE_HEIGHT = 32

    def __init__(self, img):
        super(Pipe, self).__init__()
        self.imgbody, self.imgend = img
        self.total_pipe_body_pieces = int((SCREEN_HEIGHT - 3 * Bird.HEIGHT - 3 * Pipe.PIECE_HEIGHT - SCREEN_HEIGHT/6) / Pipe.PIECE_HEIGHT)
        # self.image = pygame.Surface((Pipe.WIDTH, SCREEN_HEIGHT), SRCALPHA)
        # self.image.convert()   # speeds up blitting
        # self.image.fill((0, 0, 0, 0))
        self.bottom_pieces = randint(1, self.total_pipe_body_pieces)
        self.top_pieces = self.total_pipe_body_pieces - self.bottom_pieces

        self.top_pieces += 1
        self.bottom_pieces += 1

        #self.mask = pygame.mask.from_surface(screen)

    def display(self, screen, x = 0):
        for i in range(1, self.bottom_pieces + 1):
            screen.blit(self.imgbody, (SCREEN_WIDTH - Pipe.WIDTH - x, SCREEN_HEIGHT - i * Pipe.PIECE_HEIGHT - SCREEN_HEIGHT/6))
        screen.blit(self.imgend, (SCREEN_WIDTH - Pipe.WIDTH - x, SCREEN_HEIGHT - self.bottom_pieces * Pipe.PIECE_HEIGHT - Pipe.PIECE_HEIGHT - SCREEN_HEIGHT/6))
        for i in range(self.top_pieces):
            screen.blit(self.imgbody, (SCREEN_WIDTH - Pipe.WIDTH - x, i * Pipe.PIECE_HEIGHT))
        screen.blit(self.imgend, (SCREEN_WIDTH - Pipe.WIDTH - x, self.top_pieces * Pipe.PIECE_HEIGHT))


def load_image():
    return {f[:-4]: pygame.image.load(os.path.join('.','assets', f)).convert_alpha() for f in os.listdir(os.path.join('.', 'assets'))}

def background(screen, bg, ground):
    screen.blit(bg, (0,0))
    screen.blit(bg, (284, 0))
    screen.blit(ground, (0, SCREEN_HEIGHT-60))

def main():
    #init window
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("One Flappy Bird")

    # cache all images
    image = load_image()
    image['ground'] = pygame.transform.scale(image['ground'], (int(SCREEN_WIDTH), int(SCREEN_HEIGHT/5))) #scale ground image
    image['pipe_body'] = pygame.transform.scale(image['pipe_body'], (55,55))
    image['pipe_end'] = pygame.transform.scale(image['pipe_end'], (55,55))

    # init background

    #initialise Bird
    birdy = Bird(SCREEN_WIDTH/2-50, (SCREEN_HEIGHT/2)-20, (image['bird_wing_up'], image['bird_wing_down']))
    pipe = Pipe((image['pipe_body'], image['pipe_end']))

    crashed = False
    clock = pygame.time.Clock()

    x = 0
    #game loop
    while not crashed:
        x += 1
        pygame.display.update()
        background(screen, image['background'], image['ground'])
        
        pipe.display(screen, x)
        birdy.display(screen)
        birdy.fall()
        event = pygame.event.get()
        for e in event:
            press = e.dict.keys()
            if('key' in press and 'unicode' not in press):
                if(e.dict['key'] in [SPACE, UP_ARROW]):
                    birdy.jump()
            if(not press):
                crashed = True
        clock.tick(20)

    pygame.quit()

if __name__ == '__main__':
    main()