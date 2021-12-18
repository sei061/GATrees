import pygame, sys, time, random
from pygame.locals import *
from GAengine import GAEngine

simulator_speed = 50

# add colors as needed...
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)
black_color = pygame.Color(0, 0, 0)
white_color = pygame.Color(255, 255, 255)

pygame.init()
fps_clock = pygame.time.Clock()

play_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Assignment 4 - DTE2501')

# initialize engine - you can experiment with different values for the population and food
ga = GAEngine()
ga.make_initial_population(100)
ga.add_food(1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                running = False

    # make your calls to GAEngine here...

    ga.assign_fitness()
    ga.do_crossover(len(ga.get_population()))

    play_surface.fill(white_color)
    for pp in ga.get_population():
        pygame.draw.rect(play_surface, black_color, Rect(pp.x_pos - 1, pp.y_pos - 1, 22, 22))
        pygame.draw.rect(play_surface, green_color, Rect(pp.x_pos, pp.y_pos, 20, 20))
    for food in ga.get_foods():
        food_size = food.get_amount() / 100 * 40
        pygame.draw.rect(play_surface, red_color, Rect(food.x_pos - food_size / 2, food.y_pos - food_size / 2, food_size, food_size))

    pygame.display.flip()

    fps_clock.tick(simulator_speed)