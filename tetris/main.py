import pygame
from game import Game
from grid import Grid

pygame.init()

screen = pygame.display.set_mode((400, 800))
game_grid = Grid()
game = Game(screen, game_grid)

running = True

while game.running:
    game.screen.fill("black")
    game.game_grid.draw(game.screen)
    game.current_tetro.draw(game.screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(game.game_grid.colors)
            game.game_grid.output_grid()
            game.running = False

        if event.type == game.timer_event:
            game.move_down()

    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_a]:
        game.move_left()
    if keys[pygame.K_d]:
        game.move_rigth()
    if keys[pygame.K_x]:
        game.rotate()
    if keys[pygame.K_z]:
        game.undo_rotation()

    pygame.display.flip()
    game.clock.tick(game.fps)

pygame.quit()
