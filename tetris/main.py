import pygame
from game import Game
from grid import Grid

pygame.init()

font = pygame.font.Font(None, 36)
text_game_over = font.render("Fim de Jogo", True, "white")
text_score = font.render("Pontuação", True, "white")
text_next_tetro = font.render("Próximo", True, "white")

text_score_rect = text_score.get_rect(center=(550, 50))
text_game_over_rect = text_game_over.get_rect(center=(200, 400))
text_next_tetro_rect = text_next_tetro.get_rect(center=(550, 200))

score_value_rect = pygame.Rect(450, 100, 200, 50)
next_tetro_rect = pygame.Rect(450, 250, 200, 200)

screen = pygame.display.set_mode((700, 800))
game_grid = Grid()
game = Game(screen, game_grid)
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

    score_value = font.render(str(game.score), True, "white")
    game.screen.fill("black")
    game.game_grid.draw(game.screen)
    screen.blit(text_score, text_score_rect)
    screen.blit(text_next_tetro, text_next_tetro_rect)

    pygame.draw.rect(screen, "gray", score_value_rect)
    pygame.draw.rect(screen, "gray", next_tetro_rect)
    game.draw_next_tetro(screen)

    screen.blit(
        score_value,
        score_value.get_rect(center=score_value_rect.center),
    )

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
        game.screen.blit(text_game_over, text_game_over_rect)

    pygame.display.flip()
    game.clock.tick(FPS)

pygame.quit()
