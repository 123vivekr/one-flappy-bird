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

    def fall(self):
        self.y += 15

    def jump(self):
        self.y-=10

class Pipe(pygame.sprite.Sprite):

    def init(self, img):
        super(Bird, self).__init__()
        self.imgbody, self.imgend = img
        self.imgbody_mask, self.imgdown_mask = pygame.mask.from_surface(self.imgbody), pygame.mask.from_surface(self.imgend)
    
    

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

    # init background

    #initialise Bird
    birdy = Bird(SCREEN_WIDTH/2-50, (SCREEN_HEIGHT/2)-20, (image['bird_wing_up'], image['bird_wing_down']))

    crashed = False
    clock = pygame.time.Clock()

    #game loop
    while not crashed:
        background(screen, image['background'], image['ground'])
        birdy.display(screen)
        pygame.display.update();
        birdy.fall()
        
        print("loop")
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
