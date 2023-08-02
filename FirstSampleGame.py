import sys, time, os
import random
import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

Screen_W = 800
Screen_H = 600
WHITE =(255, 255, 255)
Image_W = 300
Image_H = 200
FPS = 60

def get_random_position(screen_w, screen_h, image_w, image_h):
    random_x = random.randint(0, screen_w)
    random_y = random.randint(0, screen_h)

    return random_x, random_y

class Bug(pygame.sprite.Sprite):
    def __init__(self, width, heigt, randomX, randomY, ScreenW, ScreenH):
        super().__init__()
        self.Raw_image = pygame.image.load(os.path.join("image","bug01.png")).convert_alpha()
        self.image = pygame.transform.scale(self.Raw_image, (width, heigt))
        self.rect = self.image.get_rect()
        self.rect.topleft = (randomX, randomY)
        self.width = width
        self.height = heigt
        self.screenW = Screen_W
        self.screenH = ScreenH

def main():
    pygame.init()

    Screen=pygame.display.set_mode((Screen_W, Screen_H))
    pygame.display.set_caption("Bug War")
    random_x, random_y = get_random_position(Screen_W, Screen_W, Image_H, Image_W)
    bug =Bug(Image_W, Image_H, random_x, random_y, Screen_H, Screen_W)
    reload_bug_event = USEREVENT + 1
    pygame.time.set_timer(reload_bug_event, 300)
    points = 0
    my_font = pygame.font.SysFont(None, 30)
    hit_text = pygame.font.SysFont(None, 40)
    hit_text_surface = None
    main_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == reload_bug_event:
                bug.kill()
                random_x, random_y = get_random_position(Screen_W, Screen_W, Image_H, Image_W)
                bug =Bug(Image_W, Image_H, random_x, random_y, Screen_H, Screen_W)
            elif event.type == MOUSEBUTTONDOWN:
                if random_x < pygame.mouse.get_pos()[0] < random_x + Image_W and random_y < pygame.mouse.get_pos()[1] < random_y + Image_H:
                    bug.kill()
                    random_x, random_y = get_random_position(Screen_W, Screen_W, Image_H, Image_W)
                    bug =Bug(Image_W, Image_H, random_x, random_y, Screen_H, Screen_W)
                    hit_text_surface = hit_text.render("Hit!!", True, (0, 0, 0))
                    points += 5

        Screen.fill(WHITE)

        point_text_surface = my_font.render("Points: {}".format(points),True,(0,0,0))
        Screen.blit(bug.image,bug.rect)
        Screen.blit(point_text_surface,(10, 0))

        if hit_text_surface:
            Screen.blit(hit_text_surface, (10, 10))
            hit_text_surface = None

        pygame.display.update()
        main_clock.tick(FPS)

if __name__ == "__main__":
    main()

