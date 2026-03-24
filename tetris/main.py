import pygame
from game import Game
from grid import Grid

pygame.init()

screen = pygame.display.set_mode((400, 800))
game_grid = Grid()
game = Game(screen, game_grid)
font = pygame.font.Font(None, 36)
FPS = 60

while game.state != "quit":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state = "quit"

        if game.state == "playing":
            if event.type == game.timer_event:
                game.move_down()

        if game.state == "game_over":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game.reset()

    game.screen.fill("black")
    game.game_grid.draw(game.screen)

    if game.state == "playing":
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_a]:
            game.move_left()
        if keys[pygame.K_d]:
            game.move_right()
        if keys[pygame.K_x]:
            game.rotate()
        if keys[pygame.K_z]:
            game.undo_rotation()

        game.current_tetro.draw(game.screen)

    if game.state == "game_over":
        text_game_over = font.render("Game Over", True, "white")
        text_show_score = font.render(f"Score: {game.score}", True, "white")
        text_rect = text_game_over.get_rect(center=(200, 400))
        text_score_rect = text_show_score.get_rect(center=(200, 450))
        game.screen.blit(text_game_over, text_rect)
        game.screen.blit(text_show_score, text_score_rect)

    pygame.display.flip()
    game.clock.tick(FPS)

pygame.quit()
