import pygame
import os
from random import randint

SCREEN_HEIGHT, SCREEN_WIDTH = 512, 284*2 #bg image dim: 284x512
UP_ARROW, SPACE = 273, 32 #keyboard mapping
FPS = 25

class Bird(pygame.sprite.Sprite):

    WIDTH = HEIGHT = 32 #bird img dimensions
    WING_UP = 1 #bird wing position

    def __init__(self, x, y, img):
        '''Load bird images'''

        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.imgup, self.imgdown = img
        self.imgup_mask, self.imgdown_mask = pygame.mask.from_surface(self.imgup), pygame.mask.from_surface(self.imgdown)

    def display(self, screen):
        '''Display bird to screen'''

        if(self.WING_UP == 1):
            screen.blit(self.imgup, (self.x, self.y))
        else:
            screen.blit(self.imgdown, (self.x, self.y))

    def fall(self):
        '''Note: values are chosen experimetally'''

        for i in range(0, 4):
            self.y += i
            pygame.display.update()

    def jump(self):
        '''Note: values are chosen experimetally'''

        for i in range(Bird.HEIGHT, 0, -20):
            self.y -= i
            pygame.display.update()
            

class Pipe(pygame.sprite.Sprite):

    #pipe img dimensions
    WIDTH = 80
    PIECE_HEIGHT = 32

    def __init__(self, img):
        '''inialise one pipe segment'''

        super(Pipe, self).__init__()
        #load images
        self.imgbody, self.imgend = img

        #pipe parts fiting
        self.total_pipe_body_pieces = int((SCREEN_HEIGHT - randint(4, 7) * Bird.HEIGHT - 3 * Pipe.PIECE_HEIGHT - SCREEN_HEIGHT/6) / Pipe.PIECE_HEIGHT)
        self.bottom_pieces = randint(1, self.total_pipe_body_pieces)
        self.top_pieces = self.total_pipe_body_pieces - self.bottom_pieces
        self.top_pieces += 1
        self.bottom_pieces += 1

    def display(self, screen, x = 0):
        '''pipe motion and display to screen'''

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
    pipes = [Pipe((image['pipe_body'], image['pipe_end'])) for i in range(2)]

    crashed = False
    clock = pygame.time.Clock()

    x = 0
    x2 = x + Pipe.WIDTH * randint(3, 6)
    #game loop
    while not crashed:
        x += 10 #1st pipe speed
        x2 += 10 #2nd

        #bird wings flap
        if(x % 30 == 0):
            birdy.WING_UP = birdy.WING_UP * -1

        pygame.display.update()
        background(screen, image['background'], image['ground'])

        pipes[0].display(screen, x % (500 + Pipe.WIDTH) - 15)
        xy2 = x2 % (500 + Pipe.WIDTH) - 15
                # if xy2 == -15:
            # val = randint(100, 500)
            # print(val)
            # xy2 = val
        pipes[1].display(screen, xy2)
        
        birdy.display(screen)
        birdy.fall()

        #get user input
        event = pygame.event.get()
        for e in event:
            press = e.dict.keys()
            if('key' in press and 'unicode' not in press):
                if(e.dict['key'] in [SPACE, UP_ARROW]):
                    birdy.jump()
            if(not press):
                crashed = True
        clock.tick(FPS) #FPS

    pygame.quit()

if __name__ == '__main__':
    main()