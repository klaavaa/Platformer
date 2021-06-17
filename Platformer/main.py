import pygame
import sys
from character import Character
from camera import Camera
from attributes import *
from obstacle import Obstacle
from world import World

def main():
    world = World(Character(), Camera(0, 0))
    world.obstacles.append(Obstacle(-10, 850, 800, 50))
    run = True
    pygame.init()
    win = pygame.display.set_mode((SW, SH ))
    clock = pygame.time.Clock()
    dt = clock.get_rawtime()
    fps = 144


    while run:

        clock.tick(fps)
        dt = clock.get_time() / 1000
        pygame.display.set_caption(f'fps: {int(clock.get_fps())}')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update(dt, world)
        draw(win, world)

    pygame.quit()



def update(dt, world):

    character = world.character
    cam = world.camera
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        character.x_vel = -1000
    if keys[pygame.K_d]:
        character.x_vel = 1000

    if keys[pygame.K_SPACE]:
        if character.is_on_ground and not character.has_jumped:
            character.y_vel = character.max_jump_vel
            character.is_on_ground = False
            character.has_jumped = True
            print("a")
    else:
        if not character.is_on_ground and character.has_jumped:
            if character.y_vel < character.min_jump_vel:
                character.y_vel = character.min_jump_vel
            character.has_jumped = False

    cam.update(character, SW, SH)

    character.update(dt, world )


def draw(win, world):

    character = world.character
    cam = world.camera
    win.fill(0)
    for obstacle in world.obstacles:
        obstacle.draw(pygame.draw.rect, win, cam.x, cam.y)


    character.draw(pygame.draw.rect, win, cam.x, cam.y)
    pygame.display.flip()



if __name__ ==  "__main__":
    main()

sys.exit()