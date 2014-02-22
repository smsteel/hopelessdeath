import pygame
from world_object import WorldObject
pygame.init()
size = width, height = 1280, 720
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
wo = WorldObject(FPS)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                wo.move_right()
        if event.type == pygame.KEYUP:
            wo.stop_moving()
    screen.fill(black)
    screen.blit(wo.animate(), wo.rect())
    pygame.display.flip()
    clock.tick(FPS)