import pygame

SCREEN_HEIGHT, SCREEN_WIDTH = 512, 284*2

def main():
    pygame.init()
    pygame.display.set_caption("One Flappy Bird")
    pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

if __name__ == '__main__':
    main()